

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A' : [50 ,0 ], 'B' : [30, 0], 'C' : [20, 0], 'D' : [15,0], 'E' : [40,0], 'F' : [10,0] ,
             'G' : [20,0] ,'H' : [10, 0], 'I' : [35, 0] ,'J' : [60, 0] , 'K' : [70, 0] , 'L' : [90,0],
              'M': [15,0] , 'N' : [40, 0] , 'O' : [10, 0], 'P' :[50, 0] , 'Q' : [30, 0] , 'R' :[50,0] ,
              'S': [20,0], 'T' :[20,0], 'U' : [40,0] , 'V' : [50, 0], 'W' : [20,0], 'X' : [17, 0], 'Y': [20,0],
              'Z': [21,0]}
    total_amount = 0
    for letter in skus:
        count = skus.count(letter)
        if(letter == 'A'):
            if(prices.get(letter)[1] == 0):
                total_amount = total_amount + (int((count / 5)) * 200) + (int((count % 5)/3) * 130) +\
                               (int((count % 5) % 3)) * prices.get(letter)[0]
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
        elif(letter in 'CDGIJLO'):
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
                    total_amount = total_amount + count * prices.get(letter)[0]
                prices.get(letter)[1] = count
                prices.get('B')[1] = count_B
        elif(letter == 'F'):
            if (prices.get(letter)[1] == 0):
                if( count % 2 == 0 and count >= 2) :
                    total_amount = total_amount + count * prices.get(letter)[0] - (int(count / 2) - 1) * prices.get(letter)[0]
                elif ( count < 2) :
                    total_amount = total_amount + count * prices.get(letter)[0]
                else:
                    total_amount = total_amount + count * prices.get(letter)[0] - (count % 2) * prices.get(letter)[0]
                prices.get(letter)[1] = count
        elif (letter == 'H'):
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/10) * 80 + + (int((count % 10)/5) * 45) + \
                             (int((count % 10) % 5)) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif letter == 'K':
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/2) * 120 + (count % 2) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif letter == 'P':
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/5) * 200 + (count % 5) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif letter == 'V':
            if(prices.get(letter)[1] == 0):
              total_amount = total_amount + int(count/3) * 130 + (int((count % 3)/2) * 90) + \
                             (int((count % 3) % 2)) * prices.get(letter)[0]
            prices.get(letter)[1] = count
        elif(letter == 'U'):
            if (prices.get(letter)[1] == 0):
                if count < 3:
                    total_amount = total_amount + count * prices.get(letter)[0]
                else:
                    if( count % 3 == 0) :
                        total_amount = total_amount + count * prices.get(letter)[0] - (int(count / 3) - 1) * prices.get(letter)[0]
                    else:
                        total_amount = total_amount + count * prices.get(letter)[0] - (int(count/4)) * prices.get(letter)[0]
                prices.get(letter)[1] = count
        elif letter == 'M':
            if(prices.get(letter)[1] == 0):
                prices.get('N')[1] = skus.count('N')
                count_N = prices.get('N')[1]
                if (count_N >= 3) :
                    final_count = count - (int(count_N / 3))
                    if final_count < 0:
                        final_count = 0
                    total_amount = total_amount + final_count * prices.get(letter)[0] + count_N * prices.get('N')[0]
                else:
                    total_amount = total_amount + count * prices.get(letter)[0] + count_N * prices.get('N')[0]
                prices.get(letter)[1] = count
                prices.get('N')[0] = count_N
        elif letter == 'N':
            if (prices.get(letter)[1] == 0):
                count_M = skus.count('M')
                if (count >= 3):

                    final_count = count_M - int(count/3)
                    if (final_count < 0):
                        final_count = 0
                    total_amount = total_amount + count * prices.get(letter)[0] + prices.get('M')[0] * final_count
                else:
                    total_amount = total_amount + count * prices.get(letter)[0] + count_M * prices.get('M')[0]
                prices.get(letter)[1] = count
                prices.get('M')[1] = count_M
        elif letter == 'Q':
            if(prices.get(letter)[1] == 0):
                prices.get('R')[1]= skus.count('R')
                count_R = prices.get('R')[1]
                if (count_R >= 3) :
                    final_count = count - (int(count_R / 3))
                    if final_count < 0:
                        final_count = 0
                    total_amount = total_amount + (int((final_count / 3)) * 80) + \
                                   ((final_count % 3) * prices.get(letter)[0]) + count_R * prices.get('R')[0]
                else:
                    total_amount = total_amount + (int(count / 3) * 80) + (count % 3) * prices.get(letter)[0] + \
                                   count_R * prices.get('R')[0]
                prices.get(letter)[1] = count
                prices.get('R')[0] = count_R
        elif letter =='R':
            if (prices.get(letter)[1] == 0):
                count_Q = skus.count('Q')
                if (count >= 3):

                    final_count = count_Q - int(count / 3)
                    if (final_count < 0):
                        final_count = 0
                    total_amount = total_amount + count * prices.get(letter)[0] + (int((final_count / 3)) * 80) + \
                                   ((final_count % 3) * prices.get('Q')[0])
                else:
                    total_amount = total_amount + count * prices.get(letter)[0]
                prices.get(letter)[1] = count
                prices.get('Q')[1] = count_Q
        elif (letter in 'STWXYZ'):
            if (prices.get(letter)[1] == 0):
                l_count = []
                total_count = 0
                for x in "STWXYZ":
                    temp_count = skus.count(x)
                    total_count = total_count + temp_count
                    i = 0
                    if (temp_count > 0):
                        while i < temp_count:
                            l_count.append(prices.get(x)[0])
                            i = i + 1
                    prices.get(x)[1] = 1
                l_count.sort()
                if (total_count < 3):
                    for item in l_count:
                        total_amount = total_amount + item
                elif(total_count % 3 == 1):
                    total_amount = total_amount + int(total_count/3) * 45 + l_count[-1]
                elif (total_count % 3 == 0 and total_count >= 3):
                    total_amount = total_amount + int(total_count/3) * 45
                else:
                    total_amount = total_amount + int(total_count/3) * 45 + l_count[-2] + l_count[-1]
        else:
            return -1
    return total_amount
    raise NotImplementedError()
