from csv import reader

def generirajOcjenu(bodovi):
    try:
        bodovi = int(bodovi)
        if bodovi <= 49:
            return "Nedovoljan"
        elif 50 <= bodovi <= 65:
            return "Dovoljan"
        elif 65 <= bodovi <= 80:
            return "Dobar"
        elif 80 <= bodovi <= 90:
            return "Vrlo_dobar"
        else:
            return "Odličan"
    except ValueError:
        pass
    except Exception:
        pass

with open('rezultati1.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    ntorke = list(map(tuple, csv_reader))
    sortirano = sorted(ntorke, key=lambda tup: tup[1], reverse=True)
    print(sortirano)
    ocjene = []
    for student in ntorke:
        obj = dict()
        obj["ime"] = student[0]
        obj["prezime"] = student[1]
        obj["bodovi"] = student[2]
        obj["ocjena"] = generirajOcjenu(student[2])
        ocjene.append(obj)
    print(ocjene)

rezultati1.csv.close()