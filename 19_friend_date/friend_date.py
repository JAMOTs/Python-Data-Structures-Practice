def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
       # Unpack the hobby lists from each friend's tuple
    hobbies_a = a[2]
    hobbies_b = b[2]

    # Check for common hobbies
    for hobby in hobbies_a:
        if hobby in hobbies_b:
            return True

    # If no common hobbies were found, return False
    return False