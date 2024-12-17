import socket
import sys

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
    # Default host and ports
    host = "portquiz.net"
    ports = [21, 22, 23, 25, 53, 80, 443, 445, 3389]

    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        try:
            ports = [int(port) for port in sys.argv[1:]]
        except ValueError:
            print("Invalid port number provided. Please enter valid integers.")
            return
    else:
        ports = default_ports

    for port in ports:
        egress_tester(host, port)

if __name__ == "__main__":
    print("Starting the port testing script...")
    main()
