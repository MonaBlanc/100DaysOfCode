#Highest score
#Write a program that reads in a list of scores and outputs the highest score.
scores = []
score = int(input("Enter score (9999 to end): "))
while score != 9999:
    scores.append(score)
    score = int(input("Enter score (9999 to end): "))
print("The highest score is", max(scores))

#Add all even numbers between 1 and 100
total = 0
for i in range(2, 101, 2):
    total += i
print(total)

total2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        total2 += i
print(total2)

