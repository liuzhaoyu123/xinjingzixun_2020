from . import index_blu


@index_blu.route("/")
def index():
    return "我是zz主页"
