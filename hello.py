from flask import Flask, redirect, request, url_for, render_template
import os
import time

# Membuat Objek
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

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

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']
        # tampilkan di terminal
        print(f"Nama: {nama}, Email: {email}, Pesan: {pesan}")

        # Pesan konfirmasi
        pesan_konfirmasi = f"Halo {nama}, data Anda berhasil dikirim"
        return render_template('contact.html', nama=nama, email=email, pesan=pesan, pesan_konfirmasi=pesan_konfirmasi)

    return render_template ('contact.html');

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        nisn = request.form['nisn']
        nama = request.form['nama']
        email = request.form['email']
        ttl = request.form['ttl']
        asalsekolah = request.form['asalsekolah']
        prodi = request.form['prodi']

        # Cek jika ada file yang diunggah
        foto = request.files['foto']
        if foto:
            # Mengambil timestamp saat ini untuk menambahkan ke nama file
            timestamp = str(int(time.time()))
            # Mengambil ekstensi file asli
            ext = foto.filename.split('.')[-1]

            # Menambahkan ekstensi ke nama file unik
            unique_filename = f"{timestamp}.{ext}"

            # Menyimpan file dengan nama unik
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif dengan menggunakan '/uploads/'
        else:
            foto_path = None

        # Pesan konfirmasi
        confirmation_message = f"Thank you, {nama}. Your registration has been received!"
        
        # Tampilkan halaman dengan pesan konfirmasi
        return render_template('register.html', confirmation_message=confirmation_message, nama=nama, email=email, ttl=ttl, asalsekolah=asalsekolah, prodi=prodi, foto=foto_path)

    return render_template ('register.html');

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
