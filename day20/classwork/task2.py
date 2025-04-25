"""2) მომხმარებელს შემოატანინეთ რიცხვი,
შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი,
ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია
"""
number = int(input("Enter your number: "))

if number > 0 :
    print("Number is positive")
    if number % 2 == 0:
        print("The number is also even")
    else:
        print("The number is also odd")
else:
    print("Number is negative or netural")