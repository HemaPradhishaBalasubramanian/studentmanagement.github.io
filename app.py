from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)
database.connect()

@app.route('/')
def index():
    students = database.fetch_all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    course = request.form['course']
    if name and age and course:
        database.insert(name, int(age), course)
    return redirect('/')

if __name__ == '_main_':
    app.run(debug=True)

