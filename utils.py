import json

def load_settings():
    try:
        with open('settings.json', 'r') as set_file:
            settings = json.loads(set_file.read())
    except IOError:
        pass
    return settings