

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    total_amount = 0;
    for letter in skus:
        count = skus.count(letter)
        if(letter == 'A'):
            total_amount = (count // 3) * 130 + (count % 3) * 50
        elif(letter == 'B'):
            total_amount = (count//2) * 45 + (count % 2) * 30
        elif(letter == 'C') :
            total_amount = count * 20
        elif(letter == 'D'):
            total_amount = count * 15
        else:
            return -1
    return total_amount
    raise NotImplementedError()
