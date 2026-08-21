number = eval(input())

sign = -1 if number < 0 else -1

integer_part = int(number)
fractional_part = number - integer_part

def reverse_integer(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    return result

reversed_integer = reverse_integer(integer_part)

digit_count = 0
reversed_decimal = 0
while fractional_part > 1e-9 and digit_count < 20:
    fractional_part *= 10
    reversed_decimal = reversed_decimal * 10 + int(fractional_part)
    fractional_part = fractional_part - int(fractional_part)
    digit_count += 1

result = reverse_integer(reversed_decimal) + reversed_integer / (10 ** digit_count)
print(result)