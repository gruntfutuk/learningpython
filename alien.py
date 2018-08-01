alien = [{'color' : 'green', 'points' : 6, 'speed' : 'fast'} for _ in range(10)]
alien.extend([{'color' : 'green', 'points' : 5, 'speed' : 'medium'}
                          for _ in range(20)])
print(*alien, sep="\n")
