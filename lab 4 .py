it 12-

import random

# Generate ten random diameters

for i in range(10):
    diameter = random.uniform(24.90, 25.10)

    print("Part", i + 1, "Diameter:",
          round(diameter, 2))
it 10- 
import random

accept = 0
rework = 0
scrap = 0

# Generate and inspect 10 parts

for i in range(10):
    diameter = random.uniform(24.90, 25.10)
    diameter = round(diameter, 2)

    print("\nPart", i + 1, "Diameter:", diameter)

    if 24.95 <= diameter <= 25.05:
        print("ACCEPT")
        accept += 1

    elif 24.90 <= diameter <= 25.10:
        print("REWORK")
        rework += 1

    else:
        print("SCRAP")
        scrap += 1

# Final shift report

print("\n===== SHIFT REPORT =====")
print("Accepted:", accept)
print("Rework:", rework)
print("Scrap:", scrap)
print("Total:", accept + rework + scrap)
it-8
import random

accept = 0
rework = 0
scrap = 0
inspected = 0

mode = input("Enter mode (halt/skip): ").lower()

for i in range(10):
    diameter = round(random.uniform(24.90, 25.10), 2)
    inspected += 1

    print("\nPart", inspected, "Diameter:", diameter)

    if 24.95 <= diameter <= 25.05:
        print("ACCEPT")
        accept += 1

    elif 24.93 <= diameter <= 25.07:
        print("REWORK")
        rework += 1

    else:
        print("SCRAP")
        scrap += 1

        if mode == "halt":
            print("Scrap found! Stopping batch.")
            break

        elif mode == "skip":
            print("Skipping scrap and continuing.")
            continue

# Final report

print("\n===== FINAL REPORT =====")
print("Inspected:", inspected)
print("Accepted:", accept)
print("Rework:", rework)
print("Scrap:", scrap)
it-6
import random

accept = 0
rework = 0
scrap = 0

consecutive = 0
attempts = 0

# Safety cap
max_attempts = 500

while consecutive < 5 and attempts < max_attempts:

    diameter = round(random.uniform(24.90, 25.10), 2)
    attempts += 1

    print("\nPart", attempts, "Diameter:", diameter)

    if 24.95 <= diameter <= 25.05:
        print("ACCEPT")
        accept += 1
        consecutive += 1

    elif 24.93 <= diameter <= 25.07:
        print("REWORK")
        rework += 1
        consecutive = 0

    else:
        print("SCRAP")
        scrap += 1
        consecutive = 0

# Final report

print("\n===== PRODUCTION REPORT =====")

print("Total attempts:", attempts)
print("Accepted:", accept)
print("Rework:", rework)
print("Scrap:", scrap)

if consecutive == 5:
    print("SUCCESS: Five consecutive ACCEPTS achieved!")

else:
    print("Safety limit reached. Five consecutive ACCEPTS not achieved.")
