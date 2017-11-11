c = input("Please state your base capital [CHF]: ")
i = input("Please enter an interest rate [%]: ")
print "Your return after 8 years of investment at ", i
print "% will be ", #mind: the "," at the end of print prevents a newline

multiplier = 1 + i/100.0 #don't forget to add decimals to the divisor!

y1 = c*multiplier
y2 = y1*multiplier
y3 = y2*multiplier
y4 = y3*multiplier
y5 = y4*multiplier
y6 = y5*multiplier
y7 = y6*multiplier
y8 = y7*multiplier #calculate it more easily as y8=c * multiplier**8

print y8, " CHF."
