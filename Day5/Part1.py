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

def check(update):
    for i, page in enumerate(update):
        for post in update[i:]:
            if page not in precedents:
                continue
            if post in precedents[page]:
                return False
    return True

#for page in precedents:
#    print(f"{page} preceeded by {precedents[page]}")

running_sum = 0
for update in updates:
    if check(update):
        running_sum += int(update[int(len(update)/2)])
print(running_sum)