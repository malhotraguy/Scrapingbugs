import time

start = time.time()
import requests
import lxml.html as lh
from fake_useragent import UserAgent

ua = UserAgent()
hdr = {'User-Agent': str(ua.chrome)}
import pandas as pd
import openpyxl
from Writing import new_xlsx, updating_to_xlsx

new_xlsx("Severity.xlsx")
severity_row = 2
new_xlsx("Version.xlsx")
version_row = 2
new_xlsx("Status.xlsx")
status_row = 2
new_xlsx("Product.xlsx")
product_row = 2
new_xlsx("Os.xlsx")
os_row = 2
new_xlsx("Priority.xlsx")
priority_row = 2
new_xlsx("Component.xlsx")
component_row = 2

for BugId in range(214019,214020):
    #BugId=214019
    url = 'https://bugs.eclipse.org/bugs/show_activity.cgi?id=' + str(BugId)
    # Create a handle, page, to handle the contents of the website
    page = requests.get(url, headers=hdr)
    # Store the contents of the website under doc
    doc = lh.fromstring(page.content)
    # Parse data that are stored between <tr>..</tr> of HTML
    tr_elements = doc.xpath('//td')
    # Check the length of the first 12 rows
    # print([len(T) for T in tr_elements[:12]])
    # Create empty list
    col = []

    # For each row, store each first element (header) and an empty list
    # print(type(tr_elements[5].text_content()))
    tr_elements.reverse()

    #tr_elements.reverse()

    [col.append((t.text_content().replace(" ","")).replace("\n","").lower()) for t in  tr_elements]
    print(col)
    if "status" in col:
        if col[col.index("status") + 1].lower() == "resolved":
            if col[col.index("status") + 2] == "reopen":

                print("Write in status Reassigned", BugId)

                status_row += updating_to_xlsx("Status.xlsx", status_row, 1, BugId)

            else:

                print("Write in status NotReassigned(!reopen)", BugId)

                status_row += updating_to_xlsx("Status.xlsx", status_row, 2, BugId)

        else:
            print("Write in status NotReassigned(!resolved)", BugId)

            status_row += updating_to_xlsx("Status.xlsx", status_row, 2, BugId)

    if "severity" in col:
        if (not (col[col.index("severity") + 1].isspace()) and (col[col.index("severity") + 1].isspace()) != "--"):
            print("Write in severity Reassigned", BugId)

            severity_row += updating_to_xlsx("Severity.xlsx", severity_row, 1, BugId)
        else:
            print("Write in severity NotReassigned", BugId)

            severity_row += updating_to_xlsx("Severity.xlsx", severity_row, 2, BugId)

    if "version" in col:
        if (not (col[col.index("version") + 1].isspace()) and (col[col.index("version") + 1].isspace()) != "--"):

            print("Write in version Reassigned", BugId)

            version_row += updating_to_xlsx("Version.xlsx", version_row, 1, BugId)
        else:

            print("Write in version NotReassigned", BugId)

            version_row += updating_to_xlsx("Version.xlsx", version_row, 2, BugId)

    if "product" in col:
        if (not (col[col.index("product") + 1].isspace()) and (col[col.index("product") + 1].isspace()) != "--"):
            print("Write in product Reassigned", BugId)

            product_row += updating_to_xlsx("Product.xlsx", product_row, 1, BugId)
        else:
            print("Write in product NotReassigned", BugId)

            product_row += updating_to_xlsx("Product.xlsx", product_row, 2, BugId)

    if "os" in col:
        if (not (col[col.index("os") + 1].isspace()) and (col[col.index("os") + 1].isspace()) != "--"):
            print("Write in os Reassigned", BugId)

            os_row += updating_to_xlsx("Os.xlsx", os_row, 1, BugId)
        else:
            print("Write in os NotReassigned", BugId)

            os_row += updating_to_xlsx("Os.xlsx", os_row, 1, BugId)

    elif "priority" in col:
        if (not (col[col.index("priority") + 1].isspace()) and (col[col.index("priority") + 1].isspace()) != "--"):
            print("Write in priority Reassigned", BugId)

            priority_row += updating_to_xlsx("Priority.xlsx", priority_row, 1, BugId)

        else:
            print("Write in priority NotReassigned", BugId)

            priority_row += updating_to_xlsx("Priority.xlsx", priority_row, 1, BugId)


    if "component" in col:
        if (not (col[col.index("component") + 1].isspace()) and (
        col[col.index("component") + 1].isspace()) != "--"):
            print("Write in component Reassigned", BugId)

            component_row += updating_to_xlsx("Component.xlsx", component_row, 1, BugId)
        else:
            print("Write in component NotReassigned", BugId)

            component_row += updating_to_xlsx("Component.xlsx", component_row, 2, BugId)

    col = []

end = time.time()
print("Script took ", end - start)

