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

formal_tasks = get_data()

slang_tasks = [['arvo', 'afternoon', 'arrival'], ['attn', 'attention', 'attorney'], ['bc','because','be careful'], 
               ['biz','business', 'busyness'], ['cmt', 'comment', 'computer'], ['cu', 'see you', 'cutie'], 
               ['dju', 'did you', 'dejavu'], ['db', 'database', 'dumb'], ['exp', 'experience', 'exception'],
               ['frag', 'kill', 'fragment'], ['fab', 'fabulous', 'fable'], ['hw', 'homework', 'hallway'],
			   ['ic', 'I see', 'ice-creame'], ['ite', 'alright', 'iteration'], ['kk', 'ok', 'King Kong'],
			   ['lil', 'little', 'lilac'], ['mnm', 'Eminem', 'minimum'], ['mty', 'empty', 'mighty'],
			   ['ne', 'any', 'negative'], ['ni', 'no idea', 'night'], ['nme', 'enemy', 'not me'],
			   ['ns', 'nice', 'anus'], ['nt', 'nice try', 'note'], ['nv', 'envy', 'never'], ['nw', 'no way', 'news'],
			   ['pf', 'profile', 'pay for'], ['popo', 'police', 'postpone'], ['prd', 'period', 'product'],
			   ['pz', 'peace', 'puzzle'], ['rm', 'room', 'remain']];

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html');

from flask import request, json
import random
@app.route('/task', methods=['GET'])
def task():
	mode = request.args.get('mode')
	if mode == 'formal':
		cur_task = random.choice(formal_tasks)
	else:
		cur_task = random.choice(slang_tasks)
	return json.dumps({'task': cur_task[0], 'correct': cur_task[1], 'incorrect': cur_task[2]});
	
if __name__ == "__main__":
	app.run()