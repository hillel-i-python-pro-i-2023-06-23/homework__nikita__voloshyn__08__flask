from app.routes import home, get_content, generate_users, get_astronauts, calculate_average
from app import app


def test():
    home()
    get_content()
    get_astronauts()
    generate_users()
    calculate_average()
    return test()


# Запуск приложения
if __name__ == "__main__":
    app.run(port=5050)
