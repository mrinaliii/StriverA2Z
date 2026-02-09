
def studentGrade(m):
    if m>=90:
        print("Grade A")
    elif m>=70:
        print("Grade B")
    elif m>=50:
        print("Grade C")
    elif m>=35:
        print("Grade D")
    else:
        print("Fail")

marks = int(input("Enter marks: "))
studentGrade(marks)
