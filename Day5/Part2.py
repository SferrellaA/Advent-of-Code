from sys import stdin

precedents = {}
updates = []
for line in stdin:
    if "|" in line:
        pre, post = line.strip("\n").split("|")
        if post not in precedents:
            precedents[post] = []
        precedents[post].append(pre)
    if "," in line:
        updates.append(line.strip("\n").split(","))

def eval(page, preceders, update):
    for pre in preceders:
        if pre in update[update.index(page):]:
            return False
    return True

def check(update):
    for page in update:
        if page not in precedents:
            continue
        if not eval(page, precedents[page], update):
            return False
    return True

def correct(update):
    for index, page in enumerate(update):
        if page not in precedents:
            continue
        for pre in precedents[page]:
            if pre not in update:
                continue
            if update.index(pre) > index:
                while not eval(page, precedents[page], update):
                    pagei = update.index(page)
                    update[pagei], update[pagei+1] = update[pagei+1], update[pagei]
                return update

running_sum = 0
for update in updates:
    if check(update):
        continue

    while True:
        update = correct(update)
        if check(update):
            running_sum += int(update[int(len(update)/2)])
            break

print(running_sum)