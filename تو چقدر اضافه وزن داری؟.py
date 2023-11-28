n = int(input())
m = float(input())
BMI = (n/(m*m))
print('%.2f' % BMI)
if BMI <= 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal')
elif BMI >= 25 and BMI < 30:
    print('Overweight')
elif BMI >= 30:
    print('Obese')
