from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Hello, World!</h1>" \
    '<p> This is a paragraph</p>'\
    '<img src="http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcTEVcrypslvdUeHleSabemh-hXNLNslN-H0XVxm7ObA2J28dKoXFD5zck7QPMjyHGBCWXhq2nmA4YA0IYslGIM", width=200>' \
    '<img src="https://media.giphy.com/media/QFbwknaUKeY1SKyTqL/giphy.gif", width=200>'


@app.route('/bye')
def bye():
    return 'Bye!!!'

@app.route('/<name>')
def greet(name):
    return f'Hello there {name}'

@app.route('/username/<path:name>')
def greeting(name):
    return f'Hello there {name}'

if __name__ == '__main__':
    app.run()