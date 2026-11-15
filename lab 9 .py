it 12- 
import os

# Create the data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Create 15 shift log records, including 3 deliberately faulty records
records = [
    "WO01,Employee: Rahul,Shift: Morning,Hours: 8",
    "WO02,Employee: Amit,Shift: Evening,Hours: 7",
    "WO03,Employee: Priya,Shift: Night,Hours: 8",
    "WO04,Employee: Neha,Shift: Morning,Hours: 6",
    "WO05,Employee: Ravi,Shift: Evening,Hours: 8",
    "WO06,Employee: Sita,Shift: Night,Hours: 7",
    "WO07,Employee: Karan,Shift: Morning,Hours: 8",

    # Three deliberately filthy (invalid) records
    "WO08,Employee: ,Shift: Morning,Hours: 8",       # Missing employee
    "WO09,Employee: Aman,Shift: Unknown,Hours: -5",  # Invalid shift and hours
    "WO10,Employee: Riya,Shift: Night,Hours: abc",   # Non-numeric hours

    "WO11,Employee: Arjun,Shift: Morning,Hours: 8",
    "WO12,Employee: Meena,Shift: Evening,Hours: 6",
    "WO13,Employee: Dev,Shift: Night,Hours: 7",
    "WO14,Employee: Pooja,Shift: Morning,Hours: 8",
    "WO15,Employee: Sanjay,Shift: Evening,Hours: 5"
]

# Write records to the file
with open("data/shift_log.txt", "w", encoding="utf-8") as file:
    for record in records:
        file.write(record + "\n")

# Read the file back and count the lines
with open("data/shift_log.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("Contents of shift_log.txt:")
print("".join(lines))

print("Total line count:", len(lines))

it 10- 

import os
import csv
from collections import defaultdict

os.makedirs("data", exist_ok=True)

valid = []
rejects = []
summary = defaultdict(lambda: [0, 0.0])

# Read and validate
with open("data/shift_log.txt", encoding="utf-8") as f:
    lines = f.readlines()

for n, line in enumerate(lines, 1):
    try:
        p = [x.strip() for x in line.strip().split(",")]
        if len(p) != 4:
            raise ValueError("Invalid fields")

        wo = p[0]
        emp = p[1].split(":", 1)[1].strip()
        shift = p[2].split(":", 1)[1].strip()
        hours = float(p[3].split(":", 1)[1].strip())

        if not wo or not emp:
            raise ValueError("Missing work order or employee")
        if shift not in ("Morning", "Evening", "Night"):
            raise ValueError("Invalid shift")
        if not 0 < hours <= 24:
            raise ValueError("Invalid hours")

        valid.append((wo, emp, shift, hours))
        summary[shift][0] += 1
        summary[shift][1] += hours

    except (ValueError, IndexError) as e:
        rejects.append([n, line.strip(), str(e)])

# Write report
with open("data/report.txt", "w", encoding="utf-8") as f:
    f.write(f"{'Work Order':<12}{'Employee':<20}{'Shift':<12}{'Hours':>6}\n")
    f.write("-" * 50 + "\n")
    for wo, emp, shift, hours in valid:
        f.write(f"{wo:<12}{emp:<20}{shift:<12}{hours:>6.2f}\n")

    f.write("\nSHIFT SUMMARY\n")
    for shift, (count, hours) in sorted(summary.items()):
        f.write(f"{shift}: {count} records, {hours:.2f} hours\n")

# Write rejected rows
with open("data/rejects.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Line", "Rejected Record", "Reason"])
    w.writerows(rejects)

print("Input lines:", len(lines))
print("Accepted:", len(valid))
print("Rejected:", len(rejects))
print("Created data/report.txt and data/rejects.csv")


it 8-

import re

# OLD VERSION (split parsing) — kept for comparison
# parts = [x.strip() for x in line.strip().split(",")]
# wo = parts[0]
# emp = parts[1].split(":", 1)[1].strip()
# shift = parts[2].split(":", 1)[1].strip()
# hours = float(parts[3].split(":", 1)[1].strip())
# Note: The regex version survived more spacing variations in testing.

# NEW VERSION: regex parsing
pattern = re.compile(
    r"^\s*(WO\d{2})\s*,\s*Employee:\s*(.*?)\s*,"
    r"\s*Shift:\s*(Morning|Evening|Night)\s*,"
    r"\s*Hours:\s*(\d+(?:\.\d+)?)\s*$"
)

