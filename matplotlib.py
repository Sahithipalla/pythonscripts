import matplotlib.pyplot as plt

y_views=[23,456,789,345,765,234]
f_views=[674,987,231,654,786,709]
t_views=[123,234,345,765,550,999]
days=[1,2,3,4,5,6]
plt.scatter(days,y_views, label="youtube views",color="b",marker="*",linestyle=":")
plt.scatter(days,f_views, label="facebook views",color="g",marker="*",linestyle=":")
plt.scatter(days,t_views, label="twitter views",color="c",marker="*",linestyle=":")
plt.xlabel("days")
plt.ylabel("views")
plt.title("youtube channel views daily")
plt.legend()

plt.xlim(1,4)
plt.ylim(100,999)
plt.grid(True,color="r",linestyle="--")
plt.savefig("img_3.png",dpi=550,facecolor="cyan")
plt.show()


