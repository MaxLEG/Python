import pygal
from cube import Cube

"""creating D6 cube"""
cube = Cube()
"""Simulation of a series of throws with saving the results in a list."""
results = []
for roll_num in range(1000):
    result = cube.roll()
    results.append(result)
    """analysis of the results"""
    frequencies = []
    for value in range(1, cube.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    """results visualisation"""
    hist = pygal.Bar()
    hist.title = "Results of rolling one D6 1000 times"
    hist.x_labels = [str(i) for i in range(1, 7)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add("D6", frequencies)
    hist.render_to_file("Visualisation/cube/cube_visual.svg")
"""     print(frequencies) """
print(results)
