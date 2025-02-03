n1, n2 = 0, 1
count = 0

while True:
    try:
        # Get user input and validate
        nterms = int(input("How many terms? "))
        # check if the number of terms is valid
        if nterms <= 0:
            print("Please enter a positive integer")
        # if there is only one term, return n1
        elif nterms == 1:
            print("Fibonacci sequence upto", nterms, ":")
            print(n1)
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

# generate fibonacci sequence
print("Fibonacci sequence:")
while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
    