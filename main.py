import socket

def egress_tester(host, port):
    print(f"Starting connection test for {host} on port {port}...")
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connection timeout
            sock.settimeout(2)
            # Connection attempt
            sock.connect((host, port))
            print(f"Successfully connected to {host} on port {port}")
            return True
    except (socket.timeout, socket.error) as e:
        print(f"Failed to connect to {host} on port {port}: {e}")
        return False

def main():
    host = "portquiz.net"
    ports = [80,445]

    for port in ports:
        egress_tester(host, port)
