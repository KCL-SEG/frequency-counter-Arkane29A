"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    items2 = []
    frequencies = {}
    

    for item in items:

        if item == str:
            items2.append(item)
        else:
            items2.append(str(item))

    for item in items2:

        if item in frequencies:
            frequencies[item] += 1

        else:
            frequencies[item] = 1
            
    
    return frequencies








