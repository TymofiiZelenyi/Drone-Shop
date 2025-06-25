from Project.db import DATABASE
# модель Product створює таблицю в БД з назвою product
class Product(DATABASE.Model):
    
    id= DATABASE.Column(DATABASE.Integer, primary_key= True)
    
    name_product = DATABASE.Column(DATABASE.String(50), default= 'product')
    description = DATABASE.Column(DATABASE.String(255), default= 'Your description')
    price = DATABASE.Column(DATABASE.Integer, default= 0)
    discount = DATABASE.Column(DATABASE.Integer, default= 0)
    count = DATABASE.Column(DATABASE.Integer, default= 0)
    
    