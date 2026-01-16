def division_test():
    # Intentional ZeroDivisionError to trigger CI failure
    result = 10 / 0
    print(f"Result is {result}")

if __name__ == "__main__":
    division_test()
