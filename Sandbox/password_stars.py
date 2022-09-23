Psw = "0"
Psw = input("What would you like to set your password as? (Min. 5 characters)")

while len(Psw) < 5:
    print("Please enter a longer password!")
    Psw = input("What would you like to set your password as? (Min. 5 characters)")

PswLen = len(Psw)
print("Your password is: ", PswLen * "*")
