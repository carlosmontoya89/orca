#from flask import Flask,jsonify,render_template
from flask import Flask, request
from flask import render_template
from flask import redirect
import requests

app = Flask(__name__)

@app.route('/')
def tasks_list():
    tasks=[]
    resp = requests.get('https://api-to-do.herokuapp.com/tasks')    
    jsonresp=resp.json()
    for element in jsonresp["tasks"]:
        tasks.append(element["Content"])      
    return render_template('list.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Error'

    response = requests.post("https://api-to-do.herokuapp.com/task", json={"task":content})

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
