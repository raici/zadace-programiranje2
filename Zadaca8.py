"""Definirati dvije funkcije koje kao parametar primaju ime ali vraćaju različitu poruku dobrodošlice.
Jedna neka ispisuje “Pozdrav {ime}!”, a druga “Dobrodošao {ime}!”
Jedna od funkcija neka bude definirana lambda izrazom, a druga standardnim načinom.
Zatim definiraj treću funkciju koja kao parametar prima naziv funkcije za ispis dobrodošlice i poziva je tako
što pošalje vaše ime u nju.
Pozvati treću funkciju prosljeđujući joj neku od prve dvije definirane funkcije."""

def prva(ime):
    return "Pozdrav " + ime

unos = input("Unesite ime: ")
print(prva(unos))

druga = lambda ime: "Dobrodošao " + ime
print(druga("Nikola"))

def treca(prva):
    return prva(unos)

print(treca(prva))