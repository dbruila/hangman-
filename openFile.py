words = []
with open(r"dict\words.txt") as fo:
    for x in fo.read().split("\n"):
        x = x.replace(',.;/ ', '')
        words.append(x)
    fo.close()
