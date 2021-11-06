from plotly.graph_objs import Bar, Layout
from plotly import offline


from roll_dice import A_Die

#Create a 8 Die.

a_die_1 = A_Die()
a_die_2 = A_Die(10)

#Create a bunch of rolls, also store
# all results in a list.

all_rolls = []
for roll_num in range(100000):
    a_roll = a_die_1.roll() + a_die_2.roll()
    all_rolls.append(a_roll)

#Analyze the rolls.

analyzation = []
limited_result = a_die_1.num_sides + a_die_2.num_sides
for value in range(2, limited_result+1):
    analyze = all_rolls.count(value)
    analyzation.append(analyze)
print(analyzation)

# Show visualization of results.
x_values = list(range(2, limited_result+1))
data = [Bar(x=x_values, y=analyzation)]

x_axis_config = {'title': 'Rolls', 'dtick': 1}
y_axis_config = {'title': 'Analyzed Results'}
die_layout = Layout(title='A 8 die and a 10 die rolled 100,000 times',
                    xaxis=x_axis_config, yaxis=y_axis_config,)
offline.plot({'data': data, 'layout': die_layout}, filename='d8_d10.html')