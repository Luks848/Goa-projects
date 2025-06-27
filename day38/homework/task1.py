# 2) შექმენით ფუნქცია manual_index, რომელიც მიიღებს სიას და ელემენტს და დააბრუნებს ელემენტის ინდექსს სიაში. გამოიყენეთ მხოლოდ loop და if, .index მეთოდის გარეშე

def manual_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1  # თუ ელემენტი არ მოიძებნა
