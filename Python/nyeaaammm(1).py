def translate(codeword):
    translation = ""
    for letter in codeword:
        if letter in "Aa":
            if letter.isupper():
                translation = translation + "H"
            else:
                translation = translation + "h"
        elif letter in "Ee":
            if letter.isupper():
                translation = translation + "C"
            else:
                translation = translation + "c"
        elif letter in "Ii":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        elif letter in "Oo":
            if letter.isupper():
                translation = translation + "Q"
            else:
                translation = translation + "q"
        elif letter in "Uu":
            if letter.isupper():
                translation = translation + "V"
            else:
                translation = translation + "v"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter password: ")))
