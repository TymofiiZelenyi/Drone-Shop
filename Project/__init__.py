from .urls import *
from .settings import project
from .loadenv import load_env
from .db import *
from .login_manager import *


from user.models import User
from shop.models import Product

project.register_blueprint(blueprint= home.home)
project.register_blueprint(blueprint= shop.shop)
project.register_blueprint(blueprint= user.user)
project.register_blueprint(blueprint= cart.cart)