import sys
import json


for line in sys.stdin:
    try:
        authors = json.loads(line)["authors"]

        for index, author in enumerate(authors, start=0):
            print("{},{}\t{}".format(author, index + 1, 1))
    except KeyError:
        continue