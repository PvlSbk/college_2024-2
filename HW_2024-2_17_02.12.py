# Задание от 02.12.24
# 1. Напишите функцию bool isPalindrome(const char* str), которая принимает строку и возвращает true,
# если строка является палиндромом, и false в противном случае.
# 2. Напишите функцию bool isPrime(int n), которая принимает целое число n и возвращает true,
# если число простое, и false в противном случае.
# 3. Напишите функцию bool isLeapYear(int year), которая принимает год и возвращает true, если год является високосным,
# и false в противном случае. Год является високосным, если он делится на 4, но не делится на 100, или делится на 400.

class Utils:

    @staticmethod
    def is_palindrome(s: str) -> bool:
        s = s.replace(" ", "").lower()
        return s == s[::-1]

    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_leap_year(year: int) -> bool:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

utils = Utils()

print(utils.is_palindrome("A man a plan a canal Panama"))
print(utils.is_palindrome("Hello"))

print(utils.is_prime(29))
print(utils.is_prime(30))

print(utils.is_leap_year(2024))
print(utils.is_leap_year(2023))