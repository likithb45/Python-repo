def convert(n):
    num = str(n)
    
    #base conditon for last 3 digit(hundred)
    if len(num) <= 3:
        return num
    
    hundreds = num[-3:]
    remaining = num[:-3]
    parts = []
    while len(remaining) > 2:
        parts.append(remaining[-2:])
        remaining = remaining[:-2]
    if remaining:
        parts.append(remaining)
    # Reverse and joining str
    indian = ','.join(parts[::-1]) + ',' + hundreds
    return indian

number=int(input())
notation = convert(number)
print(notation)  
