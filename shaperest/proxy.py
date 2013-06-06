import urllib3

from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

available_methods = ['GET', 'POST', 'DELETE', 'OPTIONS', 'HEAD', 'PUT']
http = urllib3.PoolManager()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=available_methods)
def handle_request(path):
    url = 'https://172.16.207.202/%s' % path
    r = http.request(request.method, url, fields=request.form)
    resp = make_response(r.data, r.status)
    resp.headers = r.headers.copy()
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5001)