def parse_record(line):
    match = pattern.fullmatch(line)
    if not match:
        raise ValueError("Invalid record format")

    wo, emp, shift, hours = match.groups()

    if not emp:
        raise ValueError("Missing employee name")

    hours = float(hours)
    if not 0 < hours <= 24:
        raise ValueError("Invalid hours")

    return wo, emp, shift, hours


# Test
with open("data/shift_log.txt", encoding="utf-8") as f:
    lines = f.readlines()

valid = []
rejects = []

for n, line in enumerate(lines, 1):
    try:
        valid.append(parse_record(line))
    except ValueError as e:
        rejects.append((n, line.strip(), str(e)))

print("Total lines:", len(lines))
print("Accepted:", len(valid))
print("Rejected:", len(rejects))

with open("data/rejects.csv", "w", encoding="utf-8") as f:
    f.write("Line,Rejected Record,Reason\n")
    for n, line, reason in rejects:
        f.write(f'{n},"{line}","{reason}"\n')

with open("data/report.txt", "w", encoding="utf-8") as f:
    f.write(f"{'Part Code':<12}{'Employee':<20}{'Shift':<12}{'Hours':>6}\n")
    f.write("-" * 50 + "\n")
    for wo, emp, shift, hours in valid:
        f.write(f"{wo:<12}{emp:<20}{shift:<12}{hours:>6.2f}\n")

print("Report and rejects files created.")


it 6- 

import os
import re
import csv
from datetime import datetime
from collections import defaultdict

folder = "data"
os.makedirs(folder, exist_ok=True)

pattern = re.compile(
    r"^\s*(WO\d{2})\s*,\s*Employee:\s*(.*?)\s*,"
    r"\s*Shift:\s*(Morning|Evening|Night)\s*,"
    r"\s*Hours:\s*(\d+(?:\.\d+)?)\s*$"
)

valid = []
rejects = []
plant = defaultdict(lambda: [0, 0.0])

# Read ONLY the original input file
input_file = os.path.join(folder, "shift_log.txt")

with open(input_file, encoding="utf-8") as f:
    lines = f.readlines()

# Parse and validate
for n, line in enumerate(lines, 1):
    match = pattern.fullmatch(line.strip())

    try:
        if not match:
            raise ValueError("Invalid record format")

        wo, emp, shift, hours = match.groups()
        hours = float(hours)

        if not emp:
            raise ValueError("Missing employee")
        if not 0 < hours <= 24:
            raise ValueError("Invalid hours")

        valid.append((wo, emp, shift, hours))
        plant[shift][0] += 1
        plant[shift][1] += hours

    except ValueError as e:
        rejects.append([n, line.strip(), str(e)])

# Write human report
with open(os.path.join(folder, "report.txt"), "w", encoding="utf-8") as f:
    f.write(f"{'Work Order':<12}{'Employee':<20}{'Shift':<12}{'Hours':>6}\n")
    f.write("-" * 50 + "\n")

    for wo, emp, shift, hours in valid:
        f.write(f"{wo:<12}{emp:<20}{shift:<12}{hours:>6.2f}\n")

    f.write("\nPLANT SUMMARY\n")
    for shift, (count, hours) in sorted(plant.items()):
        f.write(f"{shift}: {count} records, {hours:.2f} hours\n")

    f.write(f"\nAccepted: {len(valid)}\nRejected: {len(rejects)}\n")

# Write rejected records
with open(os.path.join(folder, "rejects.csv"), "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Line", "Rejected Record", "Reason"])
    writer.writerows(rejects)

# Append run history
history = os.path.join(folder, "run_history.csv")
new_file = not os.path.exists(history) or os.path.getsize(history) == 0

with open(history, "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    if new_file:
        writer.writerow(["Timestamp", "File Name", "Records Processed", "Rejects"])

    writer.writerow([
        datetime.now().isoformat(timespec="seconds"),
        "shift_log.txt",
        len(valid),
        len(rejects)
    ])

print("Processing complete.")
print("Input lines:", len(lines))
print("Accepted records:", len(valid))
print("Rejected records:", len(rejects))
print("Created report.txt, rejects.csv, and updated run_history.csv")