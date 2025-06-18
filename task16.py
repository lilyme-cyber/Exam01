ticket = 100
age = int(input("Yoshingizni kiriting: "))

if age <= 6:
    ticket = ticket * 0.5  
elif age == 7:
    ticket = ticket * 0.2 
elif age < 18:
    ticket = ticket * 0.7 
elif age >= 60:
    ticket = ticket * 0.3 


print(f"Siz to'lashingiz kerak: {ticket} so'm")





