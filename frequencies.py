"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    

    for item in items:

        if item in frequencies:
            frequencies[item] += 1

        else:
            frequencies[item] = 1
            
    
    return frequencies





frequencies([50,50, 60, 70, 100, 100, 100, 30])