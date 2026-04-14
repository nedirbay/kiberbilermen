from protocols.models import Protocol

protocols_to_create = [
    {
        "name": "IP (Internet Protocol)",
        "category": "network",
        "purpose": "Tor enjamlarynyň arasynda maglumat paketlerini iberilýän ýerine (adressine) eltip bermek üçin hyzmat edýär.",
        "how_it_works": "IP her bir enjama üýtgeşik sanly adres (IP adres) berýär. Maglumatlar 'paket' diýlip atlandyrylýan böleklere bölünýär we her paketiň üstünde iberijiniň we alyjynyň IP adresi ýazylýar.",
        "real_world_use": "Internetde her bir tor aragatnaşygynyň özeni IP-dir (IPv4 we IPv6).",
        "security_notes": "IP-niň özi howpsuzlyk (şifreleme) üpjün etmeýär. Şonuň üçin IPsec ýaly goşmaça protokollar gerek bolup biler."
    },
    {
        "name": "TCP",
        "category": "transport",
        "purpose": "Maglumatlaryň ygtybarly, tertipli we ýalňyşsyz eltilmegini üpjün edýän baglanyşykly protokol.",
        "how_it_works": "TCP 'three-way handshake' (üç basgançakly salamlaşyk) ulanýar. Maglumat paketleri eltilende, alyjy tarap her paketi alandygyny tassyklayar (ACK). Ýitirilen paketler gaýtadan iberilýär.",
        "real_world_use": "Web (HTTP), Email (SMTP), Faýl geçiriş (FTP) ýaly ygtybarlylyk talap edýän ýerlerde ulanylýar.",
        "security_notes": "TCP SYN Flood hüjümi arkaly serweriň resurslaryny tüketmek üçin ulanylyp bilner."
    },
    {
        "name": "UDP",
        "category": "transport",
        "purpose": "Tizlige esaslanan, baglanyşyk gurmaýan ygtybarsyz maglumat geçiriş protokoly.",
        "how_it_works": "UDP paketleri tassyklaýyş garaşmazdan göni iberýär. Paketleriň tertibi ýa-da ýitmegi UDP üçin möhüm däl.",
        "real_world_use": "Wideo jaňlar, onlaýn oýunlar, DNS soraglary we media striming (broadcast).",
        "security_notes": "UDP Amplification DDoS hüjümleri üçin iň gowy guraldyr, sebäbi iberijiniň adresini galp (spoof) etmek aňsatdyr."
    },
    {
        "name": "DNS",
        "category": "application",
        "purpose": "Domen atlaryny (mysal üçin: google.com) kompýuterleriň düşünýän IP adreslerine öwürýär.",
        "how_it_works": "Hierarchy tertipde işleýär. Siziň brauzeriňiz ilki lokal DNS serwerine soraýar, ol hem öz gezeginde Root, TLD we Awtoritatiw serwerlerden jogap tapýar.",
        "real_world_use": "Internetde her gezek domen ady ýazanyňyzda işleýän iň esasy hyzmat.",
        "security_notes": "DNS Spoofing (galp jogap bermek) we Cache Poisoning arkaly ulanyjylary galp sahypalara gönükdirip bolýar.",
        "highlight_dns": True
    },
    {
        "name": "HTTP / HTTPS",
        "category": "application",
        "purpose": "Web sahypalaryny ibermek we kabul etmek üçin hyzmat edýär.",
        "how_it_works": "Client (brauzer) Request iberýär, Server bolsa Response gaýtarýar. HTTPS bolsa bu trafigi SSL/TLS arkaly şifrleýär.",
        "real_world_use": "Ähli web brauzerler we web api hyzmatlary.",
        "security_notes": "HTTP trafigini islendik adam diňläp bilýär (MITM). HTTPS ulanmak hökmanydyr."
    },
    {
        "name": "DHCP",
        "category": "application",
        "purpose": "Tor enjamlaryna awtomatik usulda IP adreslerini we beýleki sazlamalary paýlaýar.",
        "how_it_works": "DORA (Discover, Offer, Request, Acknowledge) diýen 4 basgançakly proses arkaly işleýär.",
        "real_world_use": "Öý we ofis routerlerinde her bir täze enjam çatylanda ulanylýar.",
        "security_notes": "DHCP Starvation hüjümi arkaly tordaky ähli IP adresleri tüketmek we hyzmaty duruzmak mümkin."
    }
]

for data in protocols_to_create:
    Protocol.objects.update_or_create(
        name=data["name"],
        defaults={
            "category": data["category"],
            "purpose": data["purpose"],
            "how_it_works": data["how_it_works"],
            "real_world_use": data["real_world_use"],
            "security_notes": data["security_notes"],
            "highlight_dns": data.get("highlight_dns", False)
        }
    )

print(f"Successfully created {len(protocols_to_create)} protocol records.")
