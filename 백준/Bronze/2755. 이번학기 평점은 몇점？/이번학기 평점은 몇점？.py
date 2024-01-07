input = open(0).readline

scores = {'A+':4.3, 'A0':4.0, 'A-':3.7,
         'B+':3.3, 'B0':3.0, 'B-':2.7,
         'C+':2.3, 'C0':2.0, 'C-':1.7,
         'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}

num = int(input()); total = 0; cnt = 0
for n in range(num):
    a, b, c = input().split()
    total += int(b)*scores[c]; cnt += int(b)

print("%.2f" %(round(total/cnt + (0.001 if (total/cnt*100)%10 >= 5 else 0.000), 2)))