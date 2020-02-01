#divisor_master_new

print('1) проверка числа на простоту:')
def PrimeNumber(n):
    i = 2
    while n > i:
        if n % i == 0:
            return (n,'непростое число')
        i += 1
        if i == n:
            return (n,'простое число')
print(PrimeNumber(600))
print(PrimeNumber(163))

print('2) список всех делителей числа 600:')
def divs(n):
    result = []
    n = n // 2
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result
print(divs(600))

print('3) самый большой делитель числа 600:')
from functools import reduce
def max_div(n):
    max_number = divs(n)
    max_number = reduce(lambda a,b: a if a>b else b, max_number)
    return(max_number)
print(max_div(600))

print('4) наибольший простой делитель числа 600:')
def PrimeDiv(r, n=2):
    while n <= r:
        if r % n:
            n += 1
        else:
            r //= n
            yield n
print(max(PrimeDiv(600)))

print('5) каноническое разложение числа 600 на простые множители:')
def factors(num, d=2):
    while num > 1:
        n1, n2 = divmod(num, d)
        if n2:
            d += 1
        else:
            yield d
            num = n1
n = int(600)
print('{} = {}' .format(n, ' * '.join(map(str, factors(n)))))

#pytest

def test_1_PrimeNumber():
    assert (600, 'непростое число') == PrimeNumber(600)
def test_2_PrimeNumber():
    assert (163, 'простое число') == PrimeNumber(163)
def test_3_divs():
    assert divs(600) == [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 25, 30, 50, 60, 75, 100, 150, 300]
def test_4_max_div():
    assert max_div(600) == 300
def test_5_PrimeDiv():
    assert (max(PrimeDiv(600))) == 5
def test_6_factors():
    assert ('{} = {}' .format(n, ' * '.join(map(str, factors(n))))) == '600 = 2 * 2 * 2 * 3 * 5 * 5'