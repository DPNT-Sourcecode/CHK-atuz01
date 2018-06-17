

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    found_A = 0
    found_B = 0
    found_C = 0
    found_D = 0
    total_amount = 0
    for letter in skus:
        count = skus.count(letter)
        if(letter == 'A'):
            if(found_A == 0):
                total_amount = total_amount + (int((count / 3)) * 130) + ((count % 3) * 50)
                found_A = 1
        elif(letter == 'B'):
            if(found_B == 0):
                total_amount = total_amount + (int((count / 2)) * 45) + ((count % 2) * 30)
                found_B = 1
        elif(letter == 'C'):
            if(found_C == 0) :
                total_amount = total_amount + count * 20
                found_C = 1
        elif(letter == 'D'):
            if(found_D == 0):
                total_amount =  total_amount + count * 15
                found_D = 1
        else:
            return -1
    return total_amount
    raise NotImplementedError()
