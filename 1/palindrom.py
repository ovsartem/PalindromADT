"""
Palindrome class realization.
"""

from arraystack import ArrayStack   # or from linkedstack import LinkedStack


def polindromes(poli):
    """
    finds polindromes
    """
    main_polindrome = []
    for _ in range(len(poli)):
        word = poli.pop()
        new_stack = ArrayStack()
        delimeter = len(word)//2
        first_half = word[:delimeter][::-1]
        for j in range(delimeter):
            new_stack.push(word[-j-1])
        counter = 0
        for i in range(len(new_stack)):
            if new_stack.pop() != first_half[i]:
                counter += 1
        if counter == 0:
            main_polindrome.append(word)
    return main_polindrome


class Palindrome:
    """
    class Palindrome
    """

    def read_file(self, path):
        """
        reads files
        """
        with open(path, 'r') as data:
            stack = ArrayStack()
            for line in data:
                stack.push(line.strip().split()[0])
            return stack

    def write_to_file(self, polidrom, output):
        """
        writes files
        """
        with open(output, 'w') as data:
            data.write('\n'.join(polidrom))
        return polidrom

    def find_palindromes(self, path1, path2):
        """
        main function that finds all palindromes
        """
        words1 = self.read_file(path1)
        polindrome1 = polindromes(words1)
        return self.write_to_file(polindrome1, path2)


palindrome = Palindrome()
palindrome.find_palindromes("words.txt", "palindrome_en.txt")
# wor = "попоп"
# for i in range(len(wor)//2):
#     palindrome.push(wor[-i-1])
# print(palindrome)
