from flask import Flask
from app.routes import *

app = Flask(__name__)

# Загружаем конфигурацию
app.config.from_pyfile("config.py")

# Запускаем приложение
if __name__ == "__main__":
    app.run(port=5050)
