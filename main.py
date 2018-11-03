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
    text = """歡迎光臨!!
              遊戲玩法:
              1. 在網址列後輸入各種英文單字即可切換到另一個頁面
              EX: https://flask-practice-crawler.herokuapp.com/test
              2. 某些頁面需要密碼才會提供獎勵，密碼測試方式請在網址後面加上 "key='你的密碼'"
                 因為沒時間寫前端，所以就將就一點吧
              EX: https://flask-practice-crawler.herokuapp.com/test?key=簡子融                
    """
    return text

@app.route('/EasterEgg')
def EasterEgg():
    return render_template('gallary.html')

@app.route('/test')
def test():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run()