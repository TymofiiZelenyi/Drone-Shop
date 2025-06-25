from flask_login import current_user

from Project.db import DATABASE
from Project.config_page import config_page

@config_page(rule_name= 'home.html')
def render_home():
    return {}