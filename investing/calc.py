import sys

def invest(accumulated, additional, interest):
    result = accumulated * (1 + interest)
    return result + additional

def invest_for(years, initial, yearly_amount, interest):
    result = initial
    print(f'Year 0: {result:,}')
    for i in range(1, years + 1):
        result = invest(result, yearly_amount, interest)
        print(f'Year {i}: {result:,}')
    return result


years = int(sys.argv[1])
initial_amount = int(sys.argv[2])
yearly_amount = int(sys.argv[3])
interest = float(sys.argv[4])

print()
print(f'Investing for {years} years, starting at {initial_amount} with additional {yearly_amount} each year and {interest} interest rate')

result = invest_for(years, initial_amount, yearly_amount, interest)
