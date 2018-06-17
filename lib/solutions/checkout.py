

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A' : (50 ,0 ), 'B' : (30, 0), 'C' : (20, 0), 'D' : (15,0), 'E' : (40,0), 'F' : (10,0) ,
             'G' : (20,0) ,'H' : (10, 0), 'I' : (35, 0) ,'J' : (60, 0) , 'K' : (80, 0) , 'L' : (90,0),
              'M': (15,0) , 'N' : (40, 0) , 'O' : (10, 0), 'P' :(50, 0) , 'Q' : (30, 0) , 'R' :(50,0) ,
              'S': (30,0), 'T' :(20,0), 'U' : (40,0) , 'V' : (50, 0), 'W' : (20,0), 'X' : (90, 0), 'Y': (10,0),
              'Z': (50,0)}
    total_amount = 0
    for letter in skus:
        count = skus.count(letter)
        if(letter == 'A'):
            if(prices.get(letter)[1] == 0):
                total_amount = total_amount + (int((count / 5)) * 200) + (int((count % 5)/3) * 130) +\
                               (int((count % 5 ) % 3)) * prices.get(letter)[0]
                prices.get(letter)[1] = count
        elif(letter == 'B'):
            if(prices.get(letter)[1] == 0):
                prices.get('E')[1]= skus.count('E')
                count_E = prices.get('E')[1]
                if (count_E >= 2) :
                    final_count = count - (int(count_E / 2))
                    if final_count < 0:
                        final_count = 0
                    total_amount = total_amount + (int((final_count / 2)) * 45) + \
                                   ((final_count % 2) * prices.get(letter)[0]) + count_E * prices.get('E')[0]
                else:
                    total_amount = total_amount + (int(count / 2) * 45) + (count % 2) * prices.get(letter)[0] + \
                                   count_E * prices.get('E')[0]
                prices.get(letter)[1] = count
                prices.get('E')[0] = count_E
        elif(letter in 'CDGIJLOSTWXYZ'):
            if(prices.get(letter)[1] == 0) :
                total_amount = total_amount + count * prices.get(letter)[0]
                prices.get(letter)[1] = count
        elif(letter == 'E'):
            if (prices.get(letter)[1] == 0):
                count_B = skus.count('B')
                if (count >= 2):

                    final_count = count_B - int(count/2)
                    if (final_count < 0):
                        final_count = 0
                    total_amount = total_amount + count * prices.get(letter)[0] + (int((final_count / 2)) * 45) + \
                                   ((final_count % 2) * prices.get('B')[0])
                else:
                    total_amount = total_amount + count * 40
                prices.get(letter)[1] = count
                prices.get('B')[1] = count_B
        elif(letter == 'F'):
            if (prices.get(letter)[1] == 0):
                if( count % 2 == 0 and count >= 2) :
                    total_amount = total_amount + count * prices.get(letter)[0] - (int(count / 2) - 1 ) * prices.get(letter)[0]
                elif ( count < 2) :
                    total_amount = total_amount + count * prices.get(letter)[0]
                else:
                    total_amount = total_amount + count * prices.get(letter)[0] - (count % 2) * prices.get(letter)[0]
                prices.get(letter)[1] = count
        elif (letter == 'H'):
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/10) * 80 + + (int((count % 10)/5) * 45) + \
                             (int((count % 10 ) % 5)) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif letter == 'K':
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/2) * 150 + (count % 2) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif letter == 'P':
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/5) * 200 + (count % 5) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif letter == 'V':
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/3) * 130 + (int((count % 3)/2) * 90) + \
                             (int((count % 3 ) % 2)) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif(letter == 'U'):
            if (prices.get(letter)[1] == 0):
                if( count % 3 == 0 and count >= 3) :
                    total_amount = total_amount + count * prices.get(letter)[0] - (int(count / 3) - 1 ) * prices.get(letter)[0]
                elif ( count < 3) :
                    total_amount = total_amount + count * prices.get(letter)[0]
                else:
                    total_amount = total_amount + count * prices.get(letter)[0] - (count % 3) * prices.get(letter)[0]
                prices.get(letter)[1] = count

        else:
            return -1
    return total_amount
    raise NotImplementedError()
