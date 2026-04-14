from ports.models import Port

ports_to_create = [
    {
        "number": 21,
        "transport": "tcp",
        "service_name": "FTP",
        "category": "well_known",
        "what_it_does": "Faýllary geçirmek üçin ulanylýan protokol.",
        "where_used": "Serwerlere faýl ýüklemek we göçürmek üçin.",
        "security_risks": "Maglumatlary şifrlemezden iberýär (açyk tekst). 'Brute-force' hüjümlerine gowşak."
    },
    {
        "number": 22,
        "transport": "tcp",
        "service_name": "SSH",
        "category": "well_known",
        "what_it_does": "Uzakdaky serwerlere howpsuz birikmek üçin kriptografik protokol.",
        "where_used": "Linux serwerlerini dolandyrmak üçin standart gapy.",
        "security_risks": "Eger 'key-based' awtorizasiýa ulanylmasa, 'dictionary' hüjümlerine sezewar bolup biler."
    },
    {
        "number": 23,
        "transport": "tcp",
        "service_name": "Telnet",
        "category": "well_known",
        "what_it_does": "Uzakdaky komandaly interfeýse birikmek üçin köne protokol.",
        "where_used": "Köne tor enjamlarynda we terminal serwerlerinde.",
        "security_risks": "Iň howply portlardan biri. Ähli maglumatlar, şol sanda parollar açyk tekstde gidýär. Sniffing (diňlemek) örän aňsat."
    },
    {
        "number": 53,
        "transport": "udp",
        "service_name": "DNS",
        "category": "well_known",
        "what_it_does": "Domen atlaryny IP adreslerine öwürýär.",
        "where_used": "Internetde her bir web sahypa girilende ulanylýar.",
        "security_risks": "DNS Cache Poisoning we Amplification DDoS hüjümlerinde giňden ulanylýar."
    },
    {
        "number": 80,
        "transport": "tcp",
        "service_name": "HTTP",
        "category": "well_known",
        "what_it_does": "Web sahypalaryny görkezmek üçin esasy protokol.",
        "where_used": "Şifrlenmedik köne web sahypalarynda.",
        "security_risks": "Maglumatlar şifrlenmedik. HTTPS ulanmak maslahat berilýär."
    },
    {
        "number": 443,
        "transport": "tcp",
        "service_name": "HTTPS",
        "category": "well_known",
        "what_it_does": "SSL/TLS arkaly şifrlenen web trafigi.",
        "where_used": "Döwrebap ähli howpsuz web sahypalarynda.",
        "security_risks": "Özi howpsuz, ýöne TLS-iň köne wersiýalary (SSLv3/TLS 1.0) ulanylsa gowşak taraplary bolup biler."
    },
    {
        "number": 3306,
        "transport": "tcp",
        "service_name": "MySQL",
        "category": "registered",
        "what_it_does": "MySQL maglumatlar binasy bilen birikmek.",
        "where_used": "Web programmalaryň maglumat gorunda.",
        "security_risks": "Uzakdan birikmäge rugsat berilse, SQL Injection we Brute-force howplary bar."
    },
    {
        "number": 3389,
        "transport": "tcp",
        "service_name": "RDP",
        "category": "registered",
        "what_it_does": "Windows kompýuterlerini uzakdan dolandyrmak.",
        "where_used": "Windows Remote Desktop programmasynda.",
        "security_risks": "BlueKeep ýaly gowşaklyklar arkaly ransomware hüjümlerinde köp ulanylýar."
    }
]

for data in ports_to_create:
    Port.objects.get_or_create(
        number=data["number"],
        transport=data["transport"],
        defaults={
            "service_name": data["service_name"],
            "category": data["category"],
            "what_it_does": data["what_it_does"],
            "where_used": data["where_used"],
            "security_risks": data["security_risks"]
        }
    )

print(f"Successfully created {len(ports_to_create)} port records.")
