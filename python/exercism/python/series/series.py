#! /usr/bin/env python

def slices(series, length):
    
    s = str(series)
    diff = len(s) - length

    if not 0 <= diff < len(s):
        raise ValueError("Requested length must be less than the length of the series")
    
    return [s[i:i+length] for i in range(0, diff+1)] 
