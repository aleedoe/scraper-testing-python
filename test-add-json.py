import json

def tambah_data_ke_json(file_json, data_baru):
    """
    Fungsi ini menambahkan data baru ke dalam file JSON yang ada.

    Args:
        file_json: Nama file JSON yang akan diubah.
        data_baru: Data baru yang akan ditambahkan dalam bentuk list of dictionaries.
    """

    try:
        with open(file_json, 'r') as f:
            try:
                data_lama = json.load(f)
            except json.JSONDecodeError:
                # Jika file kosong atau berisi data yang tidak valid, buat list kosong
                data_lama = []
    except FileNotFoundError:
        # Jika file belum ada, buat list kosong
        data_lama = []

    # Gabungkan data lama dan baru
    data_lama.extend(data_baru)

    # Tulis kembali data ke file JSON
    with open(file_json, 'w') as f:
        json.dump(data_lama, f, indent=4)

# Data yang ingin ditambahkan
value = [
    {
        "data": {
            "nama_produk": "Produk A",
            "harga": 10000,
            "deskripsi": "Deskripsi produk A"
        }
    }
]

# Nama file JSON
file_json = "detail-product.json"

# Panggil fungsi untuk menambahkan data
tambah_data_ke_json(file_json, value)

print("Data berhasil ditambahkan ke file detail-product.json")
