# from app import app
from app.helpers import generate_user_data
from app.astronauts import get_number_of_astronauts
from app.data import calculate_data_average, get_file_content
from flask import jsonify
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/get-content/")
def get_content():
    file_content = get_file_content()
    return file_content


@app.route("/generate-users/")
def generate_users():
    num_users = 100
    users = generate_user_data(num_users)
    return jsonify(users)


@app.route("/get-astronauts/")
def get_astronauts():
    count, astronauts = get_number_of_astronauts()
    return f"Number of astronauts: {count}<br>Astronauts: {', '.join(astronauts)}"


@app.route("/calculate-average/")
def calculate_average():
    average_height_cm, average_weight_kg = calculate_data_average()
    return f"Average height: {average_height_cm} cm<br>Average weight: {average_weight_kg} kg"


if __name__ == "__main__":
    app.run(port=5050)
