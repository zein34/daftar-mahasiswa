from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from werkzeug.utils import redirect

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'db_mahasiswa'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()

@app.route('/')
def index():
    cursor = conn.cursor()
    sql = 'select * from mahasiswa'
    cursor.execute(sql)
    hasil = cursor.fetchall()

    return render_template('index.html', data = hasil)

@app.route('/tambah', methods = ['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        _nama = request.values.get('nama')
        _nim = request.values.get('nim')
        _jurusan = request.values.get('jurusan')

        sql = "insert into mahasiswa (nama, nim, jurusan) values (%s, %s, %s)"
        data = (_nama, _nim, _jurusan)

        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()

        return redirect('/')
    else:
        return render_template('daftar_mahasiswa.html')

@app.route('/delete/<id>')
def hapus_daftar(_id):
    cursor = conn.cursor()
    sql = 'delete from mahasiswa where id = %s'
    data = (_id)
    cursor.execute(sql, data)
    conn.commit()

    return redirect('/')

@app.route('/edit/<id>')
def ubah_daftar(_id):
    cursor = conn.cursor()
    sql = 'select * from mahasiswa where id = %s'
    data = (_id)
    cursor.execute(sql, data)
    hasil = cursor.fetchall()

    return render_template('edit_daftar_mahasiswa.html', data = hasil)

@app.route('/perbarui', methods = ['POST'])
def perbarui_daftar():
    _id = request.values.get('id')
    _nama = request.values.get('nama')
    _nim = request.values.get('nim')
    _jurusan = request.values.get('jurusan')

    sql = 'update mahasiswa set nama = %s, nim = %s, jurusan = %s where id = %s'
    data = (_nama, _nim, _jurusan, _id)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return redirect('/')