from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_page():
    return "<a href='/'>첫페이지</a> <a href='/hello'>Hello!</a> <a href='/gugu/<dan>'>구구단</a><p>첫페이지 입니다!</p>"

@app.route("/hello")
def hello_world():
    return "<a href='/'>첫페이지</a> <a href='/hello'>Hello!</a> <a href='/gugu/<dan>'>구구단</a><p>Hello world!</p>"

@app.route("/gugu/<dan>")
def gugudan(dan):
    dan = int(dan)


    resp += '<html>\n'
    resp += '<body>\n
    resp += f'<h2>{dan}단</h2>\n
    resp += '<div>\n
    for i in range(1, 10):
        resp += f'{dan} X {i:2d} = {dan * i:02d}<br>\n
    resp += '</div>\n
    resp += '</body>\n
    resp += '</html>\n

    return resp


app.run(host = '0. 0. 0. 0)