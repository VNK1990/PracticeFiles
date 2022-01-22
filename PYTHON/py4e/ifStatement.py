try:
    grade = float(input("Enter Score between 0.0-1.0 : "))
except:
    grade = -1
    print("Wrong Inputs")
    quit()

if grade >= 0.9 :
    print("A")
elif grade >= 0.8 :
    print("B")
elif grade >= 0.7 :
    print("C")
elif grade >= 0.6 :
    print("D")
elif grade < 0.6 :
    print("F")
