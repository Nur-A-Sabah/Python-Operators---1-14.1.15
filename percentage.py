print("Enter Marks Obtained in 4 Subjects: ")

math = int(input("maths : "))
english = int(input("english : "))
science = int(input("science : "))
bangla = int(input("bangla : "))

total = math + english + science + bangla

print(f"Total marks obtained in 4 subjects : {total}")

perc = (total / 400) * 100

print(f"Percentage mark : {perc}%")