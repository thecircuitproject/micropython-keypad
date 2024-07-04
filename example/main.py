from keypad import Keypad

keypad_rows = [9, 8, 7, 6]
keypad_columns = [5, 4, 3, 2]


def main():
    keypad = Keypad(keypad_rows, keypad_columns)
    print("Please enter a key from the keypad")
    key = None
    while key != "*":
        if key := keypad.scankeys:
            print(f"You have pressed: {key}")


if __name__ == "__main__":
    main()
