def making_list(file,colu):
    import pandas as pd
    smlv_df = pd.ExcelFile(file)
    smlv_df = smlv_df.parse('Sheet')
    smlv_list = []

    for i in range(len(smlv_df)):

        val = smlv_df.iloc[i]

        smlv_list.append(int(val[colu]))

    return (smlv_list)
from Writing import *
import time
import pandas as pd

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

unique_BugId_set=set(unique_BugId_list)

Component_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Component_BugIdlist)))
Assignee_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Assignee_BugIdlist)))
Priority_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Priority_BugIdlist)))
Os_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Os_BugIdlist)))
Product_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Product_BugIdlist)))
Version_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Version_BugIdlist)))
Severity_BugIdlist_notreassigned=sorted(unique_BugId_set.difference(set(Severity_BugIdlist)))

def Filling_NotReassigned(File_Name,Field_BugIdlist_notreassigned):

    df1=pd.ExcelFile(File_Name)
    df1=df1.parse("Sheet")
    df2=pd.DataFrame({"Not-Reassigned":Field_BugIdlist_notreassigned},dtype=object)
    df1=pd.concat([df1,df2],axis=1)
    writer = pd.ExcelWriter(File_Name, engine='xlsxwriter')
    df1.to_excel(writer, sheet_name='Sheet', index_label=False, index=False, header=True)
    writer.save()
    return File_Name
Filling_NotReassigned("Component.xlsx",Component_BugIdlist_notreassigned)
Filling_NotReassigned("Assignee.xlsx",Assignee_BugIdlist_notreassigned)
Filling_NotReassigned("Priority.xlsx",Priority_BugIdlist_notreassigned)
Filling_NotReassigned("Os.xlsx",Os_BugIdlist_notreassigned)
Filling_NotReassigned("Product.xlsx",Product_BugIdlist_notreassigned)
Filling_NotReassigned("Version.xlsx",Version_BugIdlist_notreassigned)
Filling_NotReassigned("Severity.xlsx",Severity_BugIdlist_notreassigned)

end = time.time()
print("Script took ", end - start)
