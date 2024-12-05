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

'''
def check(update):
    for i, page in enumerate(update):
        for post in update[i:]:
            if page not in precedents:
                continue
            if post in precedents[page]:
                return False
    return True
'''

def check(update):
    for page in update:
        if page not in precedents:
            continue
        if not eval(page, precedents[page], update):
            return False
    return True

def correct(update):
    for index, page in enumerate(update):
        #if index == 0:
        #    continue
        if page not in precedents:
            continue
        for pre in precedents[page]:
            if pre not in update:
                continue
            #print(update.index(pre), pre, index, page)
            if update.index(pre) > index:
                while not eval(page, precedents[page], update):
                    #print(f"need to update {index}:{page}")
                    pagei = update.index(page)
                    update[pagei], update[pagei+1] = update[pagei+1], update[pagei]
                    #print(update)
                return update

for page in precedents:
    print(f"{page} preceeded by {precedents[page]}")

running_sum = 0
for update in updates:
    if not check(update):
        #running_sum += int(update[int(len(update)/2)])
        print(update)
        while not check(update):
            #print()
            #print(update)
            update = correct(update)
            #print(update)
        print(update)
        print()
        running_sum += int(update[int(len(update)/2)])


print(running_sum)