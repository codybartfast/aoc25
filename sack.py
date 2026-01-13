from pathlib import Path
import sys

def get_input(input_filename = None):
    if input_filename == None:
        input_filename = "input"    
    filepath = sys._getframe(1).f_code.co_filename
    day = filepath[-5:-3]
    input_path = Path(__file__).resolve().parent / "input" / "2025"
    input_path = input_path / f"day{day}" / f"{input_filename}.txt"
    with open(input_path, encoding="utf-8") as f:
         input = f.read()
    return input 
