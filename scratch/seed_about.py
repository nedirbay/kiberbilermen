from about.models import ProjectInfo

ProjectInfo.objects.update_or_create(
    id=1,
    defaults={
        "goal": "Kiberbilermen — Türkmenistanda kiber-howpsuzlyk medeniýetini ösdürmek we ýaşlara bu ugurda düýpli bilim bermek maksady bilen döredilen innowasion platformadyr. Biziň esasy maksadymyz: halkyň sanly sowatlylygyny artdyrmak we milli kiber-giňişligimizi gorap biljek hünärmenleri ýetişdirmek.",
        "audience": "Ulgam dolandyryjylary, talyplar, IT hünärmenleri we öz şahsy maglumatlarynyň goragy bilen gyzyklanýan ähli raýatlar.",
        "author_name": "Nedirbaý",
        "author_bio": "Kiber-howpsuzlyk boýunça hünärmen we Full-stack programmist. Taslamanyň özeni we dizaýny boýunça hünärmen.",
        "future_plans": "Platformany doly kiber-howpsuzlyk akademiýasyna öwürmek, interaktiw kiber-labaratoriýalary (CTF) goşmak we sertifikatlaşdyryş ulgamyny girizmek."
    }
)

print("Successfully seeded Project Info.")
