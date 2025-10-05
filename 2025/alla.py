
heads = [1,2,3]
bodies = [1,2,3]
legs = [1,2,3]

l = []

for head in heads:
    for body in bodies:
        for leg in legs:
            chelovek = (head,body,leg)
            l.append(chelovek)
            print(chelovek)