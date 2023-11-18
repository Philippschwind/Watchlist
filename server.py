"""

"""
from flask import jsonify, Flask, request, render_template
from db_connection import Database
from Show import Show
from Episode import Episode

app = Flask(__name__, template_folder='template')
app.static_folder = 'static'


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
    else:
        return None, None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_url', methods=['POST'])
def send_url():
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    ep, show = extract_episode(parent_url)

    if ep:
        db_connect = Database('Watchlist.db')
        db_connect.add_episode(int(ep), show)
        db_connect.disconnect()

    return jsonify({'message': 'success!'}), 200


@app.route('/get_shows')
def get_shows():
    db_connect = Database('Watchlist.db')
    shows = db_connect.get_all_shows()
    db_connect.disconnect()

    shows_dict = []

    for show in shows:
        shows_dict.append({"id": show.show_id, "name": show.title, "episodeCount": show.ep_count or 0})

    return jsonify(shows_dict), 200


@app.route('/get_episodes')
def get_episodes():
    show_id = int(request.args.get('show_id'))
    db_connect = Database('Watchlist.db')
    show = db_connect.get_show_by_id(show_id)
    episodes = db_connect.get_episodes_for_show(show)
    db_connect.disconnect()

    ep_dict = []

    for ep in episodes:
        ep_dict.append({"id": ep.ep_nr, "name": ep.title})

    return jsonify(ep_dict), 200
