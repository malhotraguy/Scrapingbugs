import requests
import lxml.html as lh
from fake_useragent import UserAgent
ua = UserAgent()
hdr = {'User-Agent':str(ua.chrome)}
import pandas as pd
import openpyxl
from Writing import new_xlsx ,updating_to_xlsx
new_xlsx("Severity.xlsx")
severity_row=2
new_xlsx("Version.xlsx")
version_row=2
new_xlsx("Status.xlsx")
status_row=2
new_xlsx("Product.xlsx")
product_row=2
new_xlsx("Os.xlsx")
os_row=2
new_xlsx("Priority.xlsx")
priority_row=2
new_xlsx("Component.xlsx")
component_row=2


for BugId in range(214000,214020):
    #print(BugId)
    url='https://bugs.eclipse.org/bugs/show_activity.cgi?id='+str(BugId)
    #Create a handle, page, to handle the contents of the website
    page = requests.get(url,headers=hdr)
    #Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    #Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//tr')
    #Check the length of the first 12 rows
    #print([len(T) for T in tr_elements[:12]])
    #Create empty list
    col=[]

    #For each row, store each first element (header) and an empty list
    #print(type(tr_elements[5].text_content()))
    for j in range(1,len(tr_elements)):
        for t in tr_elements[j]:

            #i+=1
            #print(t)
            name=(str(t.text_content().replace(" ","")).replace("\n",""))

            #print(name,type(name),name.isalnum())
            col.append(((str(name).lower()).replace(" ","")).replace("\n",""))
        #print(col)

        if "status" in col:
            if col[col.index("status")+1].lower()=="resolved":
                if col[col.index("status")+2] == "reopen":

                    print("Write in status Reassigned",BugId)
                    updating_to_xlsx("Status.xlsx",status_row,1,BugId)
                    status_row +=1
                else:

                    print("Write in status NotReassigned(!reopen)",BugId)
                    updating_to_xlsx("Status.xlsx", status_row, 2, BugId)
                    status_row += 1
            else:
                print("Write in status NotReassigned(!resolved)",BugId)
                updating_to_xlsx("Status.xlsx", status_row, 2, BugId)
                status_row += 1
        elif "severity" in col:
            if (col[col.index("severity")+1].isalnum()):
                print("Write in severity Reassigned",BugId)
                updating_to_xlsx("Severity.xlsx",severity_row,1,BugId)
                severity_row +=1
            else:
                print("Write in severity NotReassigned",BugId)
                updating_to_xlsx("Severity.xlsx", severity_row, 2, BugId)
                severity_row += 1

        elif "version" in col:
            if (col[col.index("version") + 1].isalnum()):
                print("Write in version Reassigned",BugId)
                updating_to_xlsx("Version.xlsx",version_row,1,BugId)
                version_row +=1
            else:
                print("Write in version NotReassigned",BugId)
                updating_to_xlsx("Version.xlsx", version_row, 2, BugId)
                version_row += 1

        elif "product"in col:
            if (col[col.index("product") + 1].isalnum()):
                print("Write in product Reassigned",BugId)
                updating_to_xlsx("Product.xlsx",product_row,1,BugId)
                product_row +=1
            else:
                print("Write in product NotReassigned",BugId)
                updating_to_xlsx("Product.xlsx", product_row, 2, BugId)
                product_row += 1

        elif "os" in col:
            if (col[col.index("os") + 1].isalnum()):
                print("Write in os Reassigned",BugId)
                updating_to_xlsx("Os.xlsx",os_row,1,BugId)
                os_row +=1
            else:
                print("Write in os NotReassigned",BugId)
                updating_to_xlsx("Os.xlsx", os_row, 1, BugId)
                os_row += 1

        elif "priority" in col:
            if (col[col.index("priority") + 1].isalnum()):
                print("Write in priority Reassigned",BugId)
                updating_to_xlsx("Priority.xlsx",priority_row,1,BugId)
                priority_row +=1
            else:
                print("Write in priority NotReassigned",BugId)
                updating_to_xlsx("Priority.xlsx", priority_row, 1, BugId)
                priority_row += 1

        elif "component" in col:
            if (col[col.index("component") + 1].isalnum()):
                print("Write in component Reassigned",BugId)
                updating_to_xlsx("Component.xlsx",component_row,1,BugId)
                component_row +=1
            else:
                print("Write in component NotReassigned",BugId)
                updating_to_xlsx("Component.xlsx", component_row, 2, BugId)
                component_row += 1


        col = []



