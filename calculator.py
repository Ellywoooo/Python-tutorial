def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

# Avoiding call main automatically itself
if __name__ == "__main__":
    main()