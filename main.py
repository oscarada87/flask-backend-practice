from flask import Flask, request, render_template
from config import DevConfig
from searchID import IDCrawler
import json

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)
# 路由和處理函式配對
@app.route('/153')
def birthday():
    if request.method == 'GET':
        try:
            test = IDCrawler(request.args['keyword'])
            test.Start()
            news = test.GetNews()
            return str(news)
        except:
            text = "答案錯誤!!!"
            return text

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/EasterEgg')
def EasterEgg():
    return render_template('gallary.html')

@app.route('/test')
def test():
    return render_template('resume.html')

@app.route('/friend')
def friend():
    try:
        answer = int(request.args['key'])
        if answer == 116:
            return "下個關鍵字是 EasterEgg"
        else:
            return render_template('redirect/friend_redirect.html')
    except:
        return render_template('friend_gallary.html')

if __name__ == '__main__':
    app.run()

# https://www.youtube.com/watch?v=AortXsrBjtY&feature=youtu.be&ab_channel=%E9%BB%83%E7%85%9C%E9%A8%B0
# 生日影片連結
# 5/24 3/9 2/28 2/6 11/8 3/15