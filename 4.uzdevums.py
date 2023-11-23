ievade=int(input("Ievadiet kādu skaitli"))
skaitlis=ievade
saraksts=[ievade]

while skaitlis>0:
    skaitlis-=1
    rez=ievade*ievade-1
    rez2=rez*skaitlis
    print(rez2)

"""
for koprez in saraksts:
    while skaitlis>0:
        rez=ievade*skaitlis
        skaitlis-=1
        rez2=rez=skaitlis
        skaitlis-=1
        print(koprez)
"""