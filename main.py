from flask import Flask
from flask import request
from config import DevConfig
from searchID import IDCrawler
import json

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)
# 路由和處理函式配對
@app.route('/')
def index():
    if request.method == 'GET':
        test = IDCrawler(request.args['keyword'])
        test.Start()
        news = test.GetNews()
        return str(news)
        
if __name__ == '__main__':
    app.run()