"""2) შექმენით სია რომელშიც ჩამოწერთ ისტორული ეპოქები, უნდა გქონდეთ მინიმუმ 5 ეპოქა.უარყოფითი ინდექსების საშვალებით გამოიტანეთ indexing და slicing მეთოდის საშვალებით ელემენტები

ბოლო სამი ელემენტი
ბოლო ელემენტი
მეორე ელემენტიდან ყველაფერი
მესამე ელემენტამდე ყველაა ეპოქა
"""

epoqebi = ["უძველესი ეპოქა", "ანტიკური ეპოქა", "შუა საუკუნეები", "განმანათლებლობის ეპოქა", "თანამედროვე ეპოქა"]
last_three = epoqebi[-3:]
print(last_three)

bolo_erti = epoqebi[-1]
print(bolo_erti)

meore_dan_yvela = epoqebi[1:]
print(meore_dan_yvela)

mesame_mde_yvela = epoqebi[:2]
print(mesame_mde_yvela)
