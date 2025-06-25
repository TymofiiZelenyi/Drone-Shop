import flask, os
from os.path import abspath, join
from flask_login import current_user

from .models import Product
from .admin import is_admin

from Project.db import DATABASE
from Project.config_page import config_page

@config_page(rule_name= 'shop.html')
def render_shop() -> dict:
    message = ''
    if flask.request.method == "POST":
        
        name_product_form = flask.request.form["name_product"]
        db_name_product = Product.query.filter_by(name_product = name_product_form).first()
        
        if db_name_product is None:
            product = Product(
                name_product = name_product_form,
                description =  flask.request.form['description'],
                price = flask.request.form['price'],
                discount = flask.request.form['discount'],
                count =flask.request.form['count']
            )
            # Збереження даних продукту у БД
            DATABASE.session.add(product)
            DATABASE.session.commit()
            # Збереження хображення продукту в директорії static/images/products
            image_form = flask.request.files['image']
            image_form.save(abspath(join(__file__, '..', 'static', 'images', 'products', f'{name_product_form}.png')))
            
            message = 'Продукт успішно створено'
        else:
            message = "Продукт з такою назвою вже існує"
            
    return {
        "message" : message,
        "list_products" : Product.query.all()
    }
    
@is_admin
def delete_product():
    id_product = int(flask.request.args.get('id'))
    model_product : Product = Product.query.get(id_product)
    if model_product is not None:
        DATABASE.session.delete(model_product)
        DATABASE.session.commit()
        os.remove(path= abspath(join(__file__, '..', 'static', 'images', 'products', f'{model_product.name_product}.png')))
        
def add_product_cart():
    # Створюємо об'єкт відповіді на Get-запит клієнта
    response = flask.make_response(flask.redirect('/shop'))
    
    id_product = flask.request.args.get(key= 'id')
    cookies = flask.request.cookies.get(key= 'list_product')
    
    if cookies is not None:
        cookies += ' ' + id_product # 1 + ' ' + 10 + ' ' + 100 + ' ' + 11 = 1 10 100 11 = [1, 10, 100, 11]
        response.set_cookie(key= 'list_product', value= cookies)
    else:
        response.set_cookie(key= 'list_product', value= id_product)
    return response
