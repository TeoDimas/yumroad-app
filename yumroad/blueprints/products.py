from flask import Blueprint, render_template, redirect, request, url_for, abort

from yumroad.models import Product, db
from yumroad.forms import ProductForm
products = Blueprint('products', __name__)

@products.route('/')
def index():
    all_products = Product.query.all()
    return render_template('products/index.html', products=all_products)

@products.route('/create', methods=['GET', 'POST'])
def create():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, description=form.description.data)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('.details', product_id=product.id))
    return render_template('products/new.html', form=form)

@products.route('/<product_id>')
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('products/details.html', product=product)

@products.route('/<product_id>/edit', methods=['GET', 'POST'])
def edit(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(obj=product)
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('.details', product_id=product.id))
    return render_template('products/edit.html', form=form, product=product)

# @products.route('/new', methods=['GET', 'POST'])
# def plain_old_form_handling():
#     if request.method == 'POST':
#         name = request.form['name']
#         description = request.form['description']

#         product = Product(name=name, description=description)
#         db.session.add(product)
#         return redirect(url_for('.details', product_id=product.id))
#     return render_template('products/new_plain_form.html')
