from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"]= "static/images/"

db = SQLAlchemy(app)
migrate = Migrate(app, db)


syms = "abcdefghijklmnopqrstuvxyz1234567890"
personal_id = "".join(random.choice(syms) for i in range(4))
actual_user = None
products = None
users = None


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   login = db.Column(db.String(100), nullable=False)
   password = db.Column(db.String(30), nullable=False)
   name = db.Column(db.String(100), nullable=False)
   age = db.Column(db.Integer, nullable=False)
   gender = db.Column(db.String(10), nullable=False)
   personal_id = db.Column(db.String(100), nullable=False)
  
class Product(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   category = db.Column(db.String(100), nullable=False)
   price = db.Column(db.Integer, nullable=False)
   currency = db.Column(db.String(100), nullable=False)
   quantity = db.Column(db.Integer, nullable=False)
   image = db.Column(db.String(1000), nullable=False)
   description = db.Column(db.String(1000), nullable=False)
   personal_id = db.Column(db.String(100), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def login():
   global personal_id, actual_user, products, users
   error = ''
   
   if request.method == 'POST':
       form_login = request.form['email']
       form_password = request.form['password']
       
       actual_user = form_login
       products = Product.query.order_by(Product.id).all()
       users = User.query.order_by(User.id).all()
      
       # Aplicar la autorización
       users_db = User.query.all()
       for user in users_db:
           if form_login == user.login and form_password == user.password:
               return redirect("/menu")
       else:
           error = 'Nombre de usuario o contraseña incorrectos'
           return render_template('login.html', error=error)
   else:
       return render_template('login.html')
  


@app.route('/reg', methods=['GET', 'POST'])
def reg():
   global personal_id
   if request.method == 'POST':
       login = request.form['email']
       password = request.form['password']
       name = request.form['name']
       age = request.form['age']
       gender = request.form['gender']
       
      
       # Hacer que los datos del usuario se registren en la base de datos
       user = User(login=login, password=password, name=name, age=age, gender=gender, personal_id = personal_id)
       db.session.add(user)
       db.session.commit()
      
       return redirect('/')
   else:   
       return render_template('register.html')



@app.route("/create1", methods=['GET', 'POST'])
def create1():
   if request.method == "POST":
      tipo = request.form["tipo"]
      
      product = Product(tipo=tipo)
      db.session.add(product)
      
      return render_template('create1.html')
   else:
      return render_template('create1.html')


@app.route("/create2", methods=['GET', 'POST'])
def create2():
   global personal_id
   if request.method == "POST":
       name = request.form["name"]
       category = request.form["category"]
       price = request.form["price"]
       currency = request.form["currency"]
       quantity = request.form['quantity']
       description = request.form["description"]
       
       archivo = request.files["file"]
       archivo.save(os.path.join(app.config['UPLOAD_FOLDER'],archivo.filename))
      
       product = Product(name=name, category=category, price=price, currency=currency, quantity=quantity, image=archivo.filename, description=description, personal_id=personal_id)
       db.session.add(product)
       db.session.commit()
             
       return redirect("/menu")
   else:
       return render_template('create2.html')



@app.route("/ter")
def terms():
   return render_template('terms.html')


@app.route("/ret")
def ret():
   return render_template('register.html')

@app.route("/productos_venta")
def compras():
   return render_template('productos.html')

@app.route("/saldo")
def saldo():
   return render_template('saldo.html')

@app.route('/menu')
def menu():
   global actual_user
   current_user = User.query.filter_by(login=actual_user).first()

   if current_user:
        user_products = Product.query.filter_by(personal_id=current_user.personal_id).all()
        return render_template('menu.html', products=user_products, user=current_user)
   else:
        return redirect('/')


@app.route("/profile")
def profile():
   return render_template('profile.html')



if __name__ == "__main__":
   app.run(debug=True)