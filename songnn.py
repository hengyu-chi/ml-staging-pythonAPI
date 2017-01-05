# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
import redis
import json
from flask import request

#app = Flask(__name__)
app = Flask('SongNN Eyeball')
app.secret_key = 'oc28251-T12aBZFz3Eo53KFc'

default_algo_id = 'Bp'

def songnn_get_neighbors(algo_id, song_id):
    redis_conn = redis.StrictRedis(host='192.168.200.112', port=6389, db=0)
    key = 'song2song_0_' + algo_id + '_' + song_id
    print key
    data = [song_id] + redis_conn.lrange(key, 0, 50)
    jsonData = json.dumps(map(int, data))
    print request.remote_addr + ":" +  algo_id + "-" + song_id
    print jsonData
    return jsonData

@app.route("/song/<string:song_id>")
def songnn_default(song_id='-1'):
    print default_algo_id, song_id
    return songnn_get_neighbors(default_algo_id, song_id)

@app.route("/songnn/<string:algo_id>/<string:song_id>")
def songnn(algo_id, song_id):
    print algo_id, song_id
    return songnn_get_neighbors(algo_id, song_id)


app.run(host='0.0.0.0', port=12345, debug=True)
