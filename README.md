
**MegaETH Auto Tx** adalah alat open-source untuk mengotomatisasi interaksi dengan kontrak pintar di jaringan MegaETH (testnet). Dibangun dengan Python, alat ini mendukung berbagai aksi seperti staking tkUSDC, minting cUSD, swapping token, dan lainnya, dengan eksekusi multi-wallet yang efisien.

**Dibuat oleh:** [https://t.me/Growndrop](https://t.me/Growndrop)  
**Lisensi:** Open-source dan gratis untuk digunakan.

---

## Fitur Utama
- **Multi-Wallet Support**: Menjalankan aksi untuk beberapa wallet secara berurutan.
- **Aksi yang Didukung**:
  - Mint cUSD
  - Send GM
  - Random Swap (WETH ke token acak)
  - tkUSDC Staking
  - Swap All Tokens to ETH
  - tkUSDC Unstaking
- **Output Profesional**: Tabel rapi dengan status transaksi dan link explorer.


## Prasyarat
Sebelum menginstal, pastikan Anda memiliki:
- **Python 3.8+**: [Unduh di sini](https://www.python.org/downloads/).
- **Git**: Untuk mengklon repositori (opsional).
- **Node RPC**: Akses ke RPC URL MegaETH testnet
- **Private Keys**: Kunci pribadi wallet yang akan digunakan.



## Instalasi
Ikuti langkah-langkah berikut untuk mengatur:

### 1. Klon Repositori (Opsional)
Jika kode tersedia di Git, klon repositori:
```bash
git clone https://github.com/nubizen/MegaETH.git
cd MegaETH
```
### 2. Buat Virtual Environment (Disarankan)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instal Dependensi
Instal paket Python yang diperlukan:
```bash
pip install web3.py python-dotenv eth-account
```

### 4. Siapkan File .env
Buat file .env di direktori utama dengan isi berikut:
```bash
RPC_URL=https://carrot.megaeth.com/rpc
PRIVATE_KEYS=private_key1,private_key2,private_key3
RPC_URL: URL endpoint RPC MegaETH testnet.
PRIVATE_KEYS: Daftar kunci pribadi wallet, dipisahkan koma.
```

### 5. Verifikasi Struktur Direktori
Pastikan struktur direktori Anda seperti ini:
nubizen-software/
├── actions.py
├── main.py
├── utils.py
├── teko/
│   ├── config.py
│   ├── stake.py
│   ├── unstake.py
│   └── abi.py
├── cap/
│   └── cap.py
├── gte/
│   ├── gte.py
│   └── abi.py
├── onchaingm/
│   └── onchaingm.py
└── .env

---