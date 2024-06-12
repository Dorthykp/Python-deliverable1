name = "Christa"
print("Welcome to GC mini golf! What is your name?" + name)
holes = ["3", "6"]
print("Hi Christa! Would you like to play 3 or 6 holes?" + holes[0])
hole_par = [4, 2, 3]
print("How many putts for hole 1? (par is 3)" + str(hole_par[0]))
print("How many putts for hole 2? (par is 3)" + str(hole_par[1]))
print("How many putts for hole 3? (par is 3)" + str(hole_par[2]))
par = 9
total_putts = sum(hole_par)
score = par - total_putts
if score == 0:
    print(f"Good game, {name}! Your total score was: 0")
elif score < 0:
    print(f"Great job, {name}! Your total score was: -{score}")
else:
    print(f"Nice try {name}! Your total score was +{score}")
