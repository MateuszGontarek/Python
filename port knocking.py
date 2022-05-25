import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(5)
ip = "10.0.70.114"  # IP address
xd = "xd"

for p1 in range(8000,8100):
    for p2 in range(8000, 8100):
        for p3 in range(8000, 8100):
            for _ in range(2):
                s.connect((ip, p1))
                s.send(xd.encode())
                s.connect((ip, p2))
                s.send(xd.encode())
                s.connect((ip, p3))
                s.send(xd.encode())
                print(p1, p2, p3)