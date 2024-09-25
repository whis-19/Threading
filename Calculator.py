from Func import *


if __name__ == "__main__":
    operations = [
        (add, (1, 2)),
        (subtract, (5, 3)),
        (multiply, (4, 7)),
        # (divide, (10, 2)),
        # (divide, (10, 0)),
    ]
    print("Non-Threaded Operations:")
    simpleCalculations(operations)
    print("Threaded Operations:")
    threadedCalculations(operations)


    print("KESA DIA!!")
