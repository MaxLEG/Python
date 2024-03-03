import matplotlib
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

"""Assignment of the chart title and axis labels."""
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)

plt.plot(squares)
plt.show()
