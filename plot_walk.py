import matplotlib.pyplot as plt

from random_walk import Walks
while True:
    walks = Walks(150_000)
    walks.desired_walks()

    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(15, 15,), dpi=100)
    points_num = range(walks.num_points)
    ax.scatter(walks.x_values, walks.y_values, c=points_num,
               cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Make first and last points stand out.
    ax.scatter(0, 0, c='yellow', edgecolor='none', s=100)
    ax.scatter(walks.x_values[-1], walks.y_values[-1], c='red',
               edgecolor='none', s=100)

    #Make the axis disapear.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    cntnu_running = input("Would you like to "
                         "make another walk? (y/n): ")
    if cntnu_running == 'n':
        break