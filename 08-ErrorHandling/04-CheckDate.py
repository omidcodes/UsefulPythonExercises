from datetime import date, timedelta


def checkdate():
    mydays = (str(date.today() - timedelta(days=1)),  # yesterday
              str(date.today()),  # now(Today)
              str(date.today() + timedelta(days=1))
              )  # tomorrow

    # now = date.today() - timedelta(days=1); yesterday =  date.today(); tomorrow = date.today() + timedelta(days=1)

    # print(now)

    x = str(input('Please Enter today or yesterday or tomorrow in this format \n '
                  'Example (yyyy-mm-dd)(2020-03-24) : '))

    # if x == str(now) or x == str(yesterday) or x == str(tomorrow):
    if x in mydays:
        return ('Entered Date is Correct.')
    else:
        return ('It,s Incorrect')


if __name__ == '__main__':
    print(checkdate())
