

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    found_A = false
    found_B = false
    found_C = false
    found_D = false
    total_amount = 0
    for letter in skus:
        count = skus.count(letter)
        if(letter == 'A' and found_A == false):
             total_amount = total_amount + (int((count / 3)) * 130) + ((count % 3) * 50)
             found_A = true
        elif(letter == 'B' and found_B == false):
            total_amount = total_amount + (int((count / 2)) * 45) + ((count % 2) * 30)
            found_B = true
        elif(letter == 'C' and found_C == false) :
            total_amount = total_amount + count * 20
            found_C = true
        elif(letter == 'D'and found_D == false):
            total_amount =  total_amount + count * 15
            found_D = true
        else:
            return -1
    return total_amount
    raise NotImplementedError()
