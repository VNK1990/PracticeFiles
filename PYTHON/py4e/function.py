def computepay(h,r):
    if h > 40 :
        pay = (40 * r) + ((h - 40) * (r * 1.5))
    else:
        pay = h * r
    return pay

try :
    hrs = float(input("Enter Hours: "))
    rt = float(input("Enter Rate: "))
except :
    print("Wrong Input")

pay = computepay(hrs,rt)
print("Pay",pay)
