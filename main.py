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
    text = "歡迎光臨!!"
    return text

@app.route('/EasterEgg')
def test():
    return render_template('gallary.html')

if __name__ == '__main__':
    app.run()