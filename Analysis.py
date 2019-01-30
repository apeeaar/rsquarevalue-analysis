#main
#importing DATASET
import pandas as pd
dataset=  pd.read_csv("analyse1.csv",index_col = False)
dataset=dataset.drop("TAP index",axis=1)
dataset=dataset.drop("tindex",axis=1)
dataset=dataset.drop("MAP index",axis=1)
import matplotlib.pyplot as plt

#Manipulating categories
cat=[]
cols=pd.read_csv("analyse1.csv", nrows=1,index_col = False).columns
cols=cols.drop("TAP index")
cols=cols.drop("tindex")
cols=cols.drop("MAP index")
for i in cols:
    cat.append(i)
#storing categories in dictionary
cat.pop()
dic={}
num=0
for i in cat:
        dic[i]=num
        num+=1
        
#Functions       
def coeff(w):
    print("\nR2 square Coefficient: ")
    return w 

def graph(ax,ay,az):
    az.plot(x=ax, y=ay, kind="line",color="red")

#input for categories
print("Categories")
for i in dic.keys():
    print(i)
inp1=str(input("\nYour X Axis "))
cat1=dic[inp1]
inp2=str(input("\nYour Y Axis "))
cat2=dic[inp2]
scat=dataset.iloc[:,[cat1,cat2]]
mean=scat[inp2].mean()

#creating dataset c for R Squared Value computation
c=dataset.iloc[:,[cat1,cat2]].copy()
c['bar']=''
lst=[]
for i in c[inp2]:
    lst.append(i)
for i in range(len(lst)):
    lst[i]=mean-lst[i]   
c['bar']=lst
c['bar2']=c['bar']**2

#creating dataset reg for Regression analysis 
reg=dataset.iloc[:,[cat1,cat2]].copy()
reg['xy']=reg[inp1]*reg[inp2]
reg['x2']=reg[inp1]**2
reg['y2']=reg[inp2]**2
x=[]
y=[]
xy=[]
n=len(cat)
xx=[]
yy=[]

for i in reg[inp1]:
    x.append(i)
for i in reg[inp2]:
    y.append(i)
for i in reg['xy']:
    xy.append(i)
for i in reg['x2']:
    xx.append(i)
for i in reg['y2']:
    xx.append(i)    

#computation for regression
sumx=sum(x)
sumy=sum(y)
sumxy=sum(xy)
sumxx=sum(xx)
sumyy=sum(yy)
        
p=sumy*sumxx
q=sumx*sumxy
r=n*sumxx
s=sumx*sumx
t=n*sumxy
u=sumx*sumy

#Obtaining regression line constants
A=((p-q)/(r-s))
B=((t-u)/(r-s))

#computation for R Squared Value
c['lol']=A+c[inp1]*B
c['lol2']=c['lol']-mean
c['lol3']=c['lol2']**2
lst1=[]
for i in c["bar2"]:
    lst1.append(i)
lst2=[]
for i in c["lol3"]:
    lst2.append(i)
mod1=sum(lst1)
mod2=sum(lst2)   
R=mod2/mod1        


print(graph(inp1,inp2,c))
print(coeff(R))

   


