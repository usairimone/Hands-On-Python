data = [10, "20", True, 3.5, False, "apple"]

# clean and process data.
def clean_cast():
    result = []
    
    # iterate through data.
    for i in data:
        
        # skip boolean values.
        if type(i) is bool:
            continue

        # convert numeric strings.
        if isinstance(i, str):
            if i.isdigit():
                i = int(i)
            else:                
                # skip non numeric strings.
                continue

        # keep and double numeric values.
        if isinstance(i, (int, float)):
            result.append(i * 2)

    return result

def main():
    try:
        # display processed data.
        print(clean_cast())
    # handle invalid input.
    except:
        print("Invalid input! Pleaase enter the valid input.")
    
# check program entry point.
if __name__ == "__main__":
    main()