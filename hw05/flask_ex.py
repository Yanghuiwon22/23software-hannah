from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def first_page():
    return """<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script scr = ""https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script> 
</head>

<body>
    <form method="get" action="/gugu">
        <h2>구구단 출력하기</h2>
        <label>단 : </label>
        <input type="text" name="dan">
        <button type="submit">출력</button>
    </form>
    
    <!-- 서버에서 받은 결과를 출력하는 역할 -->
    <div id="results"></div>           
    
    

</body>
</html>"""

@app.route("/hello")
def hello_world():
    return "<a href='/'>첫페이지</a> <a href='/hello'>Hello!</a> <a href='/gugu/<dan>'>구구단</a><p>Hello world!</p>"

# 지난주 /gugu/7
# def gugudan(dan):
#    dan = int(dan)

# 이번주 /gugu?dan=7
@app.route("/gugu")
def gugudan():
    dan = int(request.args.get('dan'))
    resp = ''

    resp += '<html>\n'
    resp += '<body>\n'
    resp += f'<h2>{dan}단</h2>\n'
    resp += '<div>\n'
    for i in range(1, 10):
        resp += f'{dan} X {i:2d} = {dan * i:02d}<br>\n'
    resp += '</div>\n'
    resp += '</body>\n'
    resp += '</html>\n'

    return resp

if __name__=="__main__":
    app.run()