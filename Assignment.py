import datetime
import matplotlib.pyplot as plt
import json
import pandas as pd

class my_dictionary(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key] = value

def common_dates(a, b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return (a_set.intersection(b_set))

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + datetime.timedelta(n)

#loading the data.json file and converting it into data frame the file is placed in same project directory
with open('data.json') as json_data:
    d = json.load(json_data)
df = pd.DataFrame(d["rates"])
index=df.index
columns=df.columns

print("Please enter a date in YYYY-MM-DD format .Date Should be Between Jan 2019 - Dec 2019")
star_dt=input("Enter Start Date")
yr,mo,day=map(int,star_dt.split('-'))
start_dt = datetime.date(yr,mo,day)
end_dt=input("End Date")
yr,mo,day=map(int,end_dt.split('-'))
end_dt = datetime.date(yr,mo,day)
datelist=[]

#To get the dates between Start date and End Date 
for dt in daterange(start_dt, end_dt):
    datelist.append(dt.strftime("%Y-%m-%d"))
#print(datelist)
#print(index)
#print(columns)
#finding common dates between dataframes columns and required dates
finaldates=common_dates(columns,datelist)
finaldates=list(finaldates)

#creating dictionary to store INR exchange rates between given dates
dict_obj = my_dictionary()

for i in range(len(finaldates)):
    datepass=str(finaldates[i])
    #print(datepass,df.loc['INR',datepass])
    dict_obj.key = datepass
    dict_obj.value =df.loc['INR',datepass]
    dict_obj.add(dict_obj.key, dict_obj.value)

keys = dict_obj.keys()
values = dict_obj.values()

#Plot graph
plt.xticks(rotation=45)
plt.bar(keys, values,align='edge')
plt.show()



