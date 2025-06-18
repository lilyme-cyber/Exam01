grade = int(input("Balingizni kiriting: "))

if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
elif grade >= 0:
    print("F")
else:
    print("Noto‘g‘ri baho kiritildi!")
