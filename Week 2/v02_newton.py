#Goal:
# - Write some code that reasonably well computes the square root of some number a
#Ideas:
# - Setting the formula f(x) = x^2 - a to zero and solving for x yields the required srt(a)
# - Newton's method to iteratively find zeros of a function f(x) via x_(n+1) = x_n - (f(x_n) / f'(x_n)) helps then ((http://www.mathematik.de/ger/fragenantworten/erstehilfe/nullstellenapproximation/newtonverfahren.html)
#Pre-programming insights:
# - f(x) = x^2 - a  => f'(x) = 2x (http://www.ableitungsrechner.net)
# - 10 iterations might be a reasonable approximation (subject to further testing)
# - x_1 = 1 might be a fair starting value

a = input("Calculate the quare root of a=")
x1  = 1.
x2  = x1 - (x1**2 - a) / (2*x1)
x3  = x2 - (x2**2 - a) / (2*x2)
x4  = x3 - (x3**2 - a) / (2*x3)
x5  = x4 - (x4**2 - a) / (2*x4)
x6  = x5 - (x5**2 - a) / (2*x5)
x7  = x6 - (x6**2 - a) / (2*x6)
x8  = x7 - (x7**2 - a) / (2*x7)
x9  = x8 - (x8**2 - a) / (2*x8)
x10 = x9 - (x9**2 - a) / (2*x9)

print x1, x2, x3, x4, x5, x6, x7, x8, x9, x10
print "The square root of", a, "is (approximately): ", x10

import math
print "(correct result: ", math.sqrt(a), " )"