import pygal
from cube import Cube

"""creating two D6 cubes """
cube_one = Cube()
cube_two = Cube()

"""Simulation of series of throws with saving the results in a list"""
results = []
for roll_num in range(1000):
    result = cube_one.roll() + cube_two.roll()
    results.append(result)

"""analysis of the results"""
frequencies = []
max_result = cube_one.num_sides + cube_two.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

    """results visualisation"""
    hist = pygal.Bar()
    hist.title = "Results of rollin two D6 dice 1000 times"
    hist.x_labels = [str(i) for i in range(2, 13)]
    hist._x_title = "Result"
    hist.y_title = "Frequency of result"
    hist.add("D6 + d6", frequencies)
    hist.render_to_file("Visualisation/cube/double_cube_visual.svg")
