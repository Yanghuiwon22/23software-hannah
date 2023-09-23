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
    <script src="https://code.jquery.com/jquery-3.7.1.min.js"
    integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo="
    crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
    <form id="form_id" action="javascript:post_query()">
        <h2>팩토리얼 계산 </h2>
        <label>숫자 : </label>
        <input type="text" name="num">
        <button type="submit">출력</button>
    </form>
    <div id='results'></div>

<script>
function post_query() {
    $.ajax({
        type: "GET",
        url: "http://192.168.0.71:5000/fac",
        data: $("#form_id").serialize(),
        success: update_result,
        dataType: "html"
    });
}
function update_result(data) {
    $("#results").html(data);
}

</script>

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
    print(request.args.get('dan'))
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

@app.route("/fac")
def factorial():
    fac_num = int(request.args.get('num'))
    response = 1

    for i in range(1, fac_num + 1):
        response *= i

    return f"<h2>{fac_num}! = {response}</h2> " \
           """<form method="POST" action="/">
                <input type="submit" value="뒤로">"""


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)