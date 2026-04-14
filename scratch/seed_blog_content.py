import datetime
from news.models import NewsItem
from attacks.models import Attack
from defense.models import DefenseTool

# --- Seed News ---
news_items = [
    {
        "title": "Dünýäde täze 'Zero-Day' gowşaklygy tapyldy",
        "content": "Hünärmenler meşhur brauzerleriň birinde ulanyjylaryň maglumatlaryny ogurlamaga mümkinçilik berýän täze 'Zero-Day' gowşaklygyny ýüze çykardylar. Bu gowşaklyk arkaly hüjümçiler uzakdan kod işledip bilýärler. Ulanyjylara brauzerlerini haýal etmän täzelemek maslahat berilýär.",
        "published_at": datetime.date.today(),
        "category": "attack",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "AI kömegi bilen kiber-hüjümler has çylşyrymly bolýar",
        "content": "Emeli akyl (AI) diňe bir goragda däl, eýsem hüjümçileriň elinde hem güýçli gurala öwrülýär. Täze hasabatlara görä, AI arkaly döredilen phishing emailleri adaty emaillerden 3 esse has ynamly görünýär. Bu bolsa kiber-howpsuzlyk dünýäsinde täze kynçylyklary döredýär.",
        "published_at": datetime.date.today() - datetime.timedelta(days=2),
        "category": "ai_security",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "Bütindünýä Maglumat Goragy Güni bellenilýär",
        "content": "Her ýyl bellenilýän bu gün dünýä jemgyýetçiliginiň ünsüni şahsy maglumatlaryň goragyna çekmek maksady bilen geçirilýär. Kiberbilermen topary hökmünde biz hem siziň üçin täze gollanmalary taýýarladyk.",
        "published_at": datetime.date.today() - datetime.timedelta(days=5),
        "category": "other",
        "image_url": "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=800&q=80"
    }
]

# --- Seed Attacks ---
attacks = [
    {
        "name": "Phishing (Oltarma)",
        "attack_type": "phishing",
        "what_it_does": "Ulanyjylary galp web sahypalary ýa-da emailler arkaly aldap, olaryň parollaryny we bank maglumatlaryny ogurlamak.",
        "how_it_works": "Hüjümçi ýnamdar guramanyň (mysal üçin, bankyň) adyndan email iberýär. Linke basanyňyzda siz hakyky bank sahypasyna meňzeş galp sahypa düşýärsiňiz we maglumatlaryňyzy girizýärsiňiz.",
        "goal": "Şahsy maglumatlary, parollary we maliýe serişdelerini ogurlamak.",
        "example": "Siziň 'Apple ID' hasabyňyzda näsazlyk bar diýen email we galp icloud sahypasy.",
        "prevention": "Emailleriň dogrulygyny barlaň, 2FA (iki basgançakly anyklama) ulanmaly."
    },
    {
        "name": "DDoS Hüjümi",
        "attack_type": "ddos",
        "what_it_does": "Serweri ýa-da web sahypany aşa köp soraglar (request) bilen 'bokurdagyna çenli' dolduryp, onuň işini duruzmak.",
        "how_it_works": "Hüjümçi 'Botnet' diýlip atlandyrylýan müňlerçe ele salnan kompýuterleri ulanýar. Bu kompýuterler bir wagtyň özünde bir serwere soraýar we serwer jogap berip ýetişmän ýykylýar.",
        "goal": "Sahypanyň elýeterliligini kesmek, işewürlige zyýan ýetirmek.",
        "example": "Dünýäde meşhur bolan 2016-njy ýyldaky Dyn DNS hüjümi.",
        "prevention": "DDoS gorag ulgamlaryny (Cloudflare ýaly) ulanmaly we tor trafigini monitor etmeli."
    },
    {
        "name": "Ransomware (Girew-Programma)",
        "attack_type": "malware",
        "what_it_does": "Kompýuterdäki ähli faýllary şifrleýän we olary açmak üçin pul (girew) talap edýän zyýanly programma.",
        "how_it_works": "Programma kompýutere düşenden soň, fon rejiminde ähli resminamalary, suratlary güýçli şifr bilen gulplaýar we ekrana töleg talap edýän ýazgy çykarýar.",
        "goal": "Maliýe peýdasyny görmek we maglumatlary ýok etmek bilen haýbat atmak.",
        "example": "WannaCry hüjümi — dünýäde 200 müňden gowrak kompýutere zyýan ýetirdi.",
        "prevention": "Faýllaryňyzy elmydama ätiýaçlandyryň (backup) we şübheli programmalary açmaň."
    }
]

# --- Seed Defense Tools ---
tools = [
    {
        "name": "Firewall (Gorag Diwary)",
        "category": "firewall",
        "why_needed": "Tor trafigini gözegçilikde saklamak we rugsat berilmedik daşarky birikmeleriň öňüni almak üçin.",
        "how_it_works": "Belli bir düzgünler esasynda (rules) gelen we gidýän paketleri barlayar. Eger paket şübheli bolsa, ony bloka salýar."
    },
    {
        "name": "Bitdefender Antivirus",
        "category": "antivirus",
        "why_needed": "Zyýanly programmalary (viruslar, troyanlar) wagtynda ýüze çykarmak we ýok etmek üçin.",
        "how_it_works": "Signature-based (belli bir viruslaryň yzy) we Heuristic (şübheli hereketler) barlaglary arkaly kompýuteri gorayar."
    },
    {
        "name": "OpenSSL Encryption",
        "category": "encryption",
        "why_needed": "Interne trafigini şifrlemek we maglumatlaryň üçünji taraplar tarapyndan diňlenmeginiň öňüni almak üçin.",
        "how_it_works": "Kriptografik algoritmleri ulanmak bilen maglumatlary diňe açary bolan adam okap biler ýaly görnüşe öwürýär."
    }
]

# Execute Seeding
for item_data in news_items:
    NewsItem.objects.update_or_create(title=item_data["title"], defaults=item_data)

for attack_data in attacks:
    Attack.objects.update_or_create(name=attack_data["name"], defaults=attack_data)

for tool_data in tools:
    DefenseTool.objects.update_or_create(name=tool_data["name"], defaults=tool_data)

print(f"Successfully seeded {len(news_items)} News, {len(attacks)} Attacks, and {len(tools)} Defense Tools.")
