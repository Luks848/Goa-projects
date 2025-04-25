"""შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს
(4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად,
საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა
"""
pincode= (input("enter pincode: "))

counter=0
while pincode !="1234":
    pincode= (input("enter pincode: "))
    counter+=1
print("pincode is right")
print(counter)

