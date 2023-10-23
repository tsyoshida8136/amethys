from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# タスクリストの初期化
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_task():
    task = request.form.get('task')
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()