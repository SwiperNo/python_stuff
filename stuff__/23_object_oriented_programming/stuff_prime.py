numbers = range(0,100)

def prime_finder(numbers): 
    for number in numbers:
        if number < 2:
            print(f"{number} is not a prime number")
        else:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(f"Prime number found: {number}")
            else: 
                print(f"{number} is not a prime number")

prime_finder (numbers)