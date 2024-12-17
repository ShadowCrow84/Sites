from flask import Flask, render_template
import random 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
    
@app.route('/random_facts')
def random_facts():
    facts = ['Каждый 10 человек болеет технологичным зависимостью','Технологическая зависимость самая распрастраненная','Используйте технологии по назначению']
    return f'<p>{random.choice(facts)}</p> '

@app.route('/random_passwords')
def random_passwords():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(10):
        password += random.choice(elements)
    return f'{password}'
    
app.run(debug = True)