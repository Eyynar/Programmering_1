user_input = int(input("Hva er meningen med livet?"))

if user_input == 42:
    print("Det stemmer, meningen med livet er 42!")
elif 50 > user_input > 30:
    print("Nærme, men feil.")
else:
    print("FEIL!")