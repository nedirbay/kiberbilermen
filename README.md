# Kiberbilermen (Cyber-knowledgeable)

Kiberbilermen — kiber howpsuzlygyň esaslaryny öwrenmek we düşündirmek üçin döredilen okuw platformasydyr. Bu proýekt kiber howpsuzlyk düşünjesini ýönekeý dilde açyp bermegi we ulanyjylara amaly maglumatlary ýetirmegi maksat edinýär.

## ✨ Esasy Bölümler

Platforma aşakdaky bölümlerden ybarat:

- **🏠 Baş sahypa (Main):** Kiber howpsuzlygyň nämedigi, taryhy we häzirki döwürdäki ähmiýeti barada umumy maglumat.
- **🌐 Portlar (Ports):** Iň köp ulanylýan tor portlary (80, 443, 22 we ş.m.) we olaryň tehniki düşündirişi.
- **🌍 Protokollar (Protocols):** Internet protokollary (HTTP, DNS, FTP, TCP/IP) we olaryň işleýiş prinsipleri.
- **💣 Hüjümler (Attacks):** Phishing, DDoS, Malware ýaly kiber hüjümleriň görnüşleri we olardan goranmagyň ýollary.
- **🛡️ Gorag (Defense):** Antiviruslar, Firewall, IDS/IPS we şifrleme ýaly gorag gurallary barada maglumat.
- **📰 Täzelikler (News):** Kiber dünýäsindäki iň soňky täzelikler we waka beýanlary.
- **👤 Hasap (Accounts):** Ulanyjy hasabatyny dolandyrmak (registrasiýa we login) sistemasy.

## 🚀 Tehnologiýalar

Proýekt aşakdaky tehnologiýalar arkaly işlenip düzüldi:

- **Back-end:** Python 3.x & Django 6.0.4
- **Maglumat Hazynasy (Database):** SQLite3
- **Front-end:** Django Templates & CSS

## 🛠️ Gurnama we İşletmek

Proýekti ýerli (local) şertlerde işletmek üçin aşakdaky ädimleri berjaý ediň:

1. **Virtual gurşawy (venv) dörediň we işlediň:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # ýa-da
   .\venv\Scripts\activate  # Windows
   ```

2. **Gerekli paketleri guruň:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database migrasiýalaryny geçiriň:**
   ```bash
   python manage.py migrate
   ```

4. **Serweri işlediň:**
   ```bash
   python manage.py runserver
   ```

Serwer işlänsoň, brauzerde `http://127.0.0.1:8000/` salgysyna girip bilersiňiz.

## 👤 Admin Panel

Admin panel arkaly maglumatlary goşmak we dolandyrmak üçin:
1. `python manage.py createsuperuser` komandasy arkaly admin ulanyjysyny dörediň.
2. `http://127.0.0.1:8000/admin/` salgysyndan hasabyňyza giriň.
