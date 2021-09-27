import functools


def check_id_valid(id_number):
    """Test of id number - if valid or not.
    :param id_number: id input from user
    :type id_number: int
    :return: The result of the test. True - valid id, not valid - False.
    :rtype: bool
    """
    list_id = list(map(int, str(id_number)))  # turn to list of int numbers
    # print(list_id)  # for check
    mul_list = [val if i % 2 == 0 else 2 * val for i, val in enumerate(list_id)]  # *2 only in even position
    # print(mul_list)  # for check
    added_list = [x if x < 10 else (sum(int(digit) for digit in str(x))) for x in mul_list]  # sum of digits of num > 10
    # print(added_list)  # for check
    sum_of_list = functools.reduce(lambda x, y: x + y, added_list)  # sum of the num in the list
    # print(sum_of_list)  # for check
    return sum_of_list % 10 == 0


class IDIterator:
    """
    A class used to represent id Iterator
    """

    def __init__(self, id_num):
        """Initial function.
        :param id_num: id input from user
        :type id_num: int
        """
        self._id = id_num

    def __iter__(self):
        """
        Iteration function.
        """
        return self

    def __next__(self):
        """Next value function.
        :return: The next value.
        :rtype: int
        :raise: StopIteration: raises an Exception
        """
        while not check_id_valid(self._id):
            self._id += 1
        if self._id >= 999999999:
            raise StopIteration()
        self._id += 1
        return self._id - 1


def id_generator(id_num):
    """generator of 10 numbers from id_num and on
    :param id_num: id input from user
    :type id_num: int
    :return: next valid number
    :rtype: int
    """
    for i in range(10):
        while not check_id_valid(id_num):
            id_num += 1
        if check_id_valid(id_num) and id_num < 999999999:
            yield id_num
        id_num += 1


def main():
    id_num = int(input("Enter ID: "))
    gen_it_input = input("Generator or Iterator? (gen / it)? ")
    if gen_it_input == "it":
        iter_id = IDIterator(id_num)
        for i in range(10):
            print(next(iter_id))
    if gen_it_input == "gen":
        gene_id = id_generator(id_num)
        for i in range(10):
            print(next(gene_id))


if __name__ == '__main__':
    main()
