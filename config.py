import os
from dotenv import load_dotenv # allows storing application configuration settings (like API keys, database connection strings, etc.) in a .env file, separate from the main codebase.
load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
users_db = os.path.join(basedir, 'users.db')
gs_admin_password = os.environ.get('GS_ADMIN_PASS')
class Config:
    # API documentation
    APIFAIRY_TITLE = 'Balloon Launch Ground Station API :D'
    APIFAIRY_VERSION = '1.0'
    APIFAIRY_UI = 'elements'

