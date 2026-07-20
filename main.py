from flask import Flask,render_template
from database import get_products,get_sales,get_stock

app = Flask(__name__)

@app.route('/')
def home():
    x=5
    name="hazeny"
    numbers=[1,2,3,4,5,6,7,8,9,10]
    for i in numbers:
        if i%2==0:
            print(i)
    return render_template('index.html',y=x,a=name, numbers=numbers)

@app.route("/products")
def products():
    products_data=get_products()
    return render_template('products.html',products_data=products_data)

@app.route("/stock")
def stock():
    stock_data=get_stock()
    return render_template('stock.html',stock_data=stock_data)

@app.route("/sales")
def sales():
    sales_data=get_sales()
    return render_template('sales.html',sales_data=sales_data)

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/login")
def login():
    return render_template('login.html')

app.run(debug=True)