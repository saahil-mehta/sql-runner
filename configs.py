# configs.py
import ast

def load_configurations(file_path):
    with open(file_path, 'r') as file:
        # Reading the contents of the file
        config_data = file.read()
        # Safely evaluating the string as a dictionary
        config_dict = ast.literal_eval(config_data)

    return config_dict

# Loading the configurations
configurations = load_configurations('config.txt')
