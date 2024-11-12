from flask import Flask, redirect, url_for, render_template

# Membuat Objek
app = Flask(__name__)

# Route utama
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", 'FEB'];
    return render_template ('fakultas.html', fakultas=fakultas);

@app.route('/prodi')
def prodi():
    prodi = [
        {"nama": "Informatika", "fakultas": "FIKR"},
        {"nama": "Sistem Informasi", "fakultas": "FIKR"},
        {"nama": "Akuntasi", "fakultas": "FEB"},
    ];
    return render_template ('prodi.html', prodi=prodi);

@app.route('/contact')
def contact():
    return render_template ('contact.html');

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
