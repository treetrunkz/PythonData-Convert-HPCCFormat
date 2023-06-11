# dUnder.py
# A dunder file leverages classes and lists to assign 
# any csv as a matrix, a memory address for every value.

import csv

from typing import List

def load_csv():
    with open('1k.csv') as f:
        return [row for row in csv.reader(f)]

def clean_csv(rows: List[List[str]]) -> List[List[str]]:
    return [list(map(str.strip, row)) for row in rows]

class CsvRdr:
    def __init__(self, data:List[List[str]]):
        self.data = data
    
    def cell(self, row: int, col:int) -> str:
        return self.data[row][col]

    def __getitem__(self, row):
        return self.data[int(row)]

    def __call__(self, row: int, col: int) -> str:
        return self.cell(row, col)

if __name__ == '__main__':
    raw_data = load_csv()
    clean_data = clean_csv(raw_data)
    reader = CsvRdr(clean_data)


