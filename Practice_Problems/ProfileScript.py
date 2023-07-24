import cProfile

def sum():
    return 1 + 2

cProfile.run('sum()') 