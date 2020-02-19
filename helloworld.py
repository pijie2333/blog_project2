from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '这里是pijie233的个人博客'


if __name__ == '__main__':
    app.run()
