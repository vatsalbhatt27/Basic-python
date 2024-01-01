# xml file

import xml.etree.ElementTree as et
m1 = et.parse("a1.xml")
myroot = m1.getroot()
print(myroot)
print(myroot.tag)
print(myroot.tag[0:4])
print(myroot.attrib)
"""for i in myroot.findall('movie'):
    i1 = i.find('type').text
    i2 = i.find('year').text
    print(i1)
    print(i2)"""
for i in myroot.iter('description'):
    n1 = str(i.text)+'New Description'
    i.text = str(n1)
    i.set('updated','yes')
m1.write('new.xml')