"""
skaitlis=2
while skaitlis<1000:
    skaitlis**=2
    if skaitlis>=1000:
        print(skaitlis//2)
"""
print("Pirmais mazākais skaitlis, kura kvadrāts ir lielāks par 1000 ir: ")
skaitlis=1
while skaitlis<1000:
    skaitlis+=1
    skaitlis2=skaitlis**2
    if skaitlis2>1000:
        break
print(skaitlis)