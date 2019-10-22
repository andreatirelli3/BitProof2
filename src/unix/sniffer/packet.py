import struct


# Unpack ICMP packet
def icmp_packet(data):
    icmp_type, code, chksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, chksum, data[4:]