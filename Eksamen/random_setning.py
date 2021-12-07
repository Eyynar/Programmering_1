import random

subjekt = ["Ole", "Katten", "Ballen", "Kari"]
verbal = ["liker", "savnet", "mistet", "malte"]
adverbial = ["forsiktig", "raskt", "bestemt", "undrende"]

for i in range(50):
    valgt_subjekt = subjekt[random.randrange(0, len(subjekt))]
    ny_subjekt = subjekt.copy()
    ny_subjekt.remove(valgt_subjekt)
    valgt_verbal = verbal[random.randrange(0, len(verbal))]
    valgt_DOA = ny_subjekt[random.randrange(0, len(ny_subjekt))]
    valgt_adverbial = adverbial[random.randrange(0, len(adverbial))]
    print(f"{valgt_subjekt} {valgt_verbal} {valgt_DOA} {valgt_adverbial}, sa brura.")
