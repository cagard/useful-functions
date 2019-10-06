
import pandas as pd
import numpy as np
import os

def xlcolshape(file):
    """xlcolshape takes a file name as a string and returns the shape of the excel file"""
    return pd.read_excel(file).shape


def xluniquecol2(file, header=0):
    tmp = []
    for sheet in pd.ExcelFile(file).sheet_names:
        if (('species' in pd.read_excel(file, sheet_name=sheet, header=header).columns) \
                or ('Species' in pd.read_excel(file, sheet_name=sheet, header=header).columns)):
            try:
                tmp = list(set(tmp + list(pd.read_excel(file, sheet_name=sheet).columns)))
                print("Doing stuff you asked me to do for file \'{}\',sheet \'{}\' programmer person." \
                      .format(file, sheet))
                res = tmp
            except:
                print("This didn't work for file {}, sheet {}".format(file, sheet))
        else:
            print("Check columns for file {}.".format(file))
            res = None
    return res

def colmatchtodict(x, series, dictsource, key=None):
    """This takes a string, x, and a looks for values in a series that match that contain that string.
    Those values which match are returned as values in a python dict for the key, key."""

    assert isinstance(series, pd.Series)
    if key is None:
        key = x
    tmp = series[series.astype(str).str.contains(x, case=False)].tolist()
    dictsource[key] = tmp
    return dictsource

def findsyn (name,dictionary, verbose = True):
    """
    *findsyn* checks searches the values of the dict *dictionary* for the string, *name* and returns
    the key for the key,value pair to which *name* belongs.
    """
    tmp = pd.DataFrame({'preferredcol':list(dictionary.keys()),'synonymns':list(dictionary.values())})
    try:
        res = list(tmp.preferredcol[tmp.synonymns.apply(lambda x:name in x)])[0]
    except:
        res = None
        if verbose == True:
            print("No value matching \"{}\" was found in the dictionary.".format(name))
    return res

def readnclean(x, dictionary, dtype=None):
    """
    This function reads an excel file, renames columns deemed synonymous according to a dict,
    *dictionary*, and drops unnecessary columns before returning the cleaner dataframe.
    """
    tmp = pd.read_excel(x, dtype=dtype)
    tmp.columns = pd.Series(tmp.columns).map(lambda x: dictionary[x])
    dropidx = [None == col for col in list(tmp.columns)]
    tmp = tmp.drop(columns=tmp.columns[dropidx])

    return tmp
