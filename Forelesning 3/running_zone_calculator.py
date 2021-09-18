print("====Calculate your running zone based on average heart rate====")

# Getting heart rate numbers for the user.
average_5k_heart_rate = float(input("Type in your average heart rate from your 5k runs:"))
average_10k_heart_rate = float(input("Type in your average heart rate from your 10k runs:"))

# Taking away a given number from heart rates
average_5k_heart_rate -= 15
average_10k_heart_rate -= 10

# Using avg heart rates to find lactate threshold
lactate_threshold = (average_5k_heart_rate + average_10k_heart_rate) / 2

# Printing the calculated threshold
print(f"Your calculated lactate threshold is: {lactate_threshold}")

# Calculating zones 1 through 5
zone1 = int(lactate_threshold * 0.8)
zone2_from = int(lactate_threshold * 0.81)
zone2_to = int(lactate_threshold * 0.89)
zone3_from = int(lactate_threshold * 0.9)
zone3_to = int(lactate_threshold * 0.95)
zone4_from = int(lactate_threshold * 0.96)
zone4_to = int(lactate_threshold * 0.99)
zone5 = int(lactate_threshold)

# Printing the information on zones 1 through 5
print("\n============ZONES============")
print(f"Your zone 1 is up to a heart rate of {zone1}")
print(f"Your zone 2 heart rate is from {zone2_from} to {zone2_to}")
print(f"Your zone 3 heart rate is from {zone3_from} to {zone3_to}")
print(f"Your zone 4 heart rate is from {zone4_from} to {zone4_to}")
print(f"Your zone 5 heart rate is over {zone5}")