meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

# Retrieve all elements in the list
print(meniu[:])
# 1. Comenzi
print("## Comenzi")
while studenti and comenzi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    tava = tavi.pop()
    istoric_comenzi.append(comanda)
    print(f"{student} a comandat {comanda}.")

# 2. Inventar
print("\n## Inventar")
comanda_count = {}
for comanda in istoric_comenzi:
    if comanda in comanda_count:
        comanda_count[comanda] += 1
    else:
        comanda_count[comanda] = 1

print(f"S-au comandat {comanda_count['guias']} guias, {comanda_count['ceafa']} ceafa, {comanda_count['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")

for produs, pret in preturi:
    if produs == "ceafa":
        print(f"Mai este ceafa: {meniu.count(produs) > 0}.")
    if produs == "papanasi":
        print(f"Mai sunt papanasi: {meniu.count(produs) > 0}.")
    if produs == "guias":
        print(f"Mai sunt guias: {meniu.count(produs) > 0}.")

# 3. Finanțe
print("\n## Finanțe")
total_incasari = 0
for comanda in istoric_comenzi:
    for produs, pret in preturi:
        if comanda == produs:
            total_incasari += pret

print(f"Cantina a încasat: {total_incasari} lei.")
print(f"Produse care costă cel mult 7 lei: {[(produs, pret) for produs, pret in preturi if pret <= 7]}")
