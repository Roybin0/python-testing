def even_number_of_evens(numbers):
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        for n in numbers:
            if n % 2 == 0:
                evens += 1

        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("No list provided")


if __name__ == "__main__":
    print(even_number_of_evens(5))
