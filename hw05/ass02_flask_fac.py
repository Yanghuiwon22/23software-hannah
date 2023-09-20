from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def first_page():
    return "<ul>" \
           "<li><a href='/'>첫페이지</a> " \
           "<li><a href='/hello'>Hello!</a> " \
           "<li><a href='/dan_input'>구구단</a>" \
           "<li><a href='/fac_input'>팩토리얼</a>" \
           "</ul>" \
           "<p>첫페이지 입니다!</p>"

@app.route("/hello")
def hello_world():
    return "<ul>" \
           "<li><a href='/'>첫페이지</a> " \
           "<li><a href='/hello'>Hello!</a> " \
           "<li><a href='/dan_input'>구구단</a>" \
           "<li><a href='/fac_input'>팩토리얼</a>" \
           "</ul>" \
           "<p>Hello, World!</p>"

@app.route("/dan_input")
def dan_input():
    return """<ul>
    <li><a href='/'>첫페이지</a> 
    <li><a href='/hello'>Hello!</a>
    <li><a href='/fac_input'>팩토리얼</a>
    </ul>
    <form method="POST" action="/gugu">
    <h2>구구단</h2>
        <label for="dan">단 입력:</label>
        <input type="number" name="dan" id="dan" min="1" max="9" required>
        <input type="submit" value="계산">
    </form>
    """

@app.route("/fac_input")
def fac_input():
    return """<ul>
    <li><a href='/'>첫페이지</a> 
    <li><a href='/hello'>Hello!</a>
    <li><a href='/dan_input'>구구단</a></ul>
    <form method="POST" action="/fac">
    <h2>팩토리얼</h2>
        <label for="fac_num">숫자 입력:</label>
        <input type="number" name="fac_num" id="fac_num" min="1" required>
        <input type="submit" value="계산">
    </form>
    """

@app.route("/gugu", methods=['GET', 'POST'])
def gugudan():
    dan = 1
    resp = ''

    if request.method == 'POST':
        dan = int(request.form['dan'])

    resp += '<html>\n'
    resp += '<body>\n'
    resp += '<div>\n'
    resp += f'<h2>{dan}단</h2>\n'

    for i in range(1, 10):
        resp += f'{dan} X {i:2d} = {dan * i:02d}<br>\n'
    resp += '</div>\n'
    resp += '</body>\n'
    resp += '</html>\n'

    return resp

@app.route("/fac", methods=['GET','POST'])
def factorial():
    fac_num = int(request.form['fac_num'])
    response = 1

    for i in range(1, fac_num + 1):
        response *= i

    return f"<h2>{fac_num}! = {response}</h2>" \
           f"<button href='/'>뒤로</a> "


if __name__ == "__main__":
    app.run(port=8080)
