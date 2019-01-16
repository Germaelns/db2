

def task1(number1, number2, number3):
    numbers = list(range(number1, number2 + 1))
    count = 0
    for num in numbers:
        if (num % number3) is 0:
            count += 1

    print('Function 1:\nResult: '+str(count)+'\n\n')
    return count


def task2(string):
    string = string.lower()
    letters = 0
    digits = 0
    for char in string:
        if char.islower():
            letters += 1
        elif char.isdigit():
            digits += 1

    print("Function 2:\nLetters: " + str(letters) + "\nDigits: " + str(digits)+'\n\n')
    return {
        'letters': letters,
        'digits': digits,
    }


def task3(mylist):
    mylist.sort(key=lambda row: (not row[0], row[1], row[2], row[3]), reverse=True)
    print('Function 3:\n')
    print(mylist)
    return mylist


if __name__=='__main__':

    task1(1,10,2)
    task2('Hello world 2018!')

    lit = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98")
    ]

    task3(lit)