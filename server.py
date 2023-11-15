"""

"""
from flask import jsonify, Flask, request

app = Flask(__name__)


def url_strip(url):
    if "http://" in url or "https://" in url:
        url = url.replace("https://", '').replace("http://", '')\
            .replace('\"', '')
    if "/" in url:
        url = url.split('/', 1)[0]
    return url


@app.route('/send_url', methods=['POST'])
def send_url():
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    return jsonify({'message': 'success!'}), 200
