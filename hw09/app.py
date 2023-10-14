from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def first_page():
    return render_template('index.html')

@app.route("/aboutme")
def about_me_func():
    return render_template('about_me_2.html')

@app.route("/bloglist")
def blog_list_func():
    datasets = [
        {"title": '제목1', 'content': '내용1'},
        {"title": '제목2', 'content': '내용2'},
        {"title": '제목3', 'content': '내용3'}
    ]

    return render_template('blog_list.html', posts=datasets[::-1])

@app.route("/myschedule")
def my_schedule_func():
    return render_template('my_schedule.html')

@app.route("/contact")
def contact_func():
    return render_template('contact.html')

@app.route("/homework")
def homework_func():
    return render_template('homework.html')

if __name__ == "__main__":
    app.run(debug='True')
