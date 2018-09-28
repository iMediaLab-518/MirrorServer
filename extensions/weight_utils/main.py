# -*- coding:utf-8 -*-

import blescan
import bluetooth._bluetooth as bluez
import sys

MAC = sys.argv[1]

dev_id = 0

sock = bluez.hci_open_dev(dev_id)

blescan.hci_enable_le_scan(sock)

measured_anterior = 0

info_number = 0

while True:
    returnedList = blescan.parse_events(sock, 1)
    if len(returnedList) > 0:
        (mac, uuid, major, minor, txpower, rssi) = returnedList[0].split(',', 6)
        if mac.upper() == MAC:
            info_number += 1
            measunit = uuid[22:24]
            measured = int((uuid[26:28] + uuid[24:26]), 16) * 0.01
            unit = ''

            if measunit.startswith(('03', 'b3')):
                unit = 'lbs'
            if measunit.startswith(('12', 'b2')):
                unit = 'jin'
            if measunit.startswith(('02', 'a2')):
                unit = 'Kg'
                measured = measured / 2

            if measunit.startswith(('a', 'b')) and info_number > 10:
                print("%s %s" % (measured, unit))
                break
            # 测量10条数据以上才启用 防止刚连接蓝牙时获取到上一次的数据

            # if unit:
            #     if measured != measured_anterior:
            #         print("measured : %s %s %s" % (measured, unit, measunit))
            #         measured_anterior = measured
