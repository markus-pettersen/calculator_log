import os

# All functions abstracted out from the main code:
def calculator():
    """The main function. This function is called when calculator is selected
    from the menu. It prompts the user to input numbers and select an
    operation from a list. It then calls the corresponding function to
    calculate the result and then calls the log function to record the result 
    in a log file.
    """
    # Input the first number:
    # Use a while loop to repeat the code until a valid number is entered:
    while True:
        try:
            # If a number can be turned into a float, break out of the loop
            num_1 = float(input("Enter first number: "))
            break
        # Anticipated ValueError caught here. If user enters a non-float,
        # displays a warning and allows to retry:
        except ValueError:
            print("Not a valid number. Please try again.")
    # Input the second number:
    # Works in the same way as above    
    while True:
        try:
            num_2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Not a valid number. Please try again.")

    # Declare an empty display value here. Information can be assigned here
    # later in the loop (it has scope for the whole function)
    display = ""
    # Start a loop here. Will loop until a valid choice is selected:
    operation_selected = False
    while not operation_selected:
        # Operation menu presented to user here.
        # lower and strip to minimise errors
        operation = input('''Select Operation:
                 Add - 'a'
                 Subtract - 's'
                 Multiply - 'm'
                 Divide - 'd'
                 >>> ''').lower().strip()
        # each operation calls a different function.
        # assigns the result to the display variable and prints to the console
        # same procedure for each menu option:
        if operation == "a":
            display = addition(num_1, num_2)
            print(display)
            operation_selected = True
        elif operation == "s":
            display = subtraction(num_1, num_2)
            print(display)
            operation_selected = True
        elif operation == "m":
            display = multiplication(num_1, num_2)
            print(display)
            operation_selected = True
        elif operation == "d":
            display = division(num_1, num_2)
            print(display)
            operation_selected = True
        else: # Default case. Prints an error message and repeats:
            print("Invalid choice! Please try again...")
    # calls a function to log the result in a text file:
    log_result("log.txt", display)

# Each of the calculator functions below:
# Returns the string below. It is assigned to 'display' (shown above)

def addition(first, second):
    """Adds two numbers and returns a string with the full equation
    """
    answer = first + second
    return f"{first} + {second} = {answer}"

def subtraction(first, second):
    """Subtracts the second number from the first number and returns a string
    with the full equation
    """
    answer = first - second
    return f"{first} - {second} = {answer}"

def multiplication(first, second):
    """Multiplies the first number and the second number and returns a string
    with the full equation
    """
    answer = first * second
    return f"{first} × {second} = {answer}"

def division(first, second):
    """Divides the first number by the second number and returns a string with
    the full equation. Does not allow division by zero
    """
    # Anticipated division by zero error
    # Can be caught without a try-except block:
    if second == 0:
        return f"{first} ÷ {second} - Cannot divide by 0!"
    else:
        answer = first / second
        return f"{first} ÷ {second} = {answer}"

def log_result(a_file, a_string):
    """If a_file does not already exist, creates the calculation log file and
    writes the string to the file. If a_file does exist, opens the file in
    append mode and appends a_string to the file
    """
    # First checks if the log file exists using os module:
    if not os.path.exists(a_file):
        # If the log doesn't exists, creates it and writes the title and
        # the first calculation
        with open(a_file, "w", encoding="UTF-8-SIG") as my_log:
            my_log.write(f"Calculation log\n{a_string}\n")
    else:
        # If the log exists, opens it in append mode and appends the most
        # recent calculation to the end
        with open(a_file, "a", encoding="UTF-8-SIG") as my_log:
            my_log.write(a_string + "\n")

def load_log():
    """ Loads the log file and prints the contents of the file to the
    console. If the log file does not exist, display an error message.
    """
    
    # Anticipated error. Checks if the log exists before trying to open it:
    if os.path.exists("log.txt"):
        # An empty variable to add the contents to
        log_lines = ""
        # Open the file and iterate through the file, adding the lines to the
        # variable
        with open("log.txt", "r", encoding="UTF-8-SIG") as my_log:
            for line in my_log:
                log_lines += line
        # Prints the lines to the console:
        print(log_lines)
        # returns the lines because they are needed for the export function
        return log_lines
    else:
        # Prints error message if file does not exist:
        print("No log detected!")

def clear_log():
    """Checks if the log file exists. If it does, it deletes the log, if it
    does not, displays an error message
    """

    # Checks if the log exists
    if os.path.exists("log.txt"):
        # deletes the log and prints a confirmation message:
        os.remove("log.txt")
        print("Log successfully cleared")
    else:
        # If the log doesn't exist, prints a message
        print("No log found!")

def export_log():
    """Takes the contents of the log.txt file (if it exists) and allows the
    user to save it to a newly created file with a their chosen name
    """

    # Anticipated error. Check if log exists before trying to export
    if not os.path.exists("log.txt"):
        print("No log to export!")
        return
    # Calls the load_log function to find the contents of the log and
    # store in a variable:
    contents = load_log()
    # Prompts the user to give the file a name strip out white space.
    user_filename = input("Save log as: ").strip()
    # Add the file extension to the end:
    filename = user_filename + ".txt"
    # write the contents of the log to a new file with the given name:
    with open(filename, "w", encoding="UTF-8-SIG") as export_log:
        export_log.write(contents)
    # Prints confirmation to the console:
    print("Log successfully exported")

def import_log():
    """Opens a previously exported log file and displays the contents to the
    console
    """

    # Prompts the user to enter the name of the log to view:
    user_import_name = input("Enter file to import: ").strip()
    # Adds the file extension:
    filename = user_import_name + ".txt"
    # Sets up a variable to add to:
    file_contents = ""
    # Creates a flag that changes to true if a file has been opened:
    file_open = False
    # Try-except-finally block. Catches errors if the file name is wrong:
    try:
        # Tries to open the file and print out the contents:
        new_log = open(filename, "r", encoding="UTF-8-SIG")
        for line in new_log:
            file_contents += line
        print(file_contents)
        # If the code reaches this point, a file has been opened and needs to
        # be closed, so set this flag to true:
        file_open = True
    except FileNotFoundError as error:
        # Tells the user that the file was not found and prints the error:
        print("File not found")
        print(error)
    finally:
        # If the file was opened, it needs to close:
        if file_open:
            new_log.close()

#############
# Main Menu #
#############
# Main menu shown to the user at start:
# User selects an option which calls one of the above functions:
print("Simple Calculator")
while True:
    main_menu = input('''Main Menu:
            Calculator - 'c'
            View log - 'vl'
            Clear log - 'cl'
            Export log - 'el'
            View exported log - 'vel'
            Exit - 'e'
            >>> ''').lower() 
    if main_menu == "c":
        calculator()
    elif main_menu == "vl":
        load_log()
    elif main_menu == "cl":
        clear_log()
    elif main_menu == "el":
        export_log()
    elif main_menu == "vel":
        import_log()
    elif main_menu == "e":
        print("Goodbye")
        exit()
    else:
        print("Invalid selection!")