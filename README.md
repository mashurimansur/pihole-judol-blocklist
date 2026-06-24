# Pi-hole Judol (Judi Online) Blocklist

Blocklist terpadu untuk situs judi online / gambling regional Indonesia. Dibangun otomatis dengan menggabungkan & membersihkan beberapa sumber terpercaya.

## Daftar Sumber (Sources)
* [uun-aja / judol-blocklist](https://github.com/uun-aja/judol-blocklist)
* [arfshl / anti-gambling-domains](https://github.com/arfshl/anti-gambling-domains)
* [mwhd96 / BlockListJudol](https://github.com/mwhd96/BlockListJudol)

## Cara Menggunakan di Pi-hole
1. Buka Web GUI Pi-hole Anda.
2. Masuk ke menu **Adlists**.
3. Tambahkan URL mentah (raw) berikut:
   ```text
   https://raw.githubusercontent.com/mashurimansur/pihole-judol-blocklist/main/domains.txt
   ```
4. Jalankan perintah `pihole -g` di terminal Pi-hole Anda, atau buka **Tools** > **Gravity** > **Update** di Web GUI untuk memperbarui database blocklist.

## Cara Update Mandiri
Gunakan python script `update.py` yang ada di repositori ini untuk menarik update terbaru dari upstream sources dan menyaring domain unik secara otomatis:
```bash
python3 update.py
```
