import sys

current_author= None
current_count = 0
author = None

for line in sys.stdin:
    line = line.strip()

    author, count =  line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_author == author:
        current_count += count
    else:
        if current_author:
            print("{}\t{}".format(current_author, current_count))
        current_count = count
        current_author = author

if current_author == author:
    print("{}\t{}".format(current_author, current_count))

