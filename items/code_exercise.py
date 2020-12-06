def permutations(string):
    """
    Create all permutations of a string with non-repeating characters
    """
    permutation_list = []
    if len(string) == 1:
        return [string]
    else:
        for char in string:
            [permutation_list.append(char + a) for a in permutations(string.replace(char, "", 1))]
    return list(set(permutation_list))



print(permutations('aabb'))
