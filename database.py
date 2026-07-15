import psycopg2
#establishing a db connection

conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='hazeny.2008',dbname='flask_myduka')
#creating a cursor object to perform db operations

cur =conn.cursor()
def get_products():
    cur.execute('select * from products')
    products= cur.fetchall()
    return products

def insert_products(product_values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)",product_values)
    conn.commit()
product1=('pens',5,10)
product2=('flour',100,300)
#insert_products(product1)
#insert_products(product2)


#products=get_products()
#print(products)

def get_sales():
    cur.execute("select * from sales")
    sales=cur.fetchall()
    return sales

def insert_sales(sales_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",sales_values)
    conn.commit

sales1=(1,90)


#insert_sales(sales1)
#sales=get_sales()
#print(sales)


def get_stock():
    cur.execute("select * from sales")
    sales=cur.fetchall()
    return sales

def insert_stock(stock_values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",stock_values)
    conn.commit

stock1=(1,200)
stock2=(2,78)
#insert_stock(stock1)
#insert_stock(stock2)
#stocks=get_stock()
#print(stocks)

def sales_day():
    cur.execute("select date(sales.created_at) as day,sum(sales.quantity*products.selling_price) as total_sales from sales join products on sales.pid=products.id group by sales.id order by sales.id;")
    sales_per_day=cur.fetchall
    return sales_per_day

sales_per_day=sales_day()
print(sales_per_day)

def profit_products():
    cur.execute("select products.name,(products.selling_price-products.buying_price) as profit_per_product from products;")
    profit_per_product=cur.fetchall()
    return profit_per_product

profit_per_product=profit_products()
print(profit_per_product)

def profit_day():
    cur.execute("select date(sales.created_at) as day,sum(products.selling_price-products.buying_price) as profit_per_day from sales join products on sales.pid=products.id group by day order by day;")
    profit_per_day=cur.fetchall()
    return profit_per_day

profit_per_day=profit_day()
print(profit_per_day)

