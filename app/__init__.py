from flask import Flask

app = Flask(__name__)

# Загружаем конфигурацию
app.config.from_pyfile("config.py")

# Запускаем приложение
if __name__ == "__main__":
    app.run(port=5050)
