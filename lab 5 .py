it 12-
# One Line, Three Fields

raw = "P001, 25.02, day"

# Extract fields
fields = raw.split(",")

part_code = fields[0].strip()
diameter = float(fields[1].strip())
shift = fields[2].strip()

# Print details
print("Part Code:", part_code)
print("Diameter:", diameter)
print("Shift:", shift)

# Prove diameter is a number
print("Diameter + 0.01 =", diameter + 0.01)

it 10-
# The Whole Shift Log

logs = [
    "P001, 25.02, day",
    "P002, 24.98, day",
    "P003, 25.08, day",
    "P004, 25.12, day",
    "P005, 24.92, day",
    "P006, 25.00, night",
    "P007, 24.97, night",
    "P008, 25.06, night",
    "P009, 25.11, night",
    "P010, 24.99, night"
]

diameters = []

# Parse each log line
for line in logs:
    fields = line.split(",")

    part_code = fields[0].strip()
    diameter = float(fields[1].strip())
    shift = fields[2].strip()

    diameters.append(diameter)

    print(part_code, diameter, shift)

# Calculate report
print("\n===== SHIFT REPORT =====")

print("Total parts:", len(diameters))
print("Average diameter:", sum(diameters) / len(diameters))
print("Minimum diameter:", min(diameters))
print("Maximum diameter:", max(diameters))

it-8
# 10 messy log lines
logs = [
    "P101   25.4   A",
    "P102  30.2 B",
    "P103    18.7    C",
    "P104 22.5 D",
    "P105     27.8 E",
    "P106  31.0    F",
    "P107   19.6 G",
    "P108  24.3     H",
    "P109 29.7 I",
    "P110    21.5    J"
]

# Three separate bins
accepted = []
rework = []
scrap = []

# Store the part codes that are scrapped
scrap_parts = []

# Parse and classify each log
for line in logs:
    parts = line.split()

    part_code = parts[0]
    diameter = float(parts[1])

    # Example diameter rules:
    # 22 <= diameter <= 28: accepted
    # 20 <= diameter < 22 or 28 < diameter <= 30: rework
    # Otherwise: scrap
    if 22 <= diameter <= 28:
        accepted.append(diameter)

    elif 20 <= diameter < 22 or 28 < diameter <= 30:
        rework.append(diameter)

    else:
        scrap.append(diameter)
        scrap_parts.append(part_code)

# Counts
print("Accepted count:", len(accepted))
print("Rework count:", len(rework))
print("Scrap count:", len(scrap))

# Accepted average
if accepted:
    accepted_average = sum(accepted) / len(accepted)
    print("Accepted average:", accepted_average)
else:
    print("Accepted average: No accepted parts")

# Part codes that were scrapped
print("Scrapped part codes:", scrap_parts)

it6-
# Two Shifts Compared

day_logs = [
    "P001, 25.02, day",
    "P002, 25.08, day",
    "P003, 25.12, day",
    "P004, 24.98, day",
    "P005, 24.85, day"
]

night_logs = [
    "P001, 25.11, night",
    "P006, 25.00, night",
    "P007, 24.92, night",
    "P008, 25.15, night",
    "P009, 25.03, night"
]

# Function to inspect each shift
def inspect_shift(logs):

    accepted = 0
    rework = 0
    scrap = 0
    scrap_codes = []

    for line in logs:
        fields = line.split(",")

        code = fields[0].strip()
        diameter = float(fields[1].strip())

        if 24.95 <= diameter <= 25.05:
            accepted += 1

        elif 24.90 <= diameter <= 25.10:
            rework += 1

        else:
            scrap += 1
            scrap_codes.append(code)

    total = len(logs)

    accept_rate = (accepted / total) * 100

    print("Total parts:", total)
    print("Accepted:", accepted)
    print("Rework:", rework)
    print("Scrap:", scrap)
    print("Accept rate:", accept_rate, "%")

    return set(scrap_codes)


# Day shift report
print("\n===== DAY SHIFT =====")
day_scrap = inspect_shift(day_logs)

# Night shift report
print("\n===== NIGHT SHIFT =====")
night_scrap = inspect_shift(night_logs)

# Compare scrap lists using sets
print("\n===== SCRAP COMPARISON =====")

print("Scrap in both shifts:")
print(day_scrap & night_scrap)

print("Scrap unique to day shift:")
print(day_scrap - night_scrap)

print("Scrap unique to night shift:")
print(night_scrap - day_scrap)
