diedelesana=int(input("Ievadiet pašreizējo laiku 24h formātā ar stundas precizitati, nenorādot minūtes :)"))

if diedelesana>5<12:
    print("Labrīt!")
elif diedelesana>12<19:
    print("Labdien!")
elif diedelesana>19<20:
    print("Labvakar!")
else:
    print("Ej gulēt, labu nakti :)")