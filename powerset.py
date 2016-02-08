# powerset.py

def powerset(values):
    result = [[]]
    for value in values:
        result.extend([subset + [value] for subset in result])
    return result

print powerset([1,2,3])

