#!/usr/bin/python3
import http.server

PORT =8889
server_address = ("",PORT)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
print("Serveur actif sur le port: ",PORT)

httpd = server(server_address,handler)
httpd.serve_forever()

