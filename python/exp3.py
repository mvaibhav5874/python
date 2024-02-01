name = input("Enter student name: ")
class_name = input("Enter your class: ")
section = input("Enter your section: ")
marks = float(input("Enter marks you obtained overall: "))
def performance(marks):
    if marks >= 90:
        return "Onutstanding"
    elif 80 <= marks < 90:
        return "Excellent"
    elif 70 <= marks < 80:
        return "Good"
    else:
        return "Needs Improvement"

performance = performance(marks)
print(f"\nStudent Information:")
print(f"Name: {name}")
print(f"Class: {class_name}")
print(f"Section: {section}")
print(f"Marks: {marks}")
print(f"Performance: {performance}")