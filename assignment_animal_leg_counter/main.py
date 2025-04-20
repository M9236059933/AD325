def count_four_legged(animals):
    four_legged = {'lion', 'deer', 'elephant', 'horse', 'dog', 'cat'}
    count = 0
    for animal in animals:
        if animal.lower() in four_legged:
            count += 1
    return count
