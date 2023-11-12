S=input()
aList=list(S)
A=0
for i in range(len(aList)):
  b=aList[i]
  if b=='A' or b=='B' or b=='C':
    B=3
  elif b=='D' or b=='E' or b=='F':
    B=4
  elif b=='G' or b=='H' or b=='I':
    B=5
  elif b=='J' or b=='K' or b=='L':
    B=6
  elif b=='M' or b=='N' or b=='O':
    B=7
  elif b=='P' or b=='Q' or b=='R' or b=="S":
    B=8
  elif b=='T' or b=='U' or b=='V':
    B=9
  elif b=='W' or b=='X' or b=='Y' or b=='Z':
    B=10
  A+=B
print(A)