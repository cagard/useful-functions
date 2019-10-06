import pandas as pd

def xlsheets(file):
    """The function takes a string, *file*, and returns the number and names of sheets in that file.\
    The function relies on the pandas package."""
    tmp = pd.ExcelFile(file)
    res = {'names': tmp.sheet_names,'num_sheets':len(tmp.sheet_names)}
    return res
