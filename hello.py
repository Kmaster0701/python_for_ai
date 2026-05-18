#Requirements.txt file have the required lib for a certain project. can be installed into a project using pip install -r requirement.txt
#Pip free used to saves the libraries that have been used in a project on a requirements.txt file

try:
    # Read a number from a file
    with open('number.txt', 'r') as f:
        text = f.read()
    number = int(text)
    result = 100 / number
    print(f"Result: {result}")
except FileNotFoundError:
    print("Could not find number.txt")
except ValueError:
    print("File doesn't contain a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
