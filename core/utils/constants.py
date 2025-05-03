
import os
import re
from dotenv import load_dotenv


# chemins statiques
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.dirname(_CURRENT_DIR)
ROOT_DIR = os.path.dirname(CORE_DIR)
AUTH_DIR = os.path.join(CORE_DIR, 'auth')
HOME_DIR = os.path.join(CORE_DIR, 'home')
INFO_DIR = os.path.join(CORE_DIR, 'info')
STORE_DIR = os.path.join(CORE_DIR, 'store')
THEMES_DIR = os.path.join(CORE_DIR, 'themes')
PLUGINS_DIR = os.path.join(ROOT_DIR, 'plugins')
PAGES_DIR = os.path.join(PLUGINS_DIR, 'pages')
SERVICES_DIR = os.path.join(PLUGINS_DIR, 'services')
TESTS_DIR = os.path.join(ROOT_DIR, 'tests')
CORE_MANIFEST_PATH = os.path.join(CORE_DIR, 'manifest.json')

# convention de nommage
PAGE_NAME_PATTERN = '^([a-z][a-z0-9_]*)$'
SERVICE_NAME_PATTERN = '^([a-z][a-z0-9_]*)_(v[0-9]_+[0-9]+)$'


# load variables from .env
load_dotenv()
MYSQL_USER = os.getenv('PIGAL_MYSQL_USER')
MYSQL_PWD = os.getenv('PIGAL_MYSQL_PWD')

# default database
DEFAULT_TEST_DB = "sqlite:///:memory:"
DEFAULT_DEV_DB = f"sqlite:///{os.path.join(STORE_DIR, 'default.db')}"
DEFAULT_PROD_DB = f"mysql://{MYSQL_USER}:{MYSQL_PWD}@localhost/default"

# services databases
DEV_BINDS = {}
PROD_BINDS = {}
TEST_BINDS = {}
for name in os.listdir(SERVICES_DIR):
    api_dir = os.path.join(SERVICES_DIR, name)
    if name == 'auth':
        dbname = 'auth'
    else:
        dbnames = re.findall('([a-z][a-z0-9]*)_v[0-9_]+', name)
        if len(dbnames) != 1:
            continue
        dbname = dbnames[0]
    DEV_BINDS[dbname] = f"sqlite:///{os.path.join(STORE_DIR, dbname + '.db')}"
    PROD_BINDS[dbname] = f"mysql://{MYSQL_USER}:{MYSQL_PWD}@localhost/{dbname}"
    TEST_BINDS[dbname] = f"sqlite:///{os.path.join(TESTS_DIR, 'data', dbname + '.db')}"

