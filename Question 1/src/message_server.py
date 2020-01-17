"""

message_server.py
@author: wylieagab

"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import hashlib

PORT = 8080
hash_dict = {}

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''
        Recieves and processes GET request. Entry checking could be implemented further
        to do a more robust check to ensure valid requests. Implementation relies on 
        correct input. 
        '''

        messages_index = 1
        hash_index = 2
        path = self.path.split("/")
        messages_checker = path[messages_index]
        hash_val = path[hash_index]

        if messages_checker != "messages":
            self.invalid_request("invalid_path")
        elif hash_val in hash_dict:
            self.process_get_request(hash_val)
        else:
            self.invalid_request("invalid_hash")

    def process_get_request(self, hash_val):
        '''
        Creates and sends a response to the client given an existing hash.
        '''

        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'\n{\n\n "message": "')
        response.write(str.encode(hash_dict[hash_val]))
        response.write(b'" \n\n}\n\n')
        self.wfile.write(response.getvalue())


    def do_POST(self):
        '''
        Captures POST request and determines if the path is correct.
        '''
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        if self.path == "/messages":
            self.construct_post_response(body)
        else:
            self.invalid_request('invalid_path')

    def construct_post_response(self, body):
        '''
        Constructs POST response given the message body
        '''
        message_index = 1
        message = body.decode('utf-8')
        split_message = message.split(':')[1].split('"')

        if len(split_message) != 3:
            self.invalid_request("unsupported_input")
        else:
            self.send_response(200)
            self.end_headers()
            message = split_message[message_index]
            message_encoded = str.encode(message)
            hash_val = hashlib.sha256(message_encoded).hexdigest()
            hash_dict[hash_val] = message
            response = BytesIO()
            response.write(b'\n{\n\n "digest": "')
            response.write(str.encode(hash_val))
            response.write(b'" \n\n}\n\n')
            self.wfile.write(response.getvalue())
        
    
    def invalid_request(self, error):
        '''
        Generates response for a given invalid request
        '''

        response = BytesIO()

        if error == "invalid_path":
            response.write(b'\n{\n\n "err_msg": "invalid path" \n\n}\n\n')
            self.wfile.write(response.getvalue())
        elif error == "invalid_hash":
            response.write(b'\n{\n\n "err_msg": "Message not found" \n\n}\n\n')
            self.wfile.write(response.getvalue())
        elif error == "unsupported_input":
            response.write(b'\n{\n\n "err_msg": "unsupported input" \n\n}\n\n')
            self.wfile.write(response.getvalue())

        self.send_response(404, message=None)
        self.end_headers()
        
httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
