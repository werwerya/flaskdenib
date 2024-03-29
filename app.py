
import os
from urllib.parse import urlparse
from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


urld = 'mysql://yzpsacwal98r867h:mf5cbifkgu22deyu@fojvtycq53b2f2kx.chr7pe7iynqr.eu-west-1.rds.amazonaws.com:3306/vazm5zzs3gf78nf8'
db_url = urlparse(urld)

# MySQL konfigürasyonları
app.config['MYSQL_HOST'] = db_url.hostname
app.config['MYSQL_USER'] = db_url.username
app.config['MYSQL_PASSWORD'] = db_url.password
app.config['MYSQL_DB'] = db_url.path[1:]

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
