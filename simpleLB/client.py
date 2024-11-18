#!/usr/bin/env python3
import random

from scapy.all import IP, TCP, Ether, get_if_hwaddr, sendp

def main():
    pkt =  Ether(src=get_if_hwaddr("enp132s0f0np0"), dst='ff:ff:ff:ff:ff:ff')
    pkt = pkt /IP(dst="10.0.1.100") / TCP(dport=1234, sport=random.randint(49152,65535)) / "teste"
    pkt.show2()
    sendp(pkt, iface="enp132s0f0np0", verbose=False)

if __name__ == '__main__':
    main()