import matplotlib.pyplot as plt
labels_1=["facebook","instagram","youtube","twitter"]
days=[1,2,3,4]
explode_1=[0,0,0,0.2]
plt.pie(days,labels=labels_1,explode=explode_1,autopct="%0.3f%%",shadow=True)
plt.savefig("pie.png",dpi=500)
plt.show()

