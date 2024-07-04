# micropython-keypad

The Keypad library is designed to simplify keypad interfacing in Micropython-based hardware projects. Whether you’re working on a Raspberry Pi, ESP32, or any other Micropython-compatible board, this library provides an intuitive API for handling button presses and releases.

## Example usage

```python
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
```