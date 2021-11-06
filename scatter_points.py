import matplotlib.pyplot as plt

y_values = range(1,200)

x_values =[y**1 for y in y_values]


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Create chart title and axes.
ax.set_title("Video Game", fontsize=15)
ax.set_ylabel("Individuals Willing to Play the Game For Income", fontsize=15)
ax.set_xlabel("Levels", fontsize=15)

#Apply tick-labels
ax.tick_params(axis='both', which='major', labelsize=1)


#Set the range for each axis.
ax.axis([0,200,0,300])


plt.savefig('scatter_plot.png', bbox_inches='tight')
plt.show()

