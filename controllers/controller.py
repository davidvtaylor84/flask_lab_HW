from flask import render_template
from app import app
import models
from models.customer_orders import orders

@app.route('/')
def bookshop():
    return "Welcome to the bookshop!"

@app.route('/orders')
def index():
    return render_template('index.html', title='Bookshop Orders', orders = orders)

@app.route('/orders/customer/<int:index>/')
def specific_orders(index):

    return render_template('order.html', title = 'Customer Orders', orders = orders[index])