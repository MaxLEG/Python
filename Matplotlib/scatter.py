import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)

"""Assignment of the chart title and axis labels. """
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

""" Setting the font size of the divisions on the axes."""
plt.tick_params(axis="both", which="major", labelsize=14)

"""Assigning a range for each axis"""
plt.axis([0, 1100, 0, 1100000])

"""to show:"""
""" plt.show() """
"""to save diagram in file - suare_plot.png"""
plt.savefig("suare_plot.png", bbox_inches="tight")
