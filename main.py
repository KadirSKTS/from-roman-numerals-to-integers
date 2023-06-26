##################### Roman To Integer ########################
def roman_to_integer(roman):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_list = list(roman)
    integer_list = []
    for x in roman_list:
        numbers = roman_dict[f"{x}"]
        integer_list.append(numbers)

    for x in integer_list:
        x = integer_list.count(x) > 3

    if x == True:
        print('hatalı işlem yaptınız')
    else:
        result = 0
        for i in range(len(integer_list)):
            if i < len(integer_list) - 1 and integer_list[i] < integer_list[i + 1]:
                result -= integer_list[i]
            else:
                result += integer_list[i]
        print(result)

roman_to_integer('IIII')
