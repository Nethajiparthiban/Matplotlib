import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#simple plot
X=[1,2,3,4,5,6,7]
Y=[1,2,3,4,5,6,7]
#plt.plot(X,Y)
#plt.show()
x=np.array([1,2,3,4,5,6,7])
y=np.array([1,1,2,4,5,7,13])
#plt.plot(x,y,color='red')
#plt.show()
y=[2,5,9,13,18]
#plt.plot(y,linestyle='dotted',color='red')
#plt.show()
#plt.plot(y,linewidth=5,linestyle='-.',color='orange')
#plt.show()
#matplotlib.lines.lineStyles
#plt.show()
y1=[1,2,3,4,5]
y2=[2,5,9,13,18]
#plt.plot(y1)
#plt.plot(y2)
#plt.show()
x1=[1,2,3,4,5]
y1=[1,2,3,4,5]
x2=[1,2,3,4,5]
y2=[2,5,9,13,18]
x3=[1,2,3,4,5]
y3=[2,4,6,8,10]
#plt.plot(x1,y1,x2,y2,x3,y3)
#plt.show()
#markers
y=[2,5,9,13,18]
#plt.plot(y,marker='o',color='red',linestyle='-.',linewidth=5)
#plt.show()
y1=[1,2,3,4,5]
y2=[2,5,9,13,18]
#plt.plot(y1,marker='s',markersize=1,linewidth=4,color='yellow')
#plt.plot(y2,marker='D',markersize=0.7,linewidth=5,color='pink')
#plt.show()
y=[2,5,9,13,18]
#plt.plot(y,marker='o',markersize=12)
#plt.show()
#plt.plot(y,marker='o',markersize=12,markeredgecolor='red',mfc='yellow')
#plt.show()
x=np.linspace(start=-np.pi,stop=np.pi,num=256)
y=np.sin(2*x)
#plt.plot(x,y,linewidth=0.5,color='red')
#plt.show()
#plt.plot(x,y,color='orange',linewidth=1)
#plt.fill_between(x,y1=y,y2=0,alpha=0.1)
#plt.show()
x=['jan','feb','mar','apr','may']
y1=[1,2,3,4,5]
y2=[2,5,9,13,18]
y3=[2,4,6,8,10]
#plt.plot(x,y1,x,y2,x,y3)
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.show()
#Adding titles
#plt.plot(x,y1,x,y2,x,y3)
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.title('Monthly Sales')
#plt.show()
#Display the legend
#plt.plot(x,y1,x,y2,x,y3)
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.title('Monthly Sales')
#plt.legend(labels=['Alice','Bob','Carol'],loc='upper center')
#plt.show()
#Adding Grid Lines
#plt.plot(x,y1,x,y2,x,y3,marker='D')
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.title('Monthly Sales')
#plt.legend(labels=['Alice','Bob','Carol'],loc='upper left')
#plt.grid(True)
#plt.show()
#plt.plot(x,y1,x,y2,x,y3, marker='s')
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.title('Monthly Sales')
#plt.legend(labels=['Alice','Bob','Carol'],loc='upper right')
#plt.grid(color='blue',alpha=0.2,linewidth=2)
#plt.show()
#Figure size
#fig=plt.figure(figsize=(6,12))#1st value is width and 2nd one will be Length
#plt.plot(x,y1,x,y2,x,y3, marker='D')
#plt.xlabel('Month')
#plt.ylabel('Sales')
#plt.title('Monthly Sales')
#plt.legend(labels=['Alice','Bob','Carol'],loc='upper left')
#plt.grid(True)
#plt.show()
#Plot Types
titanic_data=pd.read_csv(r"C:\Users\Netha\Desktop\PowerBI\train.csv")
#print(titanic_data.head())
#Bar plots

