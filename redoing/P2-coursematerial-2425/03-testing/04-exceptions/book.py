class Book:
    def __init__(self, title, isbn):
        if title == "":
            raise RuntimeError
            # raise ValueError("Title cannot be empty.")
        self.__title = title

        if self._is_valid_isbn(isbn) == False:
            # raise ValueError("Isbn is not correct.")
            raise RuntimeError
        self.__isbn = isbn

    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return self.__isbn
    
    def _is_valid_isbn(self, isbn):
        # for ch in isbn:
        #     if ch not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]:
        #         return False
        isbn = "".join(isbn.split())
        isbn = "".join(isbn.split("-"))
        
        str_lst = list(isbn)
        int_lst = []

        for ch in str_lst:
            int_lst.append(int(ch))


        total = 0
        for i in range(len(int_lst)):
            if i % 2 == 0:
                total += int_lst[i]
            else:
                total += int_lst[i] * 3

        return total % 10 == 0







    

# ISBN Validity
# The ISBN of a book consists of 13 digits, which can be separated by spaces or dashes (-). 
# Additionally, in order to detect mistakes, the last digit acts as a checksum.

# The checksum algorithm goes as follows:

# Let's say we store the digits in an array digits. This array has length 13.
# Multiply the odd-indexed digits by 3.
# Take the sum of digits.
# This sum must be divisible by 10.
# For example, consider the valid ISBN 978-1779501127. The digits array is [9, 7, 8, 1, 7, 7, 9, 5, 0, 1, 1, 2, 7].
#  Multiplying the odd-indexed digits yields [9, 21, 8, 3, 7, 21, 9, 15, 0, 3, 1, 6, 7].
#  The sum is 9 + 21 + 8 + 3 + 7 + 21 + 9 + 15 + 0 + 3 + 1 + 6 + 7 = 110 This number is divisible by 10,
#  meaning the ISBN is valid.