price = 1000000
good_credit = False

if good_credit:
    pd = 10/100 * price
    print(f"Put down ${pd:,.2f}")

else:
    pd = 20/100 * price
    print(f"Put down ${pd:,.2f}")

print(f"Your down payment is ${pd:,.2f} ")



