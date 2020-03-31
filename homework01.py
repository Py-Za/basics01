
def calculate(a, b, c):
    print("\nTrybiki funkcji dają ci wartość:")
    if c:
        print(a+b)
    else:
        print(a-b)

def make_bool(a):
    if a == "y":
        return True
    elif a == "n":
        return False
    else:
        prompt = "\nMiało być y/n ty mały kurwiu, wpisz mi to jeszcze raz\n"
        return make_bool(input(prompt))

def make_float(a):
    try:
        return float(a)
    except ValueError:
        prompt = "\nMiała być liczba...\n"
        return make_float(input(prompt))

repeat = True

while repeat:
    p = make_float(input("\nDej mnie twoją pierszą liczbę:\n"))
    q = make_float(input("\nDej mnie twoją drugą liczbę:\n"))
    r = make_bool(str(input("\nCzy tszeci argument jest True? y/n\n")))
    calculate(p, q, r)
    repeat = make_bool(input("\nPowtarzamy? y/n\n"))

print("\nOK NARA LESZCZU\n")
