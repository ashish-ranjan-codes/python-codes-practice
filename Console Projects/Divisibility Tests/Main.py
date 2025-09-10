# Main program to test divisibility of a number
import divisibility_tests

run = True

while run:
    print("\nWhat divisibility test you want to check?\n\n")
    print("1. Divisibility by 2")
    print("2. Divisibility by 3")
    print("3. Divisibility by 4")
    print("4. Divisibility by 5")
    print("5. Divisibility by 6")
    print("6. Divisibility by 7")
    print("7. Divisibility by 8")
    print("8. Divisibility by 9")
    print("9. Divisibility by 10")
    print("10. Divisibility by 11")
    print("11. Exit ? Press 0")

    num = int(input("\n\nEnter a number: "))
    ch = int(input("\n\nWhich divisibility test you want to perform? => "))

    

    res = False
    val = 0

    match ch:
        case 1:
            val = 2
            if divisibility_tests.divisible_by_2(num):
                res = True

        case 2:
            val = 3
            if divisibility_tests.divisible_by_3(num):
                res = True
                
        case 3:
            val = 4
            if divisibility_tests.divisible_by_4(num):
                res = True

        case 4:
            val = 5
            if divisibility_tests.divisible_by_5(num):
                res = True

        case 5:
            val = 6
            if divisibility_tests.divisible_by_6(num):
                res = True

        case 6:
            val = 7
            if divisibility_tests.divisible_by_7(num):
                res = True

        case 7:
            val = 8
            if divisibility_tests.divisible_by_8(num):
                res = True
                
        case 8:
            val = 9
            if divisibility_tests.divisible_by_9(num):
                res = True

        case 9:
            val = 10
            if divisibility_tests.divisible_by_10(num):
                res = True

        case 10:
            val = 11
            if divisibility_tests.divisible_by_11(num):
                res = True
                
        case 0:
            val = 0
            print("\n\nThank you! Exited.")
            run = False

        case _:
            print("\nInvalid option")

    if res:
        print(f"\nYes! {num} is divisible by {val}.")
    elif ch != 0:
        print(f"\nSorry! {num} is not divisible by {val}.")


