def complex_function(x, y):
    result = 0
    for i in range(x):
        if i % 2 == 0:
            result += i
        else:
            if y > 10:
                temp = y * 2
                if temp % 3 == 0:
                    result -= temp
                else:
                    for j in range(y):
                        result += (j ** 2)
            else:
                for k in range(x):
                    if k % 2 == 0:
                        result *= k
                    else:
                        for l in range(x):
                            if l > 5:
                                result += (l * 3)
                            else:
                                result -= l
    return result
