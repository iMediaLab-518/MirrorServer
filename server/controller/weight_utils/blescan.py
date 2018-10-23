import struct
import bluetooth._bluetooth as bluez

LE_META_EVENT = 0x3e
OGF_LE_CTL = 0x08
OCF_LE_SET_SCAN_ENABLE = 0x000C

EVT_LE_ADVERTISING_REPORT = 0x02


def returnnumberpacket(pkt):
    myInteger = 0
    multiple = 256
    for c in pkt:
        myInteger += struct.unpack("B", c)[0] * multiple
        multiple = 1
    return myInteger


def returnstringpacket(pkt):
    myString = ""
    for c in pkt:
        myString += "%02x" % struct.unpack("B", c)[0]
    return myString


def get_packed_bdaddr(bdaddr_string):
    packable_addr = []
    addr = bdaddr_string.split(':')
    addr.reverse()
    for b in addr:
        packable_addr.append(int(b, 16))
    return struct.pack("<BBBBBB", *packable_addr)


def packed_bdaddr_to_string(bdaddr_packed):
    return ':'.join('%02x' % i for i in struct.unpack("<BBBBBB", bdaddr_packed[::-1]))


def hci_enable_le_scan(sock):
    hci_toggle_le_scan(sock, 0x01)


def hci_disable_le_scan(sock):
    hci_toggle_le_scan(sock, 0x00)


def hci_toggle_le_scan(sock, enable):
    cmd_pkt = struct.pack("<BB", enable, 0x00)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_LE_SET_SCAN_ENABLE, cmd_pkt)


def parse_events(sock, loop_count=100):
    old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)

    flt = bluez.hci_filter_new()
    bluez.hci_filter_all_events(flt)
    bluez.hci_filter_set_ptype(flt, bluez.HCI_EVENT_PKT)
    sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, flt)
    myFullList = []
    for i in range(0, loop_count):
        pkt = sock.recv(255)
        ptype, event, plen = struct.unpack("BBB", pkt[:3])
        if event == LE_META_EVENT:
            subevent, = struct.unpack("B", pkt[3])
            pkt = pkt[4:]
            if subevent == EVT_LE_ADVERTISING_REPORT:
                num_reports = struct.unpack("B", pkt[0])[0]
                report_pkt_offset = 0
                for _ in range(0, num_reports):
                    Adstring = packed_bdaddr_to_string(pkt[report_pkt_offset + 3:report_pkt_offset + 9])
                    Adstring += ","
                    Adstring += returnstringpacket(pkt[report_pkt_offset - 22: report_pkt_offset - 6])
                    Adstring += ","
                    Adstring += "%i" % returnnumberpacket(pkt[report_pkt_offset - 6: report_pkt_offset - 4])
                    Adstring += ","
                    Adstring += "%i" % returnnumberpacket(pkt[report_pkt_offset - 4: report_pkt_offset - 2])
                    Adstring += ","
                    Adstring += "%i" % struct.unpack("b", pkt[report_pkt_offset - 2])
                    Adstring += ","
                    Adstring += "%i" % struct.unpack("b", pkt[report_pkt_offset - 1])

                    myFullList.append(Adstring)
    sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, old_filter)
    return myFullList
