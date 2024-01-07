from flask import Flask, render_template, request, redirect, url_for, flash
"""
redirect: redirecciona con url_for y el nombre de la funcion?
flash: mensajes entre vistas
"""
from flask_mysqldb import MySQL


app = Flask(__name__)

# MYSQL CONNECTION
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontact'
mysql = MySQL(app)

# SETTINGS
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contact')
    data = cursor.fetchall()
    print(data)

    return render_template('index.html', contacts=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    # return 'add_contact'
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname, phone, email)

        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO contact (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()

        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('index'))

@app.route('/get_contact/<string:id>')
def get_contact(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM contact WHERE id={0}'.format(id))
    data = cursor.fetchone()
    print(data)
    return render_template('edit_contact.html', contact=data)

@app.route('/edit_contact/<string:id>', methods=['POST'])
def edit_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute("""
        UPDATE contact
        SET fullname = %s,
            phone = %s,
            email = %s
        WHERE id = %s
        """, (fullname, phone, email, id))
        mysql.connection.commit()

        flash('Contacto actualizado.')
        return redirect(url_for('index'))


@app.route('/delete_contact/<string:id>')
def delete_contact(id):
    print(id)
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM contact WHERE id={0}'.format(id))
    mysql.connection.commit()

    flash('Contacto eliminado.')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)