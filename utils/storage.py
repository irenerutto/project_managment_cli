import json
DATA_FILE = "data/data.json"
def save_data(data):
    """
    Save data to the JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    """
    Load data from the JSON file.
    """
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {"users": []}

    except json.JSONDecodeError:
        return {"users": []}       