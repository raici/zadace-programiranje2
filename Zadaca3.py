"""Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji počinje kao prvo slovo vašeg imena,
a završava kao prvo slovo prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak."""

import re

regex1 = "^n"
regex2 = "\s"
regex3 = "\d"
regex4 = "g$"


unos = input("Unesite string: ")

prvo_slovo = re.findall(regex1, unos)

if not prvo_slovo:
    print("String ne pocinje prvim slovo vašeg imena")
    
zadnje_slovo = re.findall(regex4, unos)

if not zadnje_slovo:
    print("String ne zavrsava prvim slovom vašeg prezimena")
    
broj = re.findall(regex3, unos)

if not broj:
    print("Niste unijeli broj")
    
razmak = re.findall(regex2, unos)

if not razmak:
    print("Uneseni sting ne sadrzi razmak")
    
if prvo_slovo and zadnje_slovo and broj and razmak:
    print("Uneseni string sadrzi sva trazena podudaranja")