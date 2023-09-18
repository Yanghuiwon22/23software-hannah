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
</head>
<body>
    <form method="get" action="/gugu">            <!-- get방식을 통해 숫자를 받을 것이고, 이 숫자를 /gugu로 보낸다.-->
        <h2>구구단 출력하기</h2>                     <!-- 큰 제목이라고 생각하면 된다.-->
        <label>단 : </label>                      <!-- 설명코드. 필수X-->           
        <input type="text" name="dan">            <!-- 입력받는 칸을 받는다. dan은 /gugu?dan=7에서 이름으로 사용되는 것이다.
                                                        gugudan 함수의 dan과 이름이 일치해야 한다.-->
        <button type="submit">출력</button>       <!-- 제출하는 버튼을 만든다. 이름은 출력으로 표시된다.-->
    </form>
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
    dan = int(request.args.get('dan'))            # dan은 주소에 들어있으므로 데이터를 받은거나 마찬가지이다.
    resp = ''                                     # 따라서 파라미터로 받는 것이 아닌 주소에서 데이터를 뽑아내야 한다.
                                                  # 그러므로 파라미터를 받지 않고 request.args.get을 통해 뽑아내는 것이다.

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