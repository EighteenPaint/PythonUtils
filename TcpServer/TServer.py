# -*- coding:utf-8 -*-
'''
Created by Administrator on 2019/4/22 0022.
'''
import socket
import sys
def start_tcp_server(ip, port):
  #create socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (ip, port)
  #bind port
  print 'starting listen on ip %s, port %s'%server_address
  sock.bind(server_address)
  #starting listening, allow only one connection
  try:
    sock.listen(1)
  except socket.error, e:
    print "fail to listen on port %s"%e
    sys.exit(1)
  while True:
    print "waiting for connection"
    client,addr = sock.accept()
    print 'having a connection',client,addr
    client.sendall("Thank PDT")
    client.close()
if __name__ == '__main__':
  ip = socket.gethostbyname(socket.gethostname())
  start_tcp_server(ip, 7773)