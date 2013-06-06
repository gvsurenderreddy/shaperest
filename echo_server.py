import urllib3

from flask import Flask
from flask import request
app = Flask(__name__)

available_methods = ['GET', 'POST', 'DELETE', 'OPTIONS', 'HEAD', 'PUT']
http = urllib3.PoolManager()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=available_methods)
def handle_request(path):
    return 'You %s path: %s\n' % (request.method, path)

if __name__ == '__main__':
    app.run(debug=True)
