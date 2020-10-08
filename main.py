from flask import Flask
from views import index_blu

# 创建flask应用对象
app = Flask(__name__)

# 用app对象注册蓝图
app.register_blueprint(index_blu)

if __name__ == '__main__':
    app.run(port=8899)
