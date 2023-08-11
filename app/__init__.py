from flask import Flask
from run import home, get_content, generate_users, get_astronauts, calculate_average

app = Flask(__name__)

# Загрузка конфигурации
app.config.from_pyfile("config.py")

# Регистрация роутов
app.add_url_rule("/", view_func=home)
app.add_url_rule("/get-content/", view_func=get_content)
app.add_url_rule("/generate-users/", view_func=generate_users)
app.add_url_rule("/get-astronauts/", view_func=get_astronauts)
app.add_url_rule("/calculate-average/", view_func=calculate_average)
