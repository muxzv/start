fn = "ib_2025/not_hehe.txt.xorf7"

file = open(fn, "r")
content = file.read()

fo = open("ib_2025/r.txt", "wb")

c = 0
for e in content:
    c += 1
    n = ord(e)
    fo.write((n^0xf7).to_bytes(1))
    print(chr(n^0xf7), end='')
 
#print(c)

fo.close()