lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")

string = list(input("Input: "))
shift = int(input("Shift: "))
sol = []

for i in range(0, len(string)):
    if string[i].lower() in lowercase_letters:
        pos = lowercase_letters.index(string[i].lower())

        sol.append(lowercase_letters[i + shift])


print("".join(sol))
