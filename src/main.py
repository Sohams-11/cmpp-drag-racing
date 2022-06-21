Char_1="Death Wizard"
Health_1 = 1000
Shield_1 = 500
Stamina_1 = 100
DMG_1 = 300
Spirit_1 = 700


print("CHARACER STATS: " + Char_1)
print("Health: " + str(Health_1))
print("Shield: " + str(Shield_1))
print("Stamina: " + str(Stamina_1))
print("DMG_1: " + str(DMG_1))
print("Spirit_1: " + str(Spirit_1))

enemyhp = [50, 90, 80, 20, 14]
print(enemyhp[4])
sum=0
for i in range(0, 5):
    sum += enemyhp[i]
    print(sum)

