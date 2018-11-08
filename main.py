from flask import Flask, request, render_template
from config import DevConfig
from searchID import IDCrawler
import json

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)
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
        if answer == 136:
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
            return "resume"
        else:
            return render_template('redirect/game_redirect.html')
    except:   
        return render_template('game.html')

if __name__ == '__main__':
    app.run()

# https://www.youtube.com/watch?v=AortXsrBjtY&feature=youtu.be&ab_channel=%E9%BB%83%E7%85%9C%E9%A8%B0
# 生日影片連結
# 5/24 3/9 2/28 2/6 11/8 3/15 2/18