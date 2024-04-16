from flask import Flask, render_template, request, abort
from products import products
from flask import send_file
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to Our Online Store' and render_template('click.html')


@app.route('/products')
def product_list():
    print(products)
    return render_template('products.html', products=products)


@app.route('/')
def back_home():
    return render_template('products.html')


@app.route('/product')
def product_detail():
    product_id = request.args.get('id', type=int)
    filename = request.args.get('filename')

    # product_id
    if product_id:
        product = None
        for item in products:
            if item['id'] == product_id:
                product = item
                break
        if product:
            return render_template('product_detail.html', product=product)  # Jinja2 -e kecir.
        else:
            return 'product not found', 404

            # filename
    elif filename:
        filepath = f'uploads/{filename}'
        try:
            with open(filepath, 'r') as file:
                text = file.read()
            return text
        except FileNotFoundError:
            abort(404)
        except Exception as e:
            abort(500, f"Internal Server Error: {e}")
    else:
        return "Filename is missing", 400


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)



