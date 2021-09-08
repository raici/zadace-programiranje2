"""Napisati rekurzivnu funkciju koja kao parametar prima string, a kao rezultat taj string ispisuje sa zada."""


def rekurzija(s):
    if len(s)==0:
        return s
    else:
        return rekurzija(s[1:]) + s[0]

unos = input("Unesite string: ")

print(rekurzija(unos))