# 🛡️ Kiberbilermen — Kiber Howpsuzlyk Okuw Platformasy

Kiberbilermen — kiber howpsuzlygyň esaslaryny, häzirki zaman kiber hüjümlerini we gorag gurallaryny öwrenmek ýa-da düşündirmek üçin döredilen **premium okuw platformasydyr**. Proýekt döwrebap dizaýny, dinamiki dolandyryşy we doly türkmen dili goldawy bilen tapawutlanýar.

---

## ✨ Esasy Aýratynlyklar

### 🎨 Döwrebap UI
- **Glassmorphism & Animasiýalar**: Platforma döwrebap "glassmorphism" dizaýn stiline, ýumşak gradientlere we interaktiw animasiýalara esaslanýar.
- **Sidebar Navigasiýa**: Ulanyjylar üçin amatly sidebar arkaly ähli bölümlere çalt geçiş.
- **Responsive Dizaýn**: Ähli enjamlarda (telefon, planşet, kompýuter) birmeňzeş we ajaýyp görünüş.

### ⚙️ Dinamiki Dolandyryş Sistemasy
- **Model-Based Kategoriýalar**: Hüjümler, gorag gurallary, täzelikler we beýleki bölümler üçin kategoriýalar indi doly dinamiki (Database-driven). Admin panel arkaly islän wagtyňyz täze kategoriýa goşup ýa-da öňkileri üýtgedip bilersiňiz.
- **Admin Panel (Jazzmin)**: Django Admin paneli `django-jazzmin` arkaly döwrebaplaşdyryldy. Sidebar navigasiýasy, model belligi bolan ikonlar we amatly gözleg sistemasy bilen üpjün edildi.

### 🇹🇲 Doly Türkmen Dili Goldawy
- Platformanyň özi we dolandyryş (admin) paneli doly türkmen dilinde.
- Ähli model atlary, meýdançalar (fields) we bildirişler ulanyjy üçin düşnükli dilde sazlandy.

---

## 🚀 Tehnologiýalar

- **Core Framework**: [Django 6.0.4](https://www.djangoproject.com/) — Ygtybarly we giňeldilip bilinýän backend.
- **UI & Dizaýn**: HTML5, Vanilla CSS3 (Glassmorphism), FontAwesome Icons.
- **Admin Interface**: [Django Jazzmin](https://github.com/farridav/django-jazzmin) — Modern dolandyryş interfeýsi.
- **Database**: SQLite3 (Öwrenmek we kiçi göwrümli ulanyş üçin).

---

## 🛠️ Gurnama we İşletmek

Proýekti ýerli (local) şertlerde işletmek üçin aşakdaky ädimleri berjaý ediň:

1. **Virtual gurşawy (venv) dörediň we işlediň:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # ýa-da
   .\venv\Scripts\activate  # Windows
   ```

2. **Gerekli kitaphanalary guruň:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Maglumat bazasyny taýýarlaň:**
   ```bash
   python manage.py migrate
   ```

4. **Serweri işlediň:**
   ```bash
   python manage.py runserver
   ```

5. **Giriş**: Brauzerde [http://127.0.0.1:8000/](http://127.0.0.1:8000/) salgysyna giriň.

---

## 👤 Admin Gid (Dolandyryş üçin)

Platformanyň mazmunyny dolandyrmak gaty ýönekeý:

1. **Admin hasaby**: Ilki bilen `python manage.py createsuperuser` komandasy arkaly özüňiz üçin admin hasabyny dörediň.
2. **Giriş**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) salgysyna giriň.
3. **Kategoriýalary dolandyrmak**: Her bir bölümiň (meselem, "Kiberhüjümler") öz kategoriýa modeli bar. Täze element goşmazdan ozal münüň degişli kategoriýasynyň bardygyny ýa-da ýokdugyny barlaň.
4. **Ikonlar we Markalar**: Admin panelinde her bir model aýratyn ikonlar bilen bellenen, bu bolsa işiňizi has-da ýeňilleşdirýär.

---

## 📁 Proýektiň Gurluşy

- `main/`: Baş sahypa we umumy şablonlar.
- `attacks/`: Kiber hüjümler bölüminiň logikasy we modelleri.
- `defense/`: Gorag gurallary we metodlary bölümi.
- `news/`: Platformanyň täzelikler bölümi.
- `ports/ & protocols/`: Tor esaslary bölümleri.
- `static/ & media/`: CSS, JS we ýüklenen suratlar.

---

### 🛡️ Kiberbilermen — Bilim Howpsuzlygyň Esasydyr.
© 2026 Kiberbilermen Okuw Proýekti
