from sys import stdin
reports = [line.split() for line in stdin]
reports = [[int(r) for r in report] for report in reports]

safe = 0
for report in reports:
    slope = None
    for i, r in enumerate(report):
        # made it to the end of a report
        if i == len(report)-1:
            safe += 1
            print(report)
            break
        delta = report[i+1] - r
        if abs(delta) < 1 or abs(delta) > 3:
            break
        if slope == None:
            slope = delta
            continue
        if (slope > 0 and delta < 0) or (slope < 0 and delta > 0):
            break
print(safe)
