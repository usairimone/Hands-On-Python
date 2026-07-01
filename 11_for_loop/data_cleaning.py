# You are given a list containing mixed data types (strings, floats, integers, and booleans). Write a for loop to filter out all boolean values. Convert any numeric strings into actual integers. Multiply all resulting numbers by 2 and store them in a new list.


data = [10, "20", True, 3.5, False, "apple"]

def clean_cast():
    result = []
    for i in data:
        # remove boolean values.
        if type(i) is bool:
            continue

        # convert numeric strings to int.
        if isinstance(i, str):
            if i.isdigit():
                i = int(i)
            else:
                continue

        # keep only numeric values.
        if isinstance(i, (int, float)):
            result.append(i * 2)

    return result

def main():
    try:
        print(clean_cast())
    # handles the invalid input.
    except:
        print("Invalid input! Pleaase enter the valid input.")
    
# starting point of the program.
if __name__ == "__main__":
    main()