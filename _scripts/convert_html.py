
import re
import os
import _env


def list_encoding():
    r=[]
    for i in os.listdir(os.path.split(__import__("encodings").__file__)[0]):
        name=os.path.splitext(i)[0]
        try:
            "".encode(name)
        except:
            pass
        else:
            r.append(name.replace("_","-"))
    return r

def read_html(filepath):
    try:
        with open(filepath, 'r') as f:
            html = f.read()
        return html
    except UnicodeDecodeError:
        for enc in encodings:
            print('- test read with', enc, 'for', filepath)
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    html = f.read()
                return html
            except UnicodeDecodeError:
                pass

def write_html(filepath, html):
    try:
        with open(filepath, 'w') as f:
            f.write(html)
        return True
    except UnicodeEncodeError:
        for enc in encodings:
            print('+ test write with', enc, 'for', filepath)
            try:
                with open(filepath, 'w', encoding=enc) as f:
                    f.write(html)
                return True
            except UnicodeEncodeError:
                pass

def search_transform_html(html_dir, module_name, theme_id):
    for filename in os.listdir(html_dir):
        path = os.path.join(html_dir, filename)
        if os.path.isdir(path):
            search_transform_html(path, module_name, theme_id)
        else:
            transform_html(path, module_name, theme_id)
    
def transform_html(filepath, module_name, theme_id):
    filename = os.path.basename(filepath)
    html = read_html(filepath)
    if html is None:
        print('!!! skipped during reading', filename)
        return
    html = replace_assets(html, theme_id)
    html = replace_links(html, module_name)
    done = write_html(filepath, html)
    if not done:
        print('!!! skipped during writing', filename)
        return
    print('transformed', filename)

def replace_assets(html, theme_id):
    html = html.replace('../', '')
    pattern = r'"(\S+)\.(css|js|png|jpg|svg|ico|gif)"'
    for found in re.findall(pattern, html):
        filename, extension = found        
        old = f'"{filename}.{extension}"'
        new = f'{theme_id}/{filename}.{extension}'
        new = new.replace('assets/', '')
        new = "{{ url_for('static', filename='%s') }}" % new
        html = html.replace(old, '"%s"' % new)
    return html

def replace_links(html, module_name):
    pattern = r'"(\S+)\.html"'
    for found in re.findall(pattern, html):
        old = '"%s.html"' % found
        new = "{{ url_for('temp', module='%s', page='%s') }}" 
        new = new % (module_name, found)
        html = html.replace(old, '"%s"' % new)
    return html


print('\nProgramme de conversion de fichier HTML en template Jinja2\n' + '=' * 75)
module_name = input('nom de la vue converti: ')
theme_id = input('id du theme utilise: ')

encodings = list_encoding()
html_dir = os.path.join(_env.PAGES_DIR, module_name, 'pages')
search_transform_html(html_dir, module_name, theme_id)

