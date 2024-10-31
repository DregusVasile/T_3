import random

def alege_cuvant():
    """Alege un cuvânt aleatoriu din lista de cuvinte."""
    cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
    return random.choice(cuvinte)

def verifica_litera(litera, cuvant_de_ghicit):
    """Verifică dacă litera se află în cuvânt."""
    if litera in cuvant_de_ghicit:
        print("Corect!")
        return True
    else:
        print("Greșit!")
        return False

def obtine_litera_valida(litere_incercate):
    """Obține o literă validă de la utilizator."""
    litera = input("Introdu o literă: ").lower()

    while len(litera) != 1 or not litera.isalpha() or litera in litere_incercate:
        if len(litera) != 1:
            print("Te rog, introdu o singură literă.")
        elif not litera.isalpha():
            print("Te rog, introdu o literă.")
        else:
            print("Ai introdus deja litera asta. Încearcă alta.")
        litera = input("Introdu o literă: ").lower()

    return litera

def afiseaza_progres(progres, incercari_ramase, litera, cuvant_de_ghicit):
    """Afișează progresul cuvântului și numărul de încercări rămase."""
    if litera in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera
    print(" ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")

def joaca_spanzuratoarea():
    """Implementează jocul Spânzurătoarea."""
    cuvant_de_ghicit = alege_cuvant()
    progres = ["_" for _ in cuvant_de_ghicit]
    incercari_ramase = 6
    litere_incercate = []

    afiseaza_progres(progres, incercari_ramase, '', cuvant_de_ghicit)

    while "_" in progres and incercari_ramase > 0:
        litera = obtine_litera_valida(litere_incercate)

        litere_incercate.append(litera)
        if not verifica_litera(litera, cuvant_de_ghicit):
            incercari_ramase -= 1

        afiseaza_progres(progres, incercari_ramase, litera, cuvant_de_ghicit)

    if "_" not in progres:
        print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
    else:
        print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")

# Pornim jocul
joaca_spanzuratoarea()
