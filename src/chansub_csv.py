import pandas as pd
import numpy as np
import sys
from time import sleep
import matplotlib.pyplot as plt
import subprocess as sp
from sklearn.metrics import r2_score as r2
import matplotlib.patches as mpatches

sp.call("wget https://github.com/ayaka-wada/chansub/blob/main/src/Number_of_channel_subscribers.csv",shell=True)
sp.call("cat Number_of_channel_subscribers.csv|sed '2,$s/,-/,/g' >new",shell=True)
sp.call("mv new Number_of_channel_subscribers.csv",shell=True)
data=pd.read_csv("Number_of_channel_subscribers.csv")
data.fillna(0,inplace=True)
# sp.call("rm Number_of_channel_subscribers.csv",shell=True)

class main:
 def main(self,name,days=737,degree=7):
   n=len(data[name])
   y=data[name][n-days:n]
   for i in y:
    print(i)
   x=np.arange(n-days,n)
   valid = ~(np.isnan(x) | np.isnan(y))
   model=np.poly1d(np.polyfit(x[valid],y[valid],degree))
   date=data['date'][n-1]
   x1=np.arange(n-days,n+7)
   y1=model(x1)
   ny1=[]
   for i in y1:
    if i<0:i=0
    ny1.append(i)
   x2=np.arange(n-days,n)
   y2=model(x2)
   r2s=round(r2(y,y2),3)
   plt.plot(x,y,'k')
   plt.plot(x1,ny1,'b')
   ax=plt.subplot()
   handles,labels = ax.get_legend_handles_labels()
   st='daily deaths in '+str(name)+'\n'+str(days)+' days from '+str(date)+'\n'+str(degree)+'th regression\n'+'r2: '+str(r2s)
   handles.append(mpatches.Patch(color='none', label=st))
   plt.legend(handles=handles)
   plt.savefig(name+".png")
   plt.show()
name=""
days=737
degree=5
if len(sys.argv)==1:
 print('name is needed!')
 sys.exit()
if len(sys.argv)==2:
 if sys.argv[1] in data.columns:
  name=str(sys.argv[1])
 else:
  print('correct name!')
  sys.exit()
if len(sys.argv)==3:
 if sys.argv[1] in data.columns:
  name=str(sys.argv[1])
  if int(sys.argv[2])>len(data[name]):
   print('use smaller days')
   sys.exit()
  else:
   days=int(sys.argv[2])
 else:
  print('correct name')
  sys.exit()
if len(sys.argv)==4:
 if sys.argv[1] in data.columns:
  name=str(sys.argv[1])
  if int(sys.argv[2])>len(data[name]):
   print('use smaller days')
   sys.exit()
  else:
   days=int(sys.argv[2])
   if int(sys.argv[3]) > 4:
    degree=int(sys.argv[3])
   else:
    print('use higher degree number')
    sys.exit()
 else:
  print('correct name')
  sys.exit()
m=main()
m.main(name=name,days=days,degree=degree)
