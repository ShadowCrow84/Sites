from flask import Flask
import random 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f' <a href="/random_facts">Посмотреть случайный факт!</a>'
    
@app.route('/random_facts')
def random_facts():
    facts = ['Каждый 10 человек болеет технологичным зависимостью','Технологическая зависимость самая распрастраненная','Используйте технологии по назначению']
    return f'<p>{random.choice(facts)}</p> '

@app.route('/random_passwords')
def random_passwords():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    people_lenght = int(input("Введите длину пароля"))
    password = ""
for i in range(people_lenght):
    password += random.choice(elements)
    return f'<a href="/random_password">Посмотреть случайный пароль!</a>'
    
app.run(debug = True)