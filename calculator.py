def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n + 1

if __name__ == "__main__":
    main()
