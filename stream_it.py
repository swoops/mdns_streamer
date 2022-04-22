import sys
import random
import time
import socket
from struct import pack,unpack

def encode_name(host):
    h = host.split(".")
    if len(h) != 2:
        raise Exception("Not correct number of dots, sections: %d" % len(h))

    buf = b''
    for n,i in enumerate(h):
        l = len(i)
        if l > 255:
            raise Exception("Len %d sec %d too big" % (l, i))
        buf += pack("B", l)
        buf += i.encode("utf-8")
    return buf

def ask_question(host, sock):
    l = len(host)
    buf  = b""
    for i in range(12):
        buf += pack(">B", random.randint(0,255))
    buf += encode_name(host)
    sock.sendto(buf, ("224.0.0.251", 5353)) # broadcast

def play_file(fname, sock):
    global t
    ask_question("wooo.\x1b[2J\x1b[H", sock)
    skip = False
    print("Playing %s" % fname)
    with open(fname) as fp:
        video = fp.read()
    frame_cnt = 0
    for n,host in enumerate(video.split("\nSPLIT\n")):
        # play every t'th full frame
        if host[0:3] == "\x1b[H":
            if frame_cnt % t == 0:
                skip = False
            else:
                skip = True
            frame_cnt += 1
            time.sleep(.075)
            sys.stdout.write("%s frame %d\r" % (fname, frame_cnt ))

        if skip: continue
            
        time.sleep(.013)
        ask_question(host, sock)
    print("")

t = 3
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for fname in sys.argv[1:]:
    play_file(fname, sock)
sock.close()
