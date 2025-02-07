
import matplotlib.pyplot as plt
import numpy as np

group_B = [12, 17, 15, 13, 19, 20, 21, 18, 17, 16, 15, 14, 16, 15]

fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.title("Group B")
plt.ylabel("y-axis")
fig.suptitle("Box Plot Analysis", fontsize=16)
plt.boxplot(group_B)

# show plot
plt.show()