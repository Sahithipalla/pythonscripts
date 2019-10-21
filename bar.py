 import matplotlib.pyplot as plt

y_views=[123,456,735,256,213,822]
f_views=[114,215,684,165,127,521]
days=[1,2,3,4,5,6]
plt.bar(days,y_views,label="youtube views",color="g")
plt.bar(days,f_views,label="facebook views",color="c")
plt.xlabel("days")
plt.ylabel("views")
plt.title("youtube channel views")
plt.legend()
plt.savefig("bar_1.png",dpi=500)
plt.show()
