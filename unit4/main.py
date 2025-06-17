import generators


def main():
    print(generators.translate("el gato esta en la casa"))
    print(generators.first_prime_over(1000000))
    print(list(generators.parse_ranges("0-0,4-8,20-21,43-45")))

    fibo_gen = generators.get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    return 1


if __name__ == '__main__':
    main()
