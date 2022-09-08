# Inicjacja klasy Solution

class Solution:

    # Inicjacja konstruktora zawierjącego tabelę liczb
    def __init__(self):
        self.table = [3, 7, 19, 2, 59, 22, 9, 18, 40, 4, 14, 26]

    # Metoda sprawdzająca czy liczba jest pierwsza
    def __isPrime(self, number):
        i = 2
        while i * i <= number:
            if number % i == 0:
                return False
            i += 1
        return True

    # Metoda wyszukiwania binarnego sprawdzająca tabelę
    # z konstruktora w celu wyszukania pierwszej liczby złożonej
    def getResult(self):
        left = 0
        right = len(self.table)

        while left < right:
            mid = (right + left) // 2
            if self.__isPrime(self.table[mid]):
                left = mid + 1
                print("dziala")
            else:
                right = mid
                print("nie dziala")
        return self.table[left]


# Wywołanie odpowiednich metod klasy Solution
test = Solution()
print(test.getResult())
