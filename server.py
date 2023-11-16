"""

"""
from flask import jsonify, Flask, request
from db_connection import Database

app = Flask(__name__)


def url_strip(url):
    if "http://" in url or "https://" in url:
        url = url.replace("https://", '').replace("http://", '')\
            .replace('\"', '')
    return url


def extract_episode(url):
    if 'aniwave' in url:
        ep = url.split("/")[3]
        ep = ep.replace('ep-', '')

        show = url.split("/")[2]
        show = show.split(".")[0]

        return ep, show


@app.route('/send_url', methods=['POST'])
def send_url():
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    ep, show = extract_episode(parent_url)

    if ep:
        db_connect = Database()
        db_connect.connect('Watchlist.db')
        db_connect.add_episode(int(ep), show)
        db_connect.disconnect()

    return jsonify({'message': 'success!'}), 200
