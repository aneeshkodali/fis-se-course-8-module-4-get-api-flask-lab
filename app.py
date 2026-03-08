from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


@app.route("/")
def home():
    return  {"message": "Welcome to the page!"}

# TODO: Implement GET /products route that returns all products or filters by category

@app.route("/products")
def get_products():
    # get category from request
    category = request.args.get('category')
    # filter by category
    if category:
        filtered = [
            p
            for p in products
            if p['category'].lower() == category.lower()
        ]
        return jsonify(filtered), 200
    # return all products otherwise
    return jsonify(products), 200


@app.route("/products/<int:id>")
def get_product_by_id(id):
    product = next(
        (
            p
            for p in products
            if p['id'] == id
        ),
        None
    )
    if product:
        return jsonify(product), 200
    return jsonify({"error": f"Product with ID {id} not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
