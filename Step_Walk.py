from Step_initialize import RandomWalk
import matplotlib.pyplot as plt
while True:
    rw = RandomWalk()
    rw.fill_walk()
    number_of_points = list(range(rw.num_points))
    plt.plot(rw.x_value,rw.y_value, linewidth = 0.5)
    plt.scatter(0,0,s=100,c='green',edgecolors = 'none')
    plt.scatter(rw.x_value[-1],rw.y_value[-1],s=100, c= 'red',edgecolors = 'none')
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.figure(figsize = (10,6))
    plt.show()
    answer = input('yes or no: y/n')
    if answer == 'n':
        break