import matplotlib.pyplot as plt

ages=[22,21,52,64,87,64,23,54,56,72]
bins=[0,20,40,60,80,100,120]
plt.hist(ages,bins)

plt.xlabel("ages")
plt.ylabel("frequency")
plt.title("current ages of people")
plt.legend()
plt.savefig("hist_1.png",dpi=500)
plt.show()


