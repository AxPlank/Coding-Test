import sys

score = { "A+" : 4.5,
         "A0" : 4.0,
         "B+" : 3.5,
         "B0" : 3.0,
         "C+" : 2.5,
         "C0" : 2.0,
         "D+" : 1.5,
         "D0" : 1.0,
         "F" : 0.0 }
demo = 0
nume = 0

for i in range(2):
    input = list(sys.stdin.readline().rstrip().split(" "))
    if input[2] != "P":
        demo += float(input[1])
        nume += float(input[1]) * score[input[2]]
        
print(nume / demo)