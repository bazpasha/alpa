from flask import Flask
from flask import render_template

def get_data():
    text = open('words/form_inf_sentence.txt', encoding='utf-8')

    data = []
    for line in text:
        line = line.strip('\n')
        line = line.split('\t')
        s = [line[2], line[3], line[4]]
        data.append(s)
    return data

tasks = get_data()

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');

from flask import request, json
import random
@app.route('/task', methods=['GET'])
def task():
	cur_task = random.choice(tasks)
	return json.dumps({'task': cur_task[0], 'formal': cur_task[1], 'informal': cur_task[2]});
	
if __name__ == "__main__":
	app.run()