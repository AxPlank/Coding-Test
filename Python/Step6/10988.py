# Sol 1
word = input()

if word == ''.join(reversed(word)):
    print(1)
else:
    print(0)
    
# Sol 2
word = input()

if word == word[::-1]:
    print(1)
else:
    print(0)