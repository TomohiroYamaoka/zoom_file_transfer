# coding: utf-8
import http.server
import socketserver
import json


class Handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        request_body = self.__get_body()
        print(request_body)
        self.send_response(200)
        fetchTargetJsonContent(request_body)

    def __get_body(self):
        content_len = int(self.headers['content-length'])
        request_body = json.loads(self.rfile.read(content_len).decode('utf-8'))
        return request_body


with http.server.HTTPServer(('', 3000), Handler) as httpd:
    httpd.serve_forever()


def fetchTargetJsonContent(request_body):
    url = request_body["download_url"]
    print(url)
    token = request_body["download_token"]
    print(token)
    headers = {"Authorization": "Bearer {}".format(token)}
    print(headers)
    #transferToBox(url, token)


# def transferToBox(url, token):
#    return
