from sys import argv
total = 0
mapping = {'one': '1', 
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9',
           'zero': '0'
           }


for line in open(argv[1]).readlines():
    print(line)
    ddd = line
    for key in mapping:
        print(key, mapping[key])
        ddd = ddd.replace(key, mapping[key])
    print(ddd)
    num = ''
    for c in line:
        if (c.isdigit()):
            num = c
            break
    for c in line[::-1]:
        if (c.isdigit()):
            num += c
            break
    total += int(num)
print(total)