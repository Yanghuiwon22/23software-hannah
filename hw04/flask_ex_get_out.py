from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def first_page():
    return "<a href='/'>첫페이지</a> <a href='/hello'>Hello!</a> <a href='/gugu_input'>구구단</a><p>첫페이지 입니다!</p>"

@app.route("/hello")
def hello_world():
    return "<a href='/'>첫페이지</a> <a href='/hello'>Hello!</a> <a href='/gugu_input'>구구단</a><p>Hello world!</p>"

@app.route("/gugu_input")
def gugu_input():
    return "<a href='/'>첫페이지</a> <a href='/hello'>Hello!</a> <a href='/gugu_input'>구구단</a><p>숫자 입력 창</p>"

# @app.route("/gugu/<int:dan>", methods=['GET','POST'])
# def gugudan(dan):
#     resp = ''
#
#     resp += '<form method="POST">\n'
#     resp += f'<input type="number" name="dan" value="{dan}">\n'
#     resp += f'<input type="submit" value="계산">\n'
#
#     resp += '<html>\n'
#     resp += '<body>\n'
#     resp += '<div>\n'
#
#     if request.method == 'POST':
#         dan = int(request.form['dan'])
#
#     resp += f'<h2>{dan}단</h2>\n'
#
#     for i in range(1, 10):
#         resp += f'{dan} X {i:2d} = {dan * i:02d}<br>\n'
#     resp += '</div>\n'
#     resp += '</body>\n'
#     resp += '</html>\n'
#
#     return resp

if __name__=="__main__":
    app.run()