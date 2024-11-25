
import os
import sys


SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.dirname(SCRIPTS_DIR)
STORE_DIR = os.path.join(TEMPLATE_DIR, 'data')
THEMES_DIR = os.path.join(TEMPLATE_DIR, 'core', 'themes')
PAGES_DIR = os.path.join(TEMPLATE_DIR, 'views')

if TEMPLATE_DIR not in sys.path:
    sys.path.append(TEMPLATE_DIR)
    