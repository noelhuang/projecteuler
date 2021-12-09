hundreds = ["onehundredand", "twohundredand", "threehundredand", "fourhundredand", "fivehundredand", "sixhundredand",
            "sevenhundredand", "eighthundredand", "ninehundredand"]

hundredswhole = [hundreds[i].replace("and", "") for i in range(0, len(hundreds))]

tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

specialtens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


singles = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers = [i for i in range(1, 1000)]
print(numbers)

lst29 = [2, 3, 4, 5, 6, 7, 8, 9]

lst10 = [0, 2, 3, 4, 5, 6, 7, 8, 9]

letterlist = []

def check(lst, a):
    for i in range(0, len(lst)):
        if a == lst[i]:
            return True
    return False





for number in numbers:
    if len(str(number)) == 1:
        word = singles[int(number)-1]
        letterlist.append(word)
    if len(str(number)) == 2:

        # special tens
        if 10 <= int(number) <= 19:
            word = specialtens[int(str(number)[1])]
            letterlist.append(word)

        # tens
        if int(number) > 19:
            word = tens[int(str(number)[0])-1]
            if int(str(number)[1]) == 0:
                letterlist.append(word)
        # add singles
        if int(number) > 19 and int(str(number)[1]) != 0:
            word = word + singles[int(str(number)[1]) - 1]
            letterlist.append(word)
    if len(str(number)) == 3:
        number = str(number)
        word = hundreds[int(number[0]) - 1]
        word = str(word)

        # tens with singles
        if int(number[1]) != 0 and int(number[1]) != 1:
            word = word + tens[int(number[1]) - 1]

        # singles
        if int(number[2]) != 0 and int(number[1]) != 1:
            word = word + singles[int(number[2]) - 1]

        # whole hundreds
        if int(number[1]) == 0 and int(number[2]) == 0:
            word = hundredswhole[int(number[0])-1]

        # special tens
        if int(number[1]) == 1:
            word = word + specialtens[int(number[2])]

        letterlist.append(word)

letterlist.append("onethousand")


length = 0

for i in letterlist:
    length = length + len(i)

print(length)