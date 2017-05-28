from die import Dice
import pygal
d1 = Dice()
d2 = Dice()
results = [d1.roll()*d2.roll() for x in range(50000)]  #50000 rolls. multiply 2 results together.

max_Result = d1.sides*d2.sides  #36
frequencies = [results.count(x) for x in range(1,max_Result+1)]

hist = pygal.Bar()
hist.title = "2 Six-faced dies rolled 50k times"
hist.x_labels = [str(x) for x in range(1,max_Result+1)]
hist.x_title = "Result"
hist.y_title = "Result Frequencies"

hist.add('Roll Results', frequencies)
hist.render_to_file('multiplyDie.svg')
