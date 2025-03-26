from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "description": "A powerful laptop", "price": 999},
    {"id": 2, "name": "Headphones", "description": "Noise-cancelling headphones", "price": 199}
]

users = {}
logged_in_user = None

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_in_user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            logged_in_user = username
            return redirect(url_for('index'))
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
