from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

'''
Generic graphing functions
'''


'''
Creates one basic plot at a name for simple X-Y line plot.
# Todo:
    - Implement multi axis control for the figure.
'''
def create_line_plot(X, Y, xlabel, ylabel, title, **kwargs):
    fig, plot = plt.subplots(**kwargs) # how to handle?
    plot.plot(X, Y)
    plot.set_title(title)
    plot.set_ylabel(ylabel)
    plot.set_xlabel(xlabel)

    return (fig, plot)


'''
Creates a Policy Map for action space of Easy21
'''
def create_2d_heat_map(data, x_tick_labels, y_tick_labels, text_labels, title, x_label, y_label, cmap="copper"):
    policy_map, ax = plt.subplots()
    im = ax.imshow(data, cmap=cmap)

    ax.set_xticks(np.arange(len(x_tick_labels)))
    ax.set_yticks(np.arange(len(y_tick_labels)))
    ax.set_xticklabels(x_tick_labels)
    ax.set_yticklabels(y_tick_labels)
 
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Loop over data dimensions and create text annotations.
    for i in range(len(data)):
        for j in range(len(data[0])):
            text = ax.text(j, i, text_labels[data[i,j]],
                        ha="center", va="center", color="w")

    policy_map.tight_layout()
    return (policy_map, ax)