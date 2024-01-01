h1 = ['Name','City','Mobile No']
data = [['Ruparel', 'Junagadh',7600044051],
        ['Abc', 'Rajkot',7600044052],
        ['Xyz', 'Jetpur',7600044053]]
fname = "f2.csv"
with open("f2.csv","w") as file:
    for i in h1:
        file.write(str(i)+',')
    file.write('\n')
    for j in data:
        file.write(str(j))
        file.write('\n')
