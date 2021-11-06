import matplotlib.pyplot as plt

#plt.style.available
#['seaborn-dark', 'seaborn-dack-grid','seaborn-ticks','fivethirtyeight',]
input_values = [5, 10, 15, 20, 25, 30, 35, 40, 45]
coding = [10,44,39,46,15,30, 24, 2, 0]

plt.style.use('fivethirtyeight')
# plt.style.use('seaborn-ticks')

fig, ax = plt.subplots()
ax.plot(input_values, coding,  linewidth=2, c='red')


#Chart tile and label for axes.
ax.set_title("Some Numbers", fontsize=15)
ax.set_xlabel("Age", fontsize=15)
ax.set_ylabel("Enjoys Coding", fontsize=15)

#Size of label for ticks
ax.tick_params(axis='both', labelsize=10)

plt.show()