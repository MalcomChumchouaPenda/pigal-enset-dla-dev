import os
import json
import markdown as md
from .constants import (
    PAGES_DIR, 
    SERVICES_DIR, 
    CORE_DIR
)

ENCODINGS = []
for i in os.listdir(os.path.split(__import__("encodings").__file__)[0]):
    name=os.path.splitext(i)[0]
    try:
        "".encode(name)
    except:
        pass
    else:
        ENCODINGS.append(name.replace("_","-"))

def get_path(filepath):
    if filepath.startswith('/pages/'):
        nexpath = os.path.normpath(filepath.replace('/pages/', ''))
        filepath = os.path.join(PAGES_DIR, nexpath)
    elif filepath.startswith('/services/'):
        nexpath = os.path.normpath(filepath.replace('/services/', ''))
        filepath = os.path.join(SERVICES_DIR, nexpath)
    elif filepath.startswith('/core/'):
        nexpath = os.path.normpath(filepath.replace('/core/', ''))
        filepath = os.path.join(CORE_DIR, nexpath)
    return filepath

def _use_encodings(filepath, encoding):
    text, valid = None, None
    try:
        with open(filepath, 'r', encoding=encoding) as f:
            text = f.read()
        valid = True
    except UnicodeDecodeError:
        pass
    return text, valid

def _search_encodings(filepath):
    for encoding in ENCODINGS:
        text, valid = _use_encodings(filepath, encoding)
        if valid:
            break
    return text, valid


def read_text(filepath, encoding='utf-8', coerce=True):
    filepath = get_path(filepath)
    text, valid = _use_encodings(filepath, encoding)
    if not valid and coerce:
        text, valid = _search_encodings(filepath)
    if not valid:
        raise RuntimeError(f'Unable to read text in {filepath}')
    return text

def read_json(filepath, encoding='utf-8', coerce=True):
    text = read_text(filepath, encoding=encoding, coerce=coerce)
    data = json.loads(text)
    return data

def read_markdown(filepath, encoding='utf-8', coerce=True):
    text = read_text(filepath, encoding=encoding, coerce=coerce)
    return md.markdown(text)

def is_file(filename):
    filepath = get_path(filename)
    return os.path.isfile(filepath)

