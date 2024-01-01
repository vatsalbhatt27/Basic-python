#function
s1="Ruparel Education "
print(s1)
print(s1[0])
print(s1[1:6])
print(len(s1))
print(s1.upper()) #uppercase letter
print(s1.lower()) #lowercase letter
print(s1.swapcase()) #first letter is lower and upper
print(s1.find("p")) #find index no
print(s1.index("p")) #find index no
print(s1.find("b"))
print(s1.index("p")) #write b show errer
print(s1.capitalize()) #first letter capital
print(s1.startswith("R")) #first string chr is true retun true otherwise false
print(s1.endswith("n"))
print(s1.count("a")) #count string letter position

s2="-------Ruparel Education-------"
print(s2)
print(s2.lstrip())
print(s2.rstrip())


s3="123"
print(s3.center(10,"@")) # set the number and string in center  position
print(s3.zfill(10)) # set the number and string in last position
print(s3.strip())
print(s1.replace("Education","College"))