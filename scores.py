#Get team names

home = input("Enter the home teams name.")
away = input("Enter the away teams name.")

#Get scores

scores = [(), (), (), ()]

print(home, "v." , away)

# scores[0] = input("Quarter 1 Lakers Score?")
# scores[1] = input("Quarter 1 Warriors Score?")
# scores[2] = input("Quarter 2 Lakers Score?")
# scores[3] = input("Quarter 2 Warriors Score?")
# scores[4] = input("Quarter 3 Lakers Score?")
# scores[5] = input("Quarter 3 Warriors Score?")
# scores[6] = input("Quarter 4 Lakers Score?")
# scores[7] = input("Quarter 4 Warriors Score?")

wtotal = scores[1 + 3 + 5 + 7]
ltotal = scores[0 + 2 + 4 + 6]

#Display scores

print()
print("Total Statistics")
print("Quarterly Lakers v Warriors")

print("1:" , scores[0] , scores[1])
print("2:" , scores[2] , scores[3])
print("3:" , scores[4] , scores[5])
print("4:" , scores[6] , scores[7])
print("Total:" , wtotal , ltotal)