from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL konfigürasyonları
app.config['MYSQL_HOST'] = '192.168.0.11'
app.config['MYSQL_USER'] = 'yasar'
app.config['MYSQL_PASSWORD'] = 'yasar'
app.config['MYSQL_DB'] = 'myflaskapp'  # Boşluk karakterini kaldırdım.

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Formdan gelen verileri al
    name = request.form['name']
    email = request.form['email']
    
    # Veritabanına bağlan ve verileri ekle
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cursor.close()
    
    return f'Kullanıcı {name} veritabanına eklendi.'

if __name__ == '__main__':
    app.run(debug=True)
