# Ackermann's Function
def ackermann(m, n):
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(2, 2))

'''
Steps of running codes :

A(2,2)
A(1,A(2,1))
A(1,A(1,A(2,0)))
A(1,A(1,A(1,1)))
A(1,A(1,A(0,A(1,0))))
A(1,A(1,A(0,A(0,1))))
A(1,A(1,A(0,2)))
A(1,A(1,3))
A(1,A(0,A(1,2)))
A(1,A(0,A(0,A(1,1))))
A(1,A(0,A(0,A(0,A(1,0)))))
A(1,A(0,A(0,A(0,A(0,1)))))
A(1,A(0,A(0,A(0,2))))
A(1,A(0,A(0,3)))
A(1,A(0,4))
A(1,5)
A(0,A(1,4))
A(0,A(0,A(1,3)))
A(0,A(0,A(0,A(1,2))))
A(0,A(0,A(0,A(0,A(1,1)))))
A(0,A(0,A(0,A(0,A(0,A(1,0))))))
A(0,A(0,A(0,A(0,A(0,A(0,1))))))
A(0,A(0,A(0,A(0,A(0,2)))))
A(0,A(0,A(0,A(0,3))))
A(0,A(0,A(0,4)))
A(0,A(0,5))
A(0,6)
7

'''
