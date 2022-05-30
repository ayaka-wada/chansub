import subprocess as sp

import pandas
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import sys, os
if os.path.exists('./Number_of_channel_subscribers.xlsx'):
 wb = openpyxl.load_workbook('Number_of_channel_subscribers.xlsx')
else:
 sp.call("wget https://github.com/ayaka-wada/chansub/blob/main/src/Number_of_channel_subscribers.xlsx", shell=True)
 wb = openpyxl.load_workbook('Number_of_channel_subscribers.xls')
 # wb = pandas.read_excel('Number_of_channel_subscribers.xlsx', engine = 'openpyxl')
# sheet = wb['Sheet1']
# sheet.delete_rows(sheet.min_row,5)
wb.save('result.xlsx')
d = pd.read_excel('result.xlsx', engine='openpyxl')
size = 0
names = []

for i in d.name:
 if i != 'Usada Pekora':
  names.append(i)
  size=size+1
 else: 
  names.append(i)
  size=size+1
  break
print(len(names), ': ', names)
no = len(sys.argv)-1
x = []
for i in range(2000, 2021):
 x.append(i)
cnt = []
for i in range(no):
 if sys.argv[i+1] in names:
  #print(sys.argv[i+1])
  cnt.append(d.loc[d.name==sys.argv[i+1]])
 else:
  print('correct the name of ', sys.argv[i+1])

nme = []
#print(len(cnt))
for j in range(len(cnt)):
 for i in range(2000, 2021):
  nme.append(int(cnt[j][i]))

if len(cnt) == 1:
 plt.plot(x, nme, 'k-', label=sys.argv[1])

if len(cnt) == 2:
 plt.plot(x, nme[0:21], 'k-', label=sys.argv[1])
 plt.plot(x, nme[21:42], 'k--', label=sys.argv[2])

if len(cnt) == 3:
 plt.plot(x, nme[0:21], 'k-', label=sys.argv[1])
 plt.plot(x, nme[21:42], 'k--', label=sys.argv[2])
 plt.plot(x, nme[42:63], 'k:', label=sys.argv[3])

if len(cnt) == 4:
 plt.plot(x, nme[0:21], 'k-', label=sys.argv[1])
 plt.plot(x, nme[21:42], 'k--', label=sys.argv[2])
 plt.plot(x, nme[42:63], 'k:', label=sys.argv[3])
 plt.plot(x, nme[63:84], 'k-.', label=sys.argv[4])

def main():
 plt.legend()
 plt.savefig('result.png')
 plt.show()
