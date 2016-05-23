# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
import time
import json

from pytgbot import VERSION

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    import urlparse
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import urllib.parse as urlparse
# end try

# import ssl

logger = logging.getLogger(__name__)


HOST_NAME = ""
PORT_NUMBER = 22113
CERT_FILE = '/path/to/localhost.pem'

logging.basicConfig()


def handle_hook(payload):
    logger.info("payload: " + payload)


class HookHandler(BaseHTTPRequestHandler):
    server_version = "pytgbot/%s" % VERSION

    def do_GET(self):
        self.do_STUFF("get")

    #

    def do_POST(self):
        # Check that the IP is within the GH ranges
        # if not any(s.client_address[0].startswith(IP)
        #            for IP in ('192.30.252', '192.30.253', '192.30.254', '192.30.255')):
        # s.send_error(403)
        self.do_STUFF("post")

    def do_STUFF(self, how):
        # logger.warn("asdasd!")
        length = int(self.headers['Content-Length'])
        print(self.headers)
        post_data = urlparse.parse_qs(self.rfile.read().decode('utf-8'))
        logger.warn("data: " + post_data)
        payload = json.loads(post_data['payload'][0])
        self.send_response(200)
        self.handle_hook(payload)

    def handle_hook(self, payload):
        # TODO process
        self._callback(payload)

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value

class HookHTTPServer(HTTPServer):
    def handle_request(self,request):
        pass


if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), HookHandler)
    def handle_request(request,):
        #httpd.socket = ssl.wrap_socket(httpd.socket, certfile=CERT_FILE)
        pass
    print("{time} Server Starts - {host}:{port} (using certificate (.pem) from {cert})".format(time=time.asctime(),
                                                                                               host=HOST_NAME,
                                                                                               port=PORT_NUMBER,
                                                                                               cert=CERT_FILE))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("{time} Server Stops - {host}:{port} (using certificate (.pem) from {cert})".format(time=time.asctime(),
                                                                                              host=HOST_NAME,
                                                                                              port=PORT_NUMBER,
                                                                                              cert=CERT_FILE))
