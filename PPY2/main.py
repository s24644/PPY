#----------------------1

a = "Python 2023"
b = "Python 2023"
c = "Python 2023"

print("zad 1a")
print(a==b)
print("zad 1b")
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

print("zmiana trzeciej zmiennej")
c = "Java 11"
print("ponowne wykonanie a i b")
print(a==b)
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)))
print(hex(id(b)))
print(hex(id(c)))

#---------------2

liczba1 = input("podaj pierwsza liczbe")
liczba2 = input("podaj druga liczbe")
operator = input("podaj operator")

if operator == '+':
    print(int(liczba1)+int(liczba2))
elif operator == '-':
    print(int(liczba1)-int(liczba2))
elif operator == '*':
    print(int(liczba1)*int(liczba2))
elif operator == '/':
    print(int(liczba1)/int(liczba2))
