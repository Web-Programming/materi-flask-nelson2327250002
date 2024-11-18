from flask import Flask, render_template, request, jsonify
import os
import time

UPLOAD_FOLDER = 'static/uploads'
#ALLOWED EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

# Tentukan folder upload untuk menyimpan file
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return 'File Upload Demo'

@app.route('/uploadfile', methods=['GET', 'POST'])
def uploadfile():
    if request.method == 'POST':
        # Ambil data dari form
        # nama = request.form['nama']
        # email = request.form['email']
        # hp = request.form['hp']
        # prodi = request.form['prodi']
        #foto = request.files['fotos']

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
            foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif
            # Response JSON jika file berhasil diunggah
            data = {
                "status": "success",
                "message": "File uploaded successfully",
            }
        else:
            # Jika tidak ada file yang diunggah
            data = {
                "status": "failed",
                "message": "No file uploaded"
            }
        return jsonify(data)
    
    # Jika metode GET, beri response dengan instruksi
    data = {
        "status": "success",
        "message": "Please upload a file."
    }
    return jsonify(data)

# Keep this as is
if __name__ == '__main__':
    app.run(debug=True)