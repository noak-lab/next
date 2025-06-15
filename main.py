import oneLiners
def main():
    print(oneLiners.double_letter('we are the champions!'))
    print(oneLiners.four_dividers(8))
    print(oneLiners.sum_of_digits(174))

    print(oneLiners.intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

    print(oneLiners.is_funny("hahahahahaha"))

    print(oneLiners.decrypt_password("sljmai ugrf rfc ambc: lglc dmsp mlc rum"))

    oneLiners.print_longest_line("names.txt")
    oneLiners.print_length_of_file_data("names.txt")
    oneLiners.print_shortest_name("names.txt")
    oneLiners.write_line_length("names.txt", "name_length.txt")
    oneLiners.print_by_length("names.txt")

if __name__ == '__main__':
    main()

