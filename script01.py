
def calculate(a, b, c):
    print("\nTrybiki funkcji dają ci wartość:")
    if c == True:
        print(a+b)
    elif c == False:
        print(a-b)
    else:
        print("\nCoś się wyjebało???????\n")

def make_bool(a):
    if a == "y":
        return True
    elif a == "n":
        return False
    else:
        a = str(input("\nMiało być y/n ty mały kurwiu, wpisz mi to jeszcze raz\n"))
        return make_bool(a)

def make_float(a):
    try:
        return float(a)
    except ValueError:
        b = input("\nMiała być liczba...\n")
        return make_float(b)

repeat = True

while repeat:
    p = input("\nDej mnie twoją pierszą liczbę:\n")
    p = make_float(p)
    q = input("\nDej mnie twoją drugą liczbę:\n")
    q = make_float(q)
    r = str(input("\nCzy tszeci argument jest True? y/n\n"))
    r = make_bool(r)
    calculate(p, q, r)
    repeat = input("\nPowtarzamy? y/n\n")
    repeat = make_bool(repeat)

print("\nOK NARA LESZCZU\n")

