RB = int(input("Enter number of red balls: "))
BB = int(input("Enter number of blue balls: "))
WB = int(input("Enter number of white ballss: "))

total = RB+BB+WB

prob_a = BB/total
prob_b = RB/total

prob_bga = prob_b
prob_a_and_b = prob_a*prob_b

print("Probability that the second ball is red given that the first ball is blue: ")
print(round((prob_bga),2))

print("Probability that the second ball is red and the first ball is blue: ")
print(round((prob_a_and_b),2))
