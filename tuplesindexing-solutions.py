#access the number 7 in the following set of tuples.
sevensTuple0 = (0, 3, 4, 7, 3)
sevensTuple1 = (0, 9, 5, 2, (7, 1))
sevensTuple2 = (1, [4], ('cat', (5, (8, 7) ) ), 13)

zerothSeven = sevensTuple0[3]
onethSeven = sevensTuple1[4][0]
twothSeven = sevensTuple2[2][1][1][1]

#print out the number you access so can see your answer.
print(zerothSeven, onethSeven, twothSeven)
