from attacks.models import Attack

more_attacks = [
    {
        "name": "SQL Injection",
        "attack_type": "other",
        "what_it_does": "Web sahypanyň maglumat bazasyna (database) rugsat berilmedik soraglary girizmek we maglumatlary ogurlamak.",
        "how_it_works": "Giriş meýdançalaryna (mysal üçin login sahypasy) ýörite SQL kodlaryny ýazmak arkaly bazany aldamak.",
        "goal": "Ähli ulanyjy maglumatlaryny ele salmak.",
        "example": "' OR 1=1 -- ýaly kodlar arkaly parolsyz girmek.",
        "prevention": "Prepared statements we input validation ulanmaly."
    },
    {
        "name": "Cross-Site Scripting (XSS)",
        "attack_type": "other",
        "what_it_does": "Ulanyjynyň brauzerinde zyýanly JavaScript kodlaryny işletmek.",
        "how_it_works": "Web sahypanyň içine hakyky kod däl-de, zyýanly script goşulýar.",
        "goal": "Ulanyjynyň 'cookie' (sessia) maglumatlaryny ogurlamak.",
        "prevention": "Output encoding we Content Security Policy (CSP) ulanmaly."
    },
    {
        "name": "Man-in-the-Middle (MITM)",
        "attack_type": "mitm",
        "what_it_does": "Iki tarapyň arasyndaky aragatnaşygy gizlinlikde diňlemek we maglumatlary üýtgetmek.",
        "how_it_works": "Hüjümçi torda özüni 'deläl' edip goýýar we ähli trafigi özünden geçirýär.",
        "goal": "Şifrlenmedik parollary we gizlin maglumatlary okamak.",
        "prevention": "Şifrleme (HTTPS/SSL) we VPN ulanmak."
    },
    {
        "name": "Brute Force Attack",
        "attack_type": "other",
        "what_it_does": "Islendik hasabyň parolyny mümkin bolan ähli kombinasiýalary barlap görmek arkaly tapmak.",
        "how_it_works": "Awtomatlaşdyrylan programmalar sekuntda müňlerçe paroly barlap görýärler.",
        "goal": "Hasaplara rugsat berilmedik girişi gazanmak.",
        "prevention": "Güýçli parollar, Limit login attempts we 2FA."
    },
    {
        "name": "Social Engineering",
        "attack_type": "phishing",
        "what_it_does": "Adamlaryň ynamyna girip, olardan gizlin maglumatlary almak.",
        "how_it_works": "Psihologiki usullar arkaly adamy aldamak (telefonda özüni bank işgäri diýip tanshytmak).",
        "goal": "Tehniki goragy aýlap geçip, gönüden-göni adamdan maglumat almak.",
        "prevention": "Kiber-howpsuzlyk sowatlylygyny artdyrmak."
    },
    {
        "name": "Zero-Day Exploit",
        "attack_type": "other",
        "what_it_does": "Programmada heniz belli bolmadyk gowşaklygy (vulnerability) ulanmak.",
        "how_it_works": "Hüjümçi gowşaklygy tapýar we programma üpjünçisiniň täzeleme (patch) çykarmagyndan öň ulanýar.",
        "goal": "Iň gowy goragly ulgamlara-da girmek.",
        "prevention": "Ulgamlary wagtynda täzelemek we Intrusion Detection Systems (IDS) ulanmak."
    },
    {
        "name": "Keylogger Malware",
        "attack_type": "malware",
        "what_it_does": "Klawiaturada ýazylýan her bir düwmäni (key) ýazyp alýan we hüjümçä ugradýan programma.",
        "how_it_works": "Programma fonda gizlin işleýär we ähli parollary, hatlary okaýar.",
        "goal": "Ulanyjy atlaryny we parollaryny ogurlamak.",
        "prevention": "Antivirus ulanmak we ekrandaky klawiaturadan peýdalanmak."
    },
    {
        "name": "Spyware",
        "attack_type": "malware",
        "what_it_does": "Ulanyjy barada maglumat ýygnamak we ony üçünji taraplara ugratmak üçin niýetlenen programma.",
        "how_it_works": "Brauzer geçmişini, kamerasyny we mikrofanyny barlap bilýär.",
        "goal": "Ulanyjyny yzarlamak.",
        "prevention": "Ynamdar däl çeşmelerden programma ýüklemezlik."
    },
    {
        "name": "Adware",
        "attack_type": "malware",
        "what_it_does": "Ekranda höwesjeň (agressiw) mahabatlary görkezýän zyýanly programma.",
        "how_it_works": "Brauzeriň baş sahypasyny üýtgedýär we her ýerde mahabat çykarýar.",
        "goal": "Mahabat arkaly girdeji gazanmak.",
        "prevention": "Ad-blockerler we antivirus ulanmak."
    },
    {
        "name": "Rootkit",
        "attack_type": "malware",
        "what_it_does": "Operasion ulgamynyň (OS) iň çuňňur ýerine yerleşýän we özüni gizleýän programma.",
        "how_it_works": "Antiviruslaryň özüni aldap, olardan gizlenýär we admin hukugyny alýar.",
        "goal": "Uzak wagtlap ulgamy dolandyrmak.",
        "prevention": "Secure Boot ulanmak we ýörite rootkit skanerler."
    },
    {
        "name": "DNS Spoofing",
        "attack_type": "other",
        "what_it_does": "Domen adyny galp IP-ä gönükdirmek (mysal üçin google.com ýazalyňyzda bankyň galp sahypasyna düşmek).",
        "how_it_works": "DNS kache maglumatlaryny galp maglumat bilen üýtgetmek.",
        "goal": "Ulanyjylary galp sahypalara çekmek.",
        "prevention": "DNSSEC we ygtybarly DNS serwerlerini ulanmak."
    },
    {
        "name": "Eavesdropping (Diňlemek)",
        "attack_type": "other",
        "what_it_does": "Tordaky trafigi (maglumatlary) gizlinlikde diňlemek.",
        "how_it_works": "Wi-Fi trafigini ýörite programmalar (Wireshark ýaly) bilen ele salmak.",
        "goal": "Açyk trafigi okamak.",
        "prevention": "WPA3 goragly Wi-Fi we VPN."
    },
    {
        "name": "Credential Stuffing",
        "attack_type": "other",
        "what_it_does": "Öň ogurlanan parollary ulanmak arkaly beýleki sahypalara girmäge synanyşmak.",
        "how_it_works": "Adamlaryň dürli ýerlerde birmeňzeş parol ulanýandygyny ulanýar.",
        "goal": "Köp sanly hasaplara girmek.",
        "prevention": "Her ýerde dürli parollar we 2FA."
    },
    {
        "name": "Trojan Horse",
        "attack_type": "malware",
        "what_it_does": "Özüni peýdaly programma hökmünde görkezýän, emma aslynda zyýanly funksiýasy bolan programma.",
        "how_it_works": "Oýun ýa-da peýdaly gural hökmünde ýüklenýär, emma fonda arka gapyny (backdoor) açýar.",
        "goal": "Hüjümçä uzakdan girişi üpjün etmek.",
        "prevention": "Diňe resmi dükanlardan programma ýüklemek."
    },
    {
        "name": "Botnet Attack",
        "attack_type": "other",
        "what_it_does": "Müňlerçe 'zombi' kompýuterine bir wagtda buýruk bermek.",
        "how_it_works": "Ele salnan enjamlar bir 'Command & Control' (C&C) merkezinden dolandyrylýar.",
        "goal": "Uly göwrümli DDoS hüjümlerini amala aşyrmak.",
        "prevention": "IoT enjamlarynyň parollaryny üýtgetmek we täzelemek."
    }
]

for attack_data in more_attacks:
    Attack.objects.update_or_create(name=attack_data["name"], defaults=attack_data)

print(f"Successfully added {len(more_attacks)} more attack records.")
