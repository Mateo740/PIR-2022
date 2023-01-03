

# FUSING CODE
samplenode3 = [25, 30, 22, 32, 31.9, 34, 34.1, 35.1, 35,33,44] # this is a sample code for speeds, updated after each FMU
samplecons3 = [0.8, 0, 0.2, 0, 2.1, 0, 1.1, 0,2,0] # this is a sample code for consumptions, updated after each FMU
print(samplenode3)
print(samplecons3)

position_list = []

for i in range(1, len(samplenode3)):

   if abs(samplenode3[i] - samplenode3[i-1]) <= 0.11: #compare
        position_list.append(i-1)
        position_list.append(i)
        #add both positions to list for next loop
   else:
        pass


position_list_nodes = position_list
position_list_cons = []


print(position_list)


#cool code that works for everything except one case...
l = len(position_list)
for index, obj in enumerate(position_list):
    foo = index
    if index <= (l-2):
        next = samplenode3[position_list[index + 1]]
        if abs(samplenode3[obj] - next) <= 0.11:
            if samplecons3[position_list[index]] > samplecons3[position_list[index+1]]:
                samplenode3[position_list[index+1]] = samplenode3[position_list[index]]
            else:
                samplenode3[position_list[index]] = samplenode3[position_list[index+1]]

        else:
            pass
    else:
        pass



print(samplenode3)

print(samplecons3)