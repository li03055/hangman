num = int(input("Enter 3 digit number: "))  # each number for one pig
# num bricks for each pig
pig1 = num // 100
pig2 = num % 100 // 10
pig3 = num % 10

sum_bricks = pig1 + pig2 + pig3
print("Sum of bricks: ", sum_bricks)

each_bricks_for_pig = sum_bricks // 3
sheerit_haloka = sum_bricks % 3
print("Each pig bricks: ", each_bricks_for_pig)
print("sheerit of sum bricks: ", sheerit_haloka)
print("Is sheerit_haloka 0?", sheerit_haloka == 0)
