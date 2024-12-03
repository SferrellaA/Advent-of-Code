from sys import stdin
reports = [line.split() for line in stdin]
reports = [[int(r) for r in report] for report in reports]

def check(report):
    slope = None
    for i, r in enumerate(report):
        if i == len(report)-1:
            return (True, None)
        delta = report[i+1] - r
        if abs(delta) < 1 or abs(delta) > 3:
            return (False, i)
        if slope == None:
            slope = delta
            continue
        if (slope > 0 and delta < 0) or (slope < 0 and delta > 0):
            return (False, i)

def retry(report, i):
    new_report = report.copy()
    try:
        new_report.pop(i)
    except:
        return False
    safe, _ = check(new_report)
    if safe:
        return True
    return False

safe = 0
for report in reports:
    s, i = check(report)
    if s:
        safe += 1
        continue
    # not safe on first try
    if retry(report, i-1):
        safe += 1
        continue
    if retry(report, i):
        safe += 1
        continue
    if retry(report, i+1):
        safe += 1
    
print(safe)
