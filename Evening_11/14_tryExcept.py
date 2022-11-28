#################################################
#  14.11.2022 04.00PM
#################################################
#  TOPICS TO BE COVERED
# 👉 EXCEPTION  HANDLING  IN PYTHON
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#################################################

# a = 10
# # b = 100
# b = 0
# c = a/b # ZeroDivisionError: division by zero if b = 0
# print(c)


# print("This is the code ")



# try ... catch 
# in Python try ... except


try:
    a = 10
    # b = 100
    b = 0
    c = a/b # ZeroDivisionError: division by zero if b = 0
    print(c)
except FileNotFoundError as e:
    print("Some error occured ", e)
except IndexError as e:
    print("Element not found" , e )
    # print("you have enterd wrong value of b , should not be zero")
except:
    print("ok")

print("This is the code ")

print("------------------")

'''
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
'''
try:
    f = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\amar.txt")
    print(f.read()) #FileNotFoundError: [Errno 2] No such file or directory:

except FileNotFoundError as e:
    print("Some error occured ", e)



print("You have xyz amount in your acc")

print("**********")
try:
    f = open(r"C:\Users\RAHUL\Documents\OnePython\5. Sept DS 9AM 4PM\CLASS\amar.txt")
    print(f.read()) #FileNotFoundError: [Errno 2] No such file or directory:
    
    print(10/100)
    list_even = [2,4,6,8]
    print(list_even[20])
except FileNotFoundError as e:
    print("Some error occured ", e)
except ZeroDivisionError as d :
    print("Some error occured ", d)
except IndexError as e:
    print("Element not found" , e )
else:
    print("All code exceuted successfully")

finally:
    print("This will excute irrespective of exception")