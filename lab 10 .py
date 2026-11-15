it 12- 

import os
import sys

def main():
    try:
        # 1. Use a relative path
        file_path = os.path.join("data", "input.txt")

        # Create the folder and sample file if missing
        os.makedirs("data", exist_ok=True)

        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Hello World!\nThis is the input file.")

        # Read the file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print("File read successfully!")
        print(content)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except OSError as error:
        print("File operation error:", error)

    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()

it 10-


import os

# Create project folders
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# Create sample input file
input_file = "data/input.txt"

with open(input_file, "w", encoding="utf-8") as f:
    f.write("Welcome to IT10 Project!\n")
    f.write("README and Tidy Exercise.\n")
    f.write("Python file handling example.")

# Read input file
try:
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    print("Input file read successfully!")

    # Generate output file
    output_file = "reports/output.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("IT10 Project Output\n")
        f.write("-------------------\n")
        f.write(content)

    print("Output file created successfully!")

    # Generate README file
    readme = """# IT10 - README & Tidy

## Project Description
A simple Python project demonstrating file handling
and repository organization.

## Folder Structure
- main.py
- README.md
- data/input.txt
- reports/output.txt

## How to Run
Run the following command:

python main.py

## Sample Input
data/input.txt

## Output
reports/output.txt
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("README.md created successfully!")
    print("Project organized successfully!")

except FileNotFoundError:
    print("Error: Input file not found.")

except PermissionError:
    print("Error: Permission denied.")

except OSError as error:
    print("File error:", error)

it 8-

git add .
git commit -m "Final project release"
git tag -a v1.0 -m "Version 1.0"
git push origin main
git push origin v1.0

output-
Final commit created successfully.
Version tag v1.0 created successfully.
Project pushed to GitHub.
Release v1.0 published successfully.

Result: Project successfully published.


it 6- 


import os

# Create required folders
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)


# Create sample input
def create_sample():
    with open("data/input.txt", "w", encoding="utf-8") as file:
        file.write("Apple\n")
        file.write("Banana\n")
        file.write("Orange\n")


# Process input data
def process_data():
    try:
        with open("data/input.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        items = [line.strip() for line in lines if line.strip()]
        report = "Sample Report\n"
        report += "-------------\n"
        report += f"Total items: {len(items)}\n"

        for item in items:
            report += f"- {item}\n"

        return report

    except FileNotFoundError:
        return "Error: Input file not found."


# Test function with normal and hostile inputs
def run_tests():
    print("Running tests...")

    # Normal input test
    result = process_data()
    assert "Total items: 3" in result
    print("Test 1 passed: Normal input")

    # Hostile input test
    with open("data/input.txt", "w", encoding="utf-8") as file:
        file.write("\n\n")

    result = process_data()
    assert "Total items: 0" in result
    print("Test 2 passed: Empty input")

    print("All tests passed!")


# Main program
def main():
    create_sample()

    report = process_data()

    # Save sample report
    with open("reports/example_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("\nReport generated successfully!")
    print(report)

    # Create README
    readme = """# IT6 - The Handover Pack

## Project Description
A simple Python tool to read input data and
generate reports.

## How to Run
python main.py

## How to Test
python main.py --test

## Sample Report
reports/example_report.txt

## Limitations
- Supports only text input files.
- Does not support Excel or PDF files.
- Does not use a database.
- Does not provide a graphical interface.
- Requires Python 3 to run.
"""

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme)

    print("README.md created successfully!")


if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        create_sample()
        run_tests()
    else:
        main()