from libs.percentagaise import percentagise


usrput = input("put: ")

usrputty = list(usrput)

lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("1234567890")

letters = 0
nums = 0
chars = 0

lis = []

for i in range(0, len(usrputty)):
    if usrputty[i].lower() in lowercase_letters:
        letters += 1
    elif usrputty[i].lower() in numbers:
        nums += 1
    else:
        chars += 1

lis.append(letters)
lis.append(nums)
lis.append(chars)

print(int(percentagise(lis, 0)))
print(int(percentagise(lis, 1)))
print(int(percentagise(lis, 2)))
