Psw = "0"

while len(Psw) < 5:
    Psw = input("What would you like to set your password as? (Min. 5 characters)")
    if len(Psw) < 5:
        print("Please enter a longer password!")

PswLen = len(Psw)
print("Your password is: ", PswLen * "*")
