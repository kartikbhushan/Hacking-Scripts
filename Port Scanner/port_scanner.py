import socket

class Scanner:
    def __init__(self , ip):
        self.ip = ip
        self.open_ports = []
        self.timeout = 0.1

    def __repr__(self) -> str:
        return 'Scanner: {}'.format(self.ip)

    def scan(self, lowerport , upperport):
        print("Scanning IP : {}".format(self.ip))
        print("Scanning Ports from range " + str(lowerport) + " - " + str(upperport))
        print("Default Socket timeout is set to {}".format(self.timeout))
        for port in range(lowerport , upperport+1):
            if self.is_open(port):
                self.open_ports.append(port)

    def is_open(self,port):
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.settimeout(self.timeout)
        result = s.connect_ex((self.ip , port))
        # print('port {}:    {}'.format(port, result))
        s.close()
        return result == 0

    def write(self, filepath):
        print("Results in  - open_ports")
        openports = map(str,self.open_ports)
        with open(filepath , 'w') as f:
            f.write("\n".join(openports))


def main():
    ip = '10.0.10.104'
    lowerport = 1
    upperport = 100
    scanner = Scanner(ip)
    scanner.scan(lowerport , upperport)
    print("ALL THE OPEN PORTS ARE: {}".format(scanner.open_ports))
    scanner.write("./open_ports")

if __name__ == '__main__':
    main()
