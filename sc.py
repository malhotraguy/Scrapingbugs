def making_list(file,colu):
    import pandas as pd

    smlv_df = pd.ExcelFile(file)
    smlv_df = smlv_df.parse('Sheet')
    smlv_list = []

    for i in range(len(smlv_df)):

        val = smlv_df.iloc[i]
        #print(val[0])
        smlv_list.append(int(val[colu]))

    return (smlv_list)
from Writing import *
import time
from collections import Counter
start = time.time()
Component_BugIdlist=making_list("Component.xlsx",0)
Assignee_BugIdlist=making_list("Assignee.xlsx",0)
Priority_BugIdlist=making_list("Priority.xlsx",0)
Os_BugIdlist=making_list("Os.xlsx",0)
Product_BugIdlist=making_list("Product.xlsx",0)
Version_BugIdlist=making_list("Version.xlsx",0)
Severity_BugIdlist=making_list("Severity.xlsx",0)
Status_BugIdlist=making_list("Status.xlsx",1)
unique_BugId_list=(Component_BugIdlist+Assignee_BugIdlist+Priority_BugIdlist+Os_BugIdlist+Product_BugIdlist+Version_BugIdlist+Severity_BugIdlist+Status_BugIdlist)
#print(unique_BugId_list)
#print(len(unique_BugId_list))
#cnt_ = Counter(unique_BugId_list)
#print(cnt_.most_common(15))
unique_BugId_set=set(unique_BugId_list)
num=2
for w in (sorted(unique_BugId_set.difference(set(Component_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Component.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Assignee_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Assignee.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Priority_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Priority.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Os_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Os.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Product_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Product.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Version_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Version.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Severity_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Severity.xlsx", num, 2, w, status_flag=None)
num=2
for w in (sorted(unique_BugId_set.difference(set(Status_BugIdlist)))):
    print(w)
    num += updating_to_xlsx("Status.xlsx", num, 1, w, status_flag=None)
end = time.time()
print("Script took ", end - start)
