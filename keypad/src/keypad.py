import utime
from machine import Pin


class Keypad:
    matrix_keys = [
        ["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"],
    ]

    def __init__(self, rows, columns):
        self.rows = [Pin(row, Pin.OUT) for row in rows]
        self.columns = [Pin(col, Pin.IN, Pin.PULL_DOWN) for col in columns]
        self.rows_len = len(rows)
        self.cols_len = len(columns)
        self.initialize()

    def initialize(self):
        self._pin_values(self.rows, 0)
        self._pin_values(self.columns, 0)

    @property
    def scankeys(self):
        pressed_key = None
        for row in range(self.rows_len):
            self.rows[row].high()
            for col in range(self.cols_len):
                if self.columns[col].value() == 1:
                    pressed_key = self.matrix_keys[row][col]
                    utime.sleep(0.3)
            self.rows[row].low()
        return pressed_key

    def _pin_values(self, pins, value):
        for pin in pins:
            pin.value(value)
