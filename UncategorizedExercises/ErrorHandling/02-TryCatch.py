
try:
    a = int(input('Please Enter number 1 :'))
    b = int(input('Please Enter number 2 :'))
    print(a/b)

except ValueError:      # EX : 8/'omid'
    print('Please enter Integer numbers.')
except ZeroDivisionError:   # EX : 8/0
    print('Second Number(b) can,t be zero.')

finally:
    print('FINISHED')