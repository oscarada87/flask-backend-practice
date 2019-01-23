from flask import Flask, request, render_template, send_file
from config import DevConfig
from searchID import IDCrawler
from searchET import ETCrawler
from jiebacut import jiebacut
from wordcloud import WordCloud ,ImageColorGenerator
from flask_cors import CORS
import json
# from flask_socketio import SocketIO, send, emit
import requests

from base64 import b64encode

# from rq import Queue
# from worker import conn

# q = Queue(connection=conn)
# from utils import count_words_at_url

# result = q.enqueue(count_words_at_url, 'https://flask-practice-crawler.herokuapp.com/test')

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = 'testtest'
CORS(app, supports_credentials=True)

# socketio = SocketIO(app)

def upload():
    headers = {"Authorization": "Client-ID 5d3ce8262b25794"}
    url = "https://api.imgur.com/3/image"
    j1 = requests.post(
        url, 
        headers = headers,
        data = {
            'image': b64encode(open('test.png', 'rb').read()),
            'type': 'base64',
            'name': 'test.png',
            'title': 'WordCloud'
        }
    )
    temp = str(j1.json()['data']['link'])
    return temp


# 路由和處理函式配對
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/153')
def EasterEgg():
    try:
        answer = request.args['key']
        answerList = ["forever", "infinity"]
        try:
            answer = int(answer)
            print(answer)
            if answer >= 30:
                return render_template('redirect/gallary_redirect.html')
            elif answer >= 10:
                return render_template('redirect/gallary_redirect1.html')
            else:
                print("else")
                return render_template('redirect/gallary_redirect2.html')
        except:               
            if answer.lower() in answerList:
                return "https://www.youtube.com/watch?v=AortXsrBjtY&feature=youtu.be&ab_channel=%E9%BB%83%E7%85%9C%E9%A8%B0"
            else:
                return render_template('redirect/gallary_redirect2.html')
    except:
        return render_template('gallary.html') 

@app.route('/resume')
def test():
    return render_template('resume.html')

@app.route('/friend')
def friend():
    try:
        answer = int(request.args['key'])
        if answer == 198:
            return "下個關鍵字是 153"
        else:
            return render_template('redirect/friend_redirect.html')
    except:
        return render_template('friend_gallary.html')

@app.route('/game')
def game():
    try:
        answer = request.args['key']
        if answer == "9487":
            return "下個關鍵字是 resume"
        else:
            return render_template('redirect/game_redirect.html')
    except:   
        return render_template('game.html')

@app.route('/test', methods=['POST','OPTION'])
def coding365():
    news = []
    crawlerList = []
    keyword = request.get_json()['keyword']
    crawlerList.append(IDCrawler(keyword))
    crawlerList.append(ETCrawler(keyword))

    for item in crawlerList:
        item.Start()
        news.extend(item.GetNews())    
    picture = jiebacut(news)
    picture.make()
    url = upload()
    return url

# @socketio.on('img')
# def test_message(message):
#     url = upload()
#     emit('img', {'url': url})

# @socketio.on('connect')
# def test_connect():
#     emit('connect', {'data': 'Connected'})

# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')


if __name__ == '__main__':
    app.run()

# https://www.youtube.com/watch?v=AortXsrBjtY&feature=youtu.be&ab_channel=%E9%BB%83%E7%85%9C%E9%A8%B0
# 生日影片連結
# 5/24 3/9 2/28 2/6 11/8 3/15 2/18 8/31 11/12