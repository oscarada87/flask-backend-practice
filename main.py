from flask import Flask, request, render_template, send_file
from config import DevConfig
from searchID import IDCrawler
from searchET import ETCrawler
from jiebacut import jiebacut
from wordcloud import WordCloud ,ImageColorGenerator
import json

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)

import sys, os
from os.path import dirname
sys.path.append(os.path.dirname(os.path.abspath(__file__))+'/jieba')

import jieba
jieba.tmp_dir = os.path.dirname(os.path.abspath(__file__)) + '/tmp'

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

@app.route('/test')
def coding365():
    news = []
    crawlerList = []
    try:
        keyword = request.args['key']
        crawlerList.append(IDCrawler(keyword))
        crawlerList.append(ETCrawler(keyword))
    except:
        return "Coding365測試用"

    for item in crawlerList:
        item.Start()
        news.extend(item.GetNews())    
    picture = jiebacut(news)
    picture.make()
    return send_file('test.png')


if __name__ == '__main__':
    app.run()

# https://www.youtube.com/watch?v=AortXsrBjtY&feature=youtu.be&ab_channel=%E9%BB%83%E7%85%9C%E9%A8%B0
# 生日影片連結
# 5/24 3/9 2/28 2/6 11/8 3/15 2/18 8/31 11/12