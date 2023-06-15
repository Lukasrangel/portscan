import socket
import sys


try:
	host = sys.argv[1];
except:
	print("Usage: nmap.py <host> <ports>")
	print("Ex: nmap.py 127.0.0.1 22,23,24,80,443")
	print("Caso não existam portas serão setadas as padrões");
	exit()

try:
	ports = sys.argv[2].split(',')
except:
	ports = [21,22,25,105,110,143,993,80,443,465,587,2222,2124,8081,8083,8080,3306];



for port in ports:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	code = sock.connect_ex((host, port))
	if code == 0:
		print("Porta {} aberta".format(port));
		try:
			client_2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
			client_2.settimeout(0.4);
			client_2.connect((host, port));
			client_2.send(b'GET /')
			service = client_2.recv(30).decode()
			print('-->', service)
		except:
			print("--> Unknow Service")




