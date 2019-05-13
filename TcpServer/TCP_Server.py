# -*- coding:utf-8 -*-
'''
Created by Administrator on 2019/4/22 0022.
'''
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime
import time

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# host = '127.0.0.1'
host = '127.0.0.1'
port = 7772
addr = (host, port)


class Servers(SRH):
    def handle(self):
        print 'got connection from ', self.client_address
        self.wfile.write('connection %s:%s at %s succeed!' % (host, port, ctime()))
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            # print data
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print "%s RECV from %s, data is:%s" % (cur_time, self.client_address[0], data)
            self.request.send(data)


print 'server is running....',host,":",port
server = SocketServer.ThreadingTCPServer(addr, Servers)
server.serve_forever()