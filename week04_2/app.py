from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def first_page():
    return render_template('index.html')

@app.route("/aboutme")
def about_me_func():
    return render_template('about_me.html')

@app.route("/bloglist")
def blog_list_func():
    datasets = [
        {"title": '제목1', 'content': '내용1'},
        {"title": '제목2', 'content': '내용2'},
        {"title": '제목3', 'content': '내용3'}
    ]

    return render_template('blog_list.html', posts=datasets[::-1])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug='True')
