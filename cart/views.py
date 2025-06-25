import flask

from Project.config_page import config_page
from shop.models import Product

@config_page(rule_name='cart.html')
def render_cart():
    # 
    cookies = flask.request.cookies.get(key= 'list_products')
    list_products = []
    # 
    if cookies:
        cookies = cookies.split('|')
        for id in cookies:
            if id != '':
                count_product = cookies.count(id)
                product : Product = Product.query.get(id)
                data_product = [product, count_product]
                if data_product not in list_products:
                    list_products.append(data_product)
    #    
    return {
        'list_products' : list_products,
    }

def delete_product_to_cart():
    if flask.request.method == 'POST':
        product_id = flask.request.form.get(key= 'delete') # 3
        response = flask.make_response(flask.redirect('/cart'))
        # 
        cookies = flask.request.cookies.get(key= 'list_products') # "|3||3||3||4||4||5||5||5|"
        cookies = cookies.replace(f'|{product_id}|', '') # "|4||4||5||5||5|"
        response.set_cookie(key= 'list_products', value= cookies)#
        
        return response