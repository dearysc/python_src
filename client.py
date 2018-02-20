import socket
import json
if __name__ == '__main__':
	obj = {"Act":"Request"}
	str = json.dumps(obj)
	print str
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(('192.168.2.115',8080))
	sock.send(str);
	
	data = sock.recv(1024);
	print data
