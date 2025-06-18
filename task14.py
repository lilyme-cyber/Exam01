file = input("Fayl nomini kiriting: ")

if file.endswith(".pdf"):
    print(True)
elif file.endswith(".docx"):
    print(True)
elif  file.endswith(".text"):
    print(True)
else:
    print(False)  
