import requests
import time

# Isi variabel token dan chatId sesuai dengan data Anda
token = '6859654141:AAGOGbdAFuI5AMivwCqBj8Vps04uwWKD8yE'
chatId = '6205747776'
photoUrl = 'https://st2.depositphotos.com/4294039/9795/v/950/depositphotos_97955138-stock-illustration-icon-illustration-vector-graphic-fuck.jpg' # Ganti 'URL_FOTO' dengan URL foto yang ingin Anda kirim

# Membangun URL untuk mengirim gambar ke Telegram
apiUrl = f"https://api.telegram.org/bot{token}/sendPhoto"

# Jumlah pengiriman gambar yang diinginkan
jumlahKirim = 150

# Fungsi untuk mengirim gambar ke Telegram
def kirimGambar():
    for _ in range(jumlahKirim):
        try:
            # Mengirim permintaan HTTP POST ke API Telegram
            response = requests.post(apiUrl, data={"chat_id": chatId}, files={"photo": requests.get(photoUrl).content})
            if response.status_code == 200:
                print("Pesan berhasil dikirim:", response.json())
            else:
                print("Gagal mengirim pesan. Kode status:", response.status_code)
        except Exception as e:
            print("Terjadi kesalahan:", e)
        time.sleep(1) # Jeda waktu: 1 detik

# Memulai pengiriman gambar
kirimGambar()
