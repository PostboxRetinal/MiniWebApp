from flask import Flask, render_template
from users.controllers.user_controller import user_controller
from users.controllers.product_controller import product_controller
from users.models.db import db

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Registrando el blueprint del controlador de usuarios
app.register_blueprint(user_controller)

# Registrando el blueprint del controlador de productos
app.register_blueprint(product_controller)

# Ruta para renderizar el template index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit/<string:id>')
def edit_user(id):
    print("id recibido",id)
    return render_template('edit.html', id=id)

@app.route('/edit_product/<string:id>')
def edit_product(id):
    print("product id recibido",id)
    return render_template('edit_product.html', id=id)

if __name__ == '__main__':
    app.run()

