def intToRoman(num):
    dct = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        300: "CCC",
        400: "CD",
        500: "D",
        600: "DC",
        700: "DCC",
        800: "DCCC",
        900: "CM",
        1000: "M",
        2000: "MM",
        3000: "MMM"
    }
    roman = ""

    num_copy = num
    len_of_num = 0


    while num_copy:
        len_of_num += 1
        num_copy //= 10

    while True:
        if len_of_num == 0:
            break

        if len_of_num == 1:
            roman += dct[num % 10]
            num //= 10
            len_of_num -= 1
        else:
            if dct.get(num):
                roman += dct[num]
                break

            if dct.get((num // pow(10, len_of_num-1)) * (pow(10, len_of_num-1))):
                roman += dct.get((num // pow(10, len_of_num-1)) * (pow(10, len_of_num-1)))
                num %= pow(10, len_of_num-1)
                len_of_num -= 1

                num_copy2 = num
                len_of_num2 = 0

                while num_copy2:
                    len_of_num2 += 1
                    num_copy2 //= 10

                if len_of_num2 != len_of_num:
                    len_of_num = len_of_num2

    print(roman)


intToRoman(2000)
