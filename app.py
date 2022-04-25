from flask import Flask, render_template
from addproduct_form import addproduct
import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)



app.config['SECRET_KEY'] = 'secretkey'
app.config['UPLOAD_FOLDER'] = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from store_repository import Storerepository
from Model import Item



storerepository = Storerepository()

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/category/<category>")
def show_products(category):
    orderedproducts = storerepository.get_products_by_category(category)
    return render_template("labeled_products.html", category_name=category, products=orderedproducts)


@app.route("/product/<productname>")
def show_product_details(productname):
    product = storerepository.get_product_by_name(productname)
    return render_template("product-details.html", product=product)

@app.route("/addproduct", methods=['GET','POST'])
def add_product():
    form = addproduct()
    if form.validate_on_submit():
        file = form.image.data
        filepath = os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(filepath ,app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        name = file.filename
        newproduct = Item(
            name = form.name.data,
            quantity = form.quantity.data,
            price = form.price.data,
            category = form.category.data,
            description = form.description.data,
            filename = name
        )
        db.session.add(newproduct)
        db.session.commit()
        return ('Product Added Successfully!')

    return render_template("addproduct.html", form=form)



