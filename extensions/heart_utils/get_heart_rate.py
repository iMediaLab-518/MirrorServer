from base import MiBand2
import sys

MAC = sys.argv[1]

band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")
band.authenticate()

heart = band.start_raw_data_realtime().next()
print(heart)
band.disconnect()