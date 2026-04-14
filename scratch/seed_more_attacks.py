from attacks.models import Attack

more_attacks = [
    {
        "name": "SQL Injection",
        "attack_type": "other",
        "what_it_does": "Web sahypanyň maglumat bazasyna rugsat berilmedik soraglary girizmek.",
        "how_it_works": "Giriş meýdançalaryna SQL kodlaryny ýazmak.",
        "image_url": "https://images.unsplash.com/photo-1558494949-ef0109586554?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Cross-Site Scripting (XSS)",
        "attack_type": "other",
        "what_it_does": "Ulanyjynyň brauzerinde zyýanly JavaScript kodlaryny işletmek.",
        "how_it_works": "Web sahypanyň içine script goşulýar.",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Man-in-the-Middle (MITM)",
        "attack_type": "mitm",
        "what_it_does": "Aragatnaşygy gizlinlikde diňlemek.",
        "image_url": "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Brute Force Attack",
        "attack_type": "other",
        "what_it_does": "Paroly ähli kombinasiýalary barlap görmek arkaly tapmak.",
        "image_url": "https://images.unsplash.com/photo-1624969862293-b749659ccc4e?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Social Engineering",
        "attack_type": "phishing",
        "what_it_does": "Adamlaryň ynamyna girip maglumat almak.",
        "image_url": "https://images.unsplash.com/photo-1510511459019-5dee997d7db4?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Zero-Day Exploit",
        "attack_type": "other",
        "what_it_does": "Heniz belli bolmadyk gowşaklygy ulanmak.",
        "image_url": "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Keylogger Malware",
        "attack_type": "malware",
        "what_it_does": "Klawiaturada ýazylýan her bir düwmäni ýazyp almak.",
        "image_url": "https://images.unsplash.com/photo-1542831371-29b0f74f9713?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Spyware",
        "attack_type": "malware",
        "what_it_does": "Ulanyjy barada maglumat ýygnamak.",
        "image_url": "https://images.unsplash.com/photo-1563206767-5b18f218e7de?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Adware",
        "attack_type": "malware",
        "what_it_does": "Agressiw mahabatlary görkezmek.",
        "image_url": "https://images.unsplash.com/photo-1551288560-129393373708?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Rootkit",
        "attack_type": "malware",
        "what_it_does": "OS-iň çuň ýerine yerleşmek we özüni gizlemek.",
        "image_url": "https://images.unsplash.com/photo-1561736778-92e52a7769ef?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "DNS Spoofing",
        "attack_type": "other",
        "what_it_does": "Domen adyny galp IP-ä gönükdirmek.",
        "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Eavesdropping",
        "attack_type": "other",
        "what_it_does": "Tordaky trafigi gizlinlikde diňlemek.",
        "image_url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Credential Stuffing",
        "attack_type": "other",
        "what_it_does": "Öň ogurlanan parollary ulanmak.",
        "image_url": "https://images.unsplash.com/photo-1633265485768-30691e9fb51b?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Trojan Horse",
        "attack_type": "malware",
        "what_it_does": "Özüni peýdaly programma hökmünde görkezmek.",
        "image_url": "https://images.unsplash.com/photo-1603791440384-56cd371ee9a7?auto=format&fit=crop&w=400&q=80"
    },
    {
        "name": "Botnet Attack",
        "attack_type": "other",
        "what_it_does": "Müňlerçe 'zombi' kompýuterine bir wagtda buýruk bermek.",
        "image_url": "https://images.unsplash.com/photo-1551288560-129393373708?auto=format&fit=crop&w=400&q=80"
    }
]

for attack_data in more_attacks:
    Attack.objects.update_or_create(name=attack_data["name"], defaults=attack_data)

print(f"Successfully updated more attacks with images.")
