idx = 0
ucpc = ['U', 'C', 'P', 'C']

for s in list(input().rstrip()):
  if idx < 4 and s == ucpc[idx]:
    idx += 1

if idx == 4:
  print("I love UCPC")
else:
  print("I hate UCPC")