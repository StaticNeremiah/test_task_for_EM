import json


def save_library(library, filename='library.json'):
    """
    Saves the library to a json file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(library, file, ensure_ascii=False, indent=4)


def load_library(filename='func_style/library.json'):
    """
    Loads the library from a json file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
