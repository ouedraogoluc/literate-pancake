
import mypackage
import mypackage.operations
print(mypackage.operations.addition(1, 2))

from mypackage import operations
print(operations.soustraction(1, 2))

from mypackage.operations import multiplication
print(multiplication(1, 2))

print(mypackage.operations.addition(1, 2))
