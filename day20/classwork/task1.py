"""1) მოხმარებელს შემოატანინეთ რიცხვი,
შემდეგ კი დაუბეჭდეთ ეს რიცხვი დადებითია, უარყოფითი თუ ნეიტურალი ანუ ნული.
შემდეგ კომენტარებით ახსენით რა გასნხვავებაა if-სა და elif-ს შორის რატომ არ შეიძლება
ზოგერ elif-ს ნაცვლად if-ის გამოყენება"""

number= int(input("enter number: "))

if number > 0:
    print("number is possitive")

elif number < 0:
    print("number is neitral")

else:
    print("number is negative")

#if-  ნიშნავს იმ შემთხვევაში თუ
#elif- ვიყენებთ როცა რამდენიმე პირობა გვაქვს