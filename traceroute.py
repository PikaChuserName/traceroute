from scapy.all import *

TIMEOUT = 3

def main():
    dst = raw_input('Destination IP:')

    ttl = 0
    while 1:
        ping = IP(dst=dst, ttl=ttl)/ICMP(type=8)
        result = sr1(ping, timeout=TIMEOUT)
        if result == None:
            print 'Timeout'
        elif result.type == 11:
            print result.src
        else:
            print result.src
            break
        ttl += 1            
   
if __name__== "__main__":
    main()        



