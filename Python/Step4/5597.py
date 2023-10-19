"""
백준 5597번: 과제 안 내신 분..?
"""
# Sol 1
import sys

HWList = [int(sys.stdin.readline().rstrip()) for _ in range(28)]
HWnotList = []

for i in range(1, 31):
    if HWList.__contains__(i) == 0:
        HWnotList.append(str(i))
        
print("\n".join(HWnotList))

# Sol 2
import sys

HWList = [int(sys.stdin.readline().rstrip()) for _ in range(28)]
HWnotList = []

for i in range(1, 31):
    if i not in HWList:
        HWnotList.append(str(i))
        
print("\n".join(HWnotList))

# Sol 3
import sys

HWnotList = [str(i+1) for i in range(30)]

for _ in range(28):
    HWnotList.remove(sys.stdin.readline().rstrip())
        
print("\n".join(HWnotList))