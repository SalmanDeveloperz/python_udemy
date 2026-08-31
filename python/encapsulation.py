"""
Encapsulation:
Bundling of Data
"""

class Number:
    _a=3
    __b=6
    def show(self):
        print(f"protected: {self._a}")
        print(f"Private: {self.__b}")

obj= Number()
obj.show()

print("testing outside of the class to print the protected", obj._a+9)
print('testing outside of the class to print the private', obj.__b)