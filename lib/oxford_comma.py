def oxford_comma(items):
    print(items)
    #listItems = items.split()
    if len(items) == 1:
        return ' '.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        #The way it works is listed[-1] gets the last value from the list. 
        #We use = to assign this value to listed[-1][:-1], which is a slice of the last word from the list with everything before the last character.
        return ('{}, and {}'.format(', '.join(items[:-1]), items[-1]))