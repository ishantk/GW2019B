# Single Value Container
popLdh = 134655
popJal = 765251
popAsr = 556613
popFzr = 876554
popMohali = 542752


popCount = popLdh + popJal + popAsr + popFzr + popMohali
print("Population of Punjab is: ",popCount)

# Multi Value Container
#             0         1       2       3       4
popPunjab = [134655, 765251, 556613, 876554, 542752]
# popCount = popPunjab[0] + popPunjab[1] +popPunjab[2] +popPunjab[3] + popPunjab[4]

popCountPunjab = 0
for num in popPunjab:
    popCountPunjab = popCountPunjab + num

print("Population of Punjab is: ",popCountPunjab)

popHaryana = [244655, 585251, 856613, 996554, 589752]

popCountHaryana = 0
for num in popHaryana:
    popCountHaryana = popCountHaryana + num

print("Population of Haryana is: ", popCountHaryana)

if popCountPunjab > popCountHaryana:
    print("Population of Punjab is More than Haryana by ",(popCountPunjab-popCountHaryana))
else:
    print("Population of Haryana is More than Punjab by ", (popCountHaryana - popCountPunjab))


# List of Lists | Multi Value Container containing Multi Value Containers
populationIndia = [
                    [134655, 765251, 556613, 876554, 542752],    # 0
                    [244655, 585251, 856613, 996554, 589752],    # 1
                    [244655, 585251, 856613, 996554],            # 2
                    [244655, 585251, 856613],                    # 3
                    [244655, 585251]                            # 4
                  ]

print("Length of popPunjab is: ",len(popPunjab))
print("Length of popHaryana is: ",len(popHaryana))
print("Length of populationIndia is: ",len(populationIndia))
print("Length of populationIndia[0] is: ",len(populationIndia[0]))
print("Length of populationIndia[1] is: ",len(populationIndia[1]))

data = []
data.append(10)
data.append(20)

# moreData = []
# moreData.append(data)

print(data)

# Find who has maximum population using loops
# Ascending Arrangement on the basis of population count (Sorting) -> Refer Google

"""
    data = [
                [0, 1, 0, 1, 1, 0]
                [1, 1, 0, 1, 1, 1]
                [0, 0, 1, 0, 0, 0]
                [1, 1, 0, 1, 1, 0]
                [1, 1, 1, 0, 0, 1]
                [1, 1, 0, 1, 1, 1]
           ]
           
    Create 2 diagonal lists
    [0, 1, 1, 1, 0, 1] -> decimal value
    [0, 1, 0, 0, 1, 1] -> decimal value
    
    Add decimal values -> Answer ?      

"""






