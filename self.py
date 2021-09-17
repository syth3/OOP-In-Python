class MyClass:
    def print_memory_address(self):
        print("Print inside of class:", self)


object1 = MyClass()
print("Print outside of class:", object1)
object1.print_memory_address()

print()

object2 = MyClass()
print("Print outside of class:", object2)
object2.print_memory_address()
