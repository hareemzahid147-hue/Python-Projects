                     # STUDENTS RESULTS GENERATOR


# Importing libraries
from tabulate import tabulate
import csv


# Defining the main function
def main():
    students = []
    sn = 0

    # Creating a csv file
    create_csv()
    # Looping for user input (name, marks)
    while True:
        try:
            name = input("Name: ").capitalize().strip()
            mark = int(input("Marks: "))
            if not (65 >= mark >= 0):
                raise ValueError
            sn += 1
            students.append((sn, name, mark))
        except ValueError:
            print("Wrong Input! Try Again")
            continue
        # When Ctrl D pressed loop terminates
        except EOFError:
            print()
            break

    # Appending csv file
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        for sn, name, mark in students:
            result = pass_fail(percentage(mark))
            writer.writerow([sn, name, percentage(mark), result, emoji(result)])

    # Creating table of students
    create_table()


# Converts marks to percentage
def percentage(n):
    return f"{round(n / 65 * 100)}%"


# Checks whether a student passed or failed
def pass_fail(p):
    p = p.replace("%", "")
    if int(p) >= 50: return f"PASS"
    else: return f"FAIL"


# Generates emoji
def emoji(text):
    if text == "PASS":
        return "👍"
    else:
        return "👎"


# Creates a csv file
def create_csv():
     with open("data.csv", mode="w", newline="") as file:
         writer = csv.writer(file)
         writer.writerow(["Sn.", "Name:", "Percentage:", "Result:", "Emoji:"])


# Creates a tabe
def create_table():
    with open("data.csv") as file:
        csv_reader = csv.DictReader(file)
        print(tabulate(csv_reader, headers="keys", tablefmt="psql"))


# Calling the main function
if __name__ == "__main__":
    main()
