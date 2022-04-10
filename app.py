from flask import Flask, render_template, request
from store_repository import Storerepository


app = Flask(__name__)
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
