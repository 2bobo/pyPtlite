# coding: UTF-8

import sys
import socket
import struct

COMANNDS = {'req_cmd' : 87,
            'D' : 0,                # Reset Patlite
            'R' : 1,                # Red Lighting
            'Y' : 2,                # Yellow Lighting
            'G' : 4,                # Green Lighting
            's' : 8,                # short Beep Sound
            'l' : 16,               # Long Beep sound
            'r' : 32,               # Red Flashing
            'y' : 64,               # Yellow Flashing
            'g' : 128 }             # Green Flashing

if len(sys.argv) != 4:
    print 'Usage: # python %s filename' % sys.argv[0]
    print "patlite.py IP PORT CMD \n\
           CMD list: \n\
            D: Reset Patlite \n\
            R: Red Lighting \n\
            Y: Yellow Lighting \n\
            G: Green Lighting \n\
            s: short Beep Sound \n\
            l: Long Beep sound \n\
            r: Red Flashing \n\
            y: Yellow Flashing \n\
            g: Green Flashing "

    quit()

else :
    host = sys.argv[1]
    port = int(sys.argv[2])
    cmds = sys.argv[3]

byte_data = 0
for cmd in cmds:
    byte_data += COMANNDS[cmd]

hex_rec_cmd = struct.pack("!H",COMANNDS["req_cmd"])[1]
hex_byte_data = struct.pack("!H",byte_data)[1]
send_data = hex_rec_cmd + hex_byte_data

# Sned Dara
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((host,port))
clientsock.send(send_data)

clientsock.close()
