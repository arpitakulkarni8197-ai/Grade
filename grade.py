n = int(input("Enter number of subjects: "))

passed = True

for i in range(1, n + 1):
    marks = float(input(f"Enter marks for subject {i}: "))

    if marks < 40:
        passed = False
    elif marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    else:
        print("Grade: PASS")

if passed:
    print("Result: PASS")
else:
    print("Result: FAIL")
