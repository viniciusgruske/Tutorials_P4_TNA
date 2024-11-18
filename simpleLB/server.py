#!/usr/bin/env python3
import sys

from scapy.all import (
    TCP,
    sniff
)
from scapy.layers.inet import _IPOption_HDR


def handle_pkt(pkt):
    if TCP in pkt and pkt[TCP].dport == 1234:
        print("got a packet")
        pkt.show2()
        sys.stdout.flush()

def main():

    if len(sys.argv)<2:
        print('pass 1 argument: interface name')
        exit(1)

    iface = sys.argv[1]
    print("sniffing on %s" % iface)
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()