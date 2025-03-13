print ('here is the weight convertor, mister human mass')
Their_weight = float(input('Your weight please mate):'))
print('we need to ensure this was in the correct unit, what was your unit?')
unitof_weight = input(str("Your weights' unit, kg or pounds"))
if unitof_weight == "kg":
    pounds = Their_weight * 2.20462 
    print(f"{Their_weight} in {pounds:50.1f}")
elif unitof_weight == "lbs":
     kilos = Their_weight / 2.0462
     print(f'{Their_weight} kg in {pounds:.2f} lbs-ready')
else:
     print("invalid unit! please enter kg or lbs")



    

