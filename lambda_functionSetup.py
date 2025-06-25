# setup.py

import os
import configparser

# Local directory for files containing secrets 
# File names should be like config.dev.secret.properties
file_path_prefix = '/Users/personal/Documents/test'

def load_properties(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    config = configparser.ConfigParser(interpolation=None)

    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    if not file_content.startswith('['):
        file_content = "[DEFAULT]\n" + file_content

    config.read_string(file_content)
    
    return dict(config.items(('DEFAULT')))

def setup_environment():
    try:
        dev_properties = load_properties('config.' + os.getenv('env') + '.properties')
        secret_properties = load_properties(file_path_prefix + 'config.' + os.getenv('env') + '.secret.properties')
        
        for key, value in dev_properties.items():
            os.environ[key.upper()] = str(value)

        for key, value in secret_properties.items():
            os.environ[key.upper()] = str(value)

    except FileNotFoundError as e:
        print(e)
