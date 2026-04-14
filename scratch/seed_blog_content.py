import datetime
from news.models import NewsItem
from attacks.models import Attack
from defense.models import DefenseTool

# --- Seed News ---
news_items = [
    {
        "title": "Dünýäde täze 'Zero-Day' gowşaklygy tapyldy",
        "content": "Hünärmenler meşhur brauzerleriň birinde ulanyjylaryň maglumatlaryny ogurlamaga mümkinçilik berýän täze 'Zero-Day' gowşaklygyny ýüze çykardylar...",
        "published_at": datetime.date.today(),
        "category": "attack",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80"
    },
    {
        "title": "AI kömegi bilen kiber-hüjümler has çylşyrymly bolýar",
        "content": "Emeli akyl (AI) diňe bir goragda däl, eýsem hüjümçileriň elinde hem güýçli gurala öwrülýär...",
        "published_at": datetime.date.today() - datetime.timedelta(days=2),
        "category": "ai_security",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80"
    }
]

# --- Seed Attacks ---
attacks = [
    {
        "name": "Phishing (Oltarma)",
        "attack_type": "phishing",
        "what_it_does": "Ulanyjylary galp web sahypalary ýa-da emailler arkaly aldap, olaryň parollaryny we bank maglumatlaryny ogurlamak.",
        "how_it_works": "Hüjümçi ýnamdar guramanyň adyndan email iberýär...",
        "goal": "Şahsy maglumatlary, parollary we maliýe serişdelerini ogurlamak.",
        "example": "Siziň 'Apple ID' hasabyňyzda näsazlyk bar diýen email.",
        "prevention": "Emailleriň dogrulygyny barlaň, 2FA ulanmaly.",
        "image_url": "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "DDoS Hüjümi",
        "attack_type": "ddos",
        "what_it_does": "Serweri ýa-da web sahypany aşa köp soraglar bilen doldurylyp, onuň işini duruzmak.",
        "how_it_works": "Hüjümçi Botnet ulanýar...",
        "goal": "Sahypanyň elýeterliligini kesmek.",
        "example": "Dyn DNS hüjümi.",
        "prevention": "DDoS gorag ulgamlaryny (Cloudflare ýaly) ulanmaly.",
        "image_url": "https://images.unsplash.com/photo-1558494949-ef0109586554?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Ransomware (Girew-Programma)",
        "attack_type": "malware",
        "what_it_does": "Kompýuterdäki ähli faýllary şifrleýän we girew talap edýän zyýanly programma.",
        "how_it_works": "Programma faýllary gulplaýar...",
        "goal": "Maliýe peýdasyny görmek.",
        "example": "WannaCry hüjümi.",
        "prevention": "Faýllary ätiýaçlandyryň (backup).",
        "image_url": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?auto=format&fit=crop&w=800&q=80"
    }
]

# --- Seed Defense Tools ---
tools = [
     {
        "name": "Firewall (Gorag Diwary)",
        "category": "firewall",
        "why_needed": "Tor trafigini gözegçilikde saklamak we rugsat berilmedik aragatnaşygyň öňüni almak.",
        "how_it_works": "Belli bir düzgünler esasynda paketleri barlaýar.",
        "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=800&q=80"
    },
    {
        "name": "Bitdefender Antivirus",
        "category": "antivirus",
        "why_needed": "Zyýanly programmalary ýüze çykarmak we ýok etmek üçin.",
        "how_it_works": "Viruslaryň yzy we şübheli hereketler arkaly barlayar.",
        "image_url": "https://images.unsplash.com/photo-1563206767-5b18f218e7de?auto=format&fit=crop&w=800&q=80"
    }
]

# Execute Seeding
for item_data in news_items:
    NewsItem.objects.update_or_create(title=item_data["title"], defaults=item_data)

for attack_data in attacks:
    Attack.objects.update_or_create(name=attack_data["name"], defaults=attack_data)

for tool_data in tools:
    DefenseTool.objects.update_or_create(name=tool_data["name"], defaults=tool_data)

print(f"Successfully seeded News, Attacks, and Defense Tools with images.")