embarked=titanic_data['Embarked'].value_counts()
#print(embarked.index)#This will be out bar labels
#print(embarked.values)#this will be heights of the bars
#Lets create the bar plot.
#plt.bar(x=embarked.index,height=embarked.values)
#plt.show()
#plt.bar(x=embarked.index,height=embarked.values,color=['blue','green','red'])
#plt.show()
#plt.barh(y=embarked.index,width=embarked.values,color=['orange','blue','yellow'])
#plt.show()
#Stacked barplots.
embarked_m=titanic_data[titanic_data['Sex']=='male']['Embarked'].value_counts()
embarked_f=titanic_data[titanic_data['Sex']=='female']['Embarked'].value_counts()
#print(embarked_m)
#print(embarked_f)
#In order to stack bars, we plot one set of data normaly, then we tell matplot to stack the other
#on top using the bottom parameter.This specifies the y-coordinates of the bars bases.
#plt.bar(x=embarked_m.index,height=embarked_m.values,color='red')
#plt.bar(x=embarked_f.index,height=embarked_f.values,color='blue')
#plt.show()
#finaly we can use the same functions that we saw b4 to provide axis labels a title and a plot legend
#plt.bar(x=embarked_m.index,height=embarked_m.values,color='blue',width=0.7)
#plt.bar(x=embarked_f.index,height=embarked_f.values,color='red',width=0.7)
#plt.xlabel('Port')
#plt.ylabel('Passengers')
#plt.title('Port of Embarkation by sex')
#plt.legend(labels=['M','F'])
#plt.show()
#Histograms
ages=titanic_data['Age']
#plt.hist('ages')
#plt.show()
#plt.hist(ages,density=True)
#plt.show()
#plt.hist(ages,bins=20)
#plt.xlabel('Age')
#plt.ylabel('Passengers')
#plt.title('Distribution of passengers Ages')
#plt.grid(True)
#plt.show()
#Pie Charts.
x=titanic_data['Sex'].value_counts()
#plt.pie(x)
#plt.show()
#plt.pie(x,labels=['Male','Female'])
#plt.show()
#plt.pie(x,labels=['Male','Female'],startangle=90)
#plt.show()
#plt.pie(x,labels=['Male','Female'],startangle=90,explode=[0.1,0])
#plt.show()
#plt.pie(x,labels=['Male','Female'],startangle=90,autopct='%.1f%%')
#plt.show()
#Scatter plots
#age=titanic_data['Age']
#fare=titanic_data['Fare']
#plt.scatter(x=age,y=fare)
#plt.show()
age_m=titanic_data[titanic_data['Sex']=='male']['Age']
fare_m=titanic_data[titanic_data['Sex']=='male']['Fare']
age_f=titanic_data[titanic_data['Sex']=='female']['Age']
fare_f=titanic_data[titanic_data['Sex']=='female']['Fare']
#plt.scatter(x=age_m,y=fare_m)
#plt.scatter(x=age_f,y=fare_f)
#plt.legend(['male','female'])
#plt.show()
age=titanic_data['Age']
fare=titanic_data['Fare']
pclass=titanic_data['Pclass']
#fig=plt.figure(figsize=(12,6))
#plt.scatter(x=age,y=fare,c=pclass,cmap='RdYlGn')
#plt.colorbar(ticks=[1,2,3])
#plt.xlabel('Age')
#plt.ylabel('Fare')
#plt.show()
#fig=plt.figure(figsize=(12,6))
#plt.scatter(x=age,y=fare,s=(pclass*35))
#plt.xlabel('Age')
#plt.ylabel('Fare')
#plt.show()
#Box Plots
age=titanic_data['Age'].dropna()
#fig=plt.figure(figsize=(6,6))
#plt.boxplot(age,labels=['Age'])
#plt.show()
#3D Plots
age=titanic_data['Age']
fare=titanic_data['Fare']
pclass=titanic_data['Pclass']
#fig=plt.figure(figsize=(9,9))
#ax=plt.axes(projection='3d')
#ax.scatter(xs=age,ys=fare,zs=pclass)
#ax.set_xlabel('Age')
#ax.set_ylabel('Fare')
#ax.set_zlabel('Class')
#plt.show()
#fig=plt.figure(figsize=(9,9))
#ax=plt.axes(projection='3d')
#ax.scatter(xs=age,ys=fare,zs=pclass,cmap='brg')
#ax.set_xlabel('Age')
#ax.set_ylabel('Fare')
#ax.set_zlabel('Class')
#plt.show()
#Subplots
s_vals=titanic_data['Sex'].value_counts()
e_vals=titanic_data['Embarked'].value_counts()
#fig,axes=plt.subplots(1,2)#create a grid with 1 row and 2 columns
#fig.set_size_inches(8,4)#make the figure wide
#Create a pie chart in the first grid slot
#axes[0].pie(s_vals,labels=['Male','Female'],startangle=90,autopct='%.1f%%')
#axes[0].set_title('Sex')
#Create a pie chart in the second grid slot.
#axes[1].pie(e_vals,labels=['S','C','Q'],startangle=90,explode=[0,0.1,0])
#axes[1].set_title('Embarked')
#plt.show()
