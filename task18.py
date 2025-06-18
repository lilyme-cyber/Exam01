
vazn = float(input("Vazningizni kiriting : "))
boy = float(input("Bo'yingizni kiriting : "))

if vazn <= 0 or vazn > 500:
    print("Noto'g'ri vazn kiritildi. ")
elif boy <= 0 or boy < 0.5 or boy > 3.0:
    print("Noto'g'ri bo'y kiritildi.")
else:
    bmi = vazn / (boy ** 2)
    print(f"BMI: {bmi:.2f}")


    if bmi < 18.5:
        print("Kam vazn")
    elif bmi < 25:
        print("Normal vazn")
    elif bmi < 30:
        print("Ortiqcha vazn")
    else:
        print("Semizlik")
