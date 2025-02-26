class Solution(object):
    def intToRoman(self, num):
        global roman_num
        roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        n_list = list(reversed(list(map(int, str(num)))))
        roman_num = ""
        digits = sorted(list(roman.keys()))

        def func(n):
            global roman_num
            if n_list[n] == 1:
                roman_num += roman[digits[n*2]]
            elif n_list[n] == 2:
                roman_num += (roman[digits[n*2]] * 2)
            elif n_list[n] == 3:
                roman_num += (roman[digits[(n*2)]] * 3)
            elif n_list[n] == 4:
                roman_num += (roman[digits[(n*2)+1]] + roman[digits[n*2]])   
            elif n_list[n] == 5:
                roman_num += roman[digits[(n*2)+1]]
            elif n_list[n] == 6:
                roman_num += (roman[digits[n*2]] + roman[digits[(n*2)+1]])   
            elif n_list[n] == 7:
                roman_num += (roman[digits[n*2]] * 2 + roman[digits[(n*2)+1]])  
            elif n_list[n] == 8:
                roman_num += (roman[digits[n*2]] * 3 + roman[digits[(n*2)+1]])
            elif n_list[n] == 9:
                roman_num += (roman[digits[(n*2)+2]] + roman[digits[n*2]])
        
        for n in range(len(n_list)):
            if n == 3:
                roman_num += ('M' * n_list[n])
            else:
                func(n)
            
        return ''.join(reversed(roman_num))
