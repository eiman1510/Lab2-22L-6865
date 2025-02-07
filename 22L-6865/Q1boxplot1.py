
import matplotlib.pyplot as plt
import numpy as np

group_A = [12, 15, 14, 13, 16, 18, 19, 15, 14, 20, 17, 14, 15,40,45,50,62]

fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.title("Group A")
plt.ylabel("y-axis")
fig.suptitle("Box Plot Analysis", fontsize=16)
plt.boxplot(group_A)

# show plot
plt.show()