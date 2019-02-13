import requests
import lxml.html as lh
import pandas as pd

url='https://bugs.eclipse.org/bugs/show_activity.cgi?id=322944'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
#Check the length of the first 12 rows
#print([len(T) for T in tr_elements[:12]])
#Create empty list
col=[]
i=5
#For each row, store each first element (header) and an empty list
print(type(tr_elements[5].text_content()))
for t in tr_elements[5]:

    #i+=1
    print(t)
    name=(str(t.text_content().replace(" ","")).replace("\n",""))
    if name=="Status":
        print("YES")
        #print(tr_elements.index(t))
        #print(tr_elements[(tr_elements.index(t))+1])

    print(name)
    col.append((str(name).replace(" ","")).replace("\n",""))
if "Status" in col:
    if col[col.index("Status")+1]=="RESOLVED":
        print("Write in not Reassigned")

    else:
        print("Write in Assigned")
#print(col)