import pandas as pd
import os
from app.config import FILES_INPUT_DIR

def get_file_content():
    file_path = os.path.join(os.path.dirname(__file__), "input_files", "test_text.txt")
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def calculate_data_average():
    file_path = os.path.join(FILES_INPUT_DIR, 'people_data.csv')
    data = pd.read_csv(file_path)
    average_height_cm = data["Height"].mean()
    average_weight_kg = data["Weight"].mean()
    return average_height_cm, average_weight_kg
