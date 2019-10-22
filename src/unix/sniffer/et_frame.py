import struct


# Unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac = struct.unpack('! 6s 6s', data[:12])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), data[:14], data[14:]


# Return formatted MAC address (AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()