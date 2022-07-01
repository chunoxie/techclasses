def format_print(n):
    # print in decimal, octal, hex and binary

    d = str(n)
    o = oct(n)[2:]
    h = hex(n)[2:]
    b = bin(n)[2:]

    d = d.rjust(4)
    o = o.rjust(4)
    h = h.rjust(4)
    b = b.rjust(8)

    h = h.upper()

    #print(f"{str(n).rjust(4)} {o[2:].rjust(4)} {h[2:].upper().rjust(4)} {b[2:].rjust(8)}")
    return f"{d} {o} {h} {b}"

x = 20
for i in range(1, x + 1):
    print(format_print(i))