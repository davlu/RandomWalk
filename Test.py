import matplotlib.pyplot as plt
x_values = list(range(1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,s=10, c = y_values, cmap=plt.cm.Reds, edgecolor = 'none') #ALL POINTS ON GRAPH
#linewidths = arg for plt.plot

plt.axis([0,1100,0,1100000]) #AXIS RANGE

plt.title("Square Numbers", fontsize = 24)
plt.ylabel("Square of Value", fontsize = 14)
plt.xlabel("Value", fontsize = 14)

plt.tick_params(axis='both',labelsize=14) #CHANGE PARAMETER SIZE
plt.savefig('savefile.png',bbox_inches = 'tight') #SAVE

plt.figure(figsize = (10,6)) #figure resolution. can add dpi= argument

plt.show()