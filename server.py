#  coding: utf-8 
import SocketServer

#  Copyright 2013 Abram Hindle, Eddie Antonio Santos, Yu Zuo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/

return_404 = "HTTP/1.1 404 Not Found\r\n"
return_css = "HTTP/1.1 200 OK\nContent-type: text/css\r\n\r\n"
return_html = "HTTP/1.1 200 OK\nContent-type: text/html\r\n\r\n"

class MyWebServer(SocketServer.BaseRequestHandler):


    def Html_decete(self,URL):
            final_request = return_html
            f = open(URL, 'r')
            for each_line in f:
                final_request=final_request+each_line
            f.close()
	    self.request.sendall(final_request)
    
            
    def Css_decete(self,URL):
        final_request = return_css
        f = open(URL, 'r')
        for each_line in f:
        	final_request=final_request+each_line
        f.close()
    	self.request.sendall(final_request)
    
    def detect_URL(self, URL):
        URL_size = len(URL)
        URL_con=URL[1:URL_size]
        if(URL[URL_size-1]=="/"):
            URL_con=URL_con[0:len(URL_con)-1]
        URL_con="www/"+URL_con
        return URL_con    
        
    def handle(self):
        URL=""
        self.data = self.request.recv(1024).strip()
        if self.data != "":
            userData=self.data.split()
            URL =self.detect_URL(userData[1])
        
        if(URL == "www/"):
            URL = "www/index.html"
        if (URL == "www/deep"):
            URL = "www/deep/index.html"
            
        try:
            testF = open(URL,"r")
            testF.close()
        except :
            self.request.sendall(return_404)
            
        index = "www/index.html"
        deep_index = "www/deep/index.html"
        base = "www/base.css"
        deep_deep = "www/deep/deep.css"
        
        
        if "etc/group" in URL:
            self.request.sendall(return_404)        
        elif "deep/index.html" in URL:
            self.Html_decete(deep_index) 
        elif "index.html" in URL:
            self.Html_decete(index)
        elif "base.css" in URL:
            self.Css_decete(base)        
        elif "deep.css" in URL: 
            self.Css_decete(deep_deep)        

        
        
        
        
        
        
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
