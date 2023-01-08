import time


def max_pairwise_product(number_list):
    result = 0
    for i in range(len(number_list) - 1):
        product = number_list[i] * number_list[i + 1]
        if product > result:
            result = product
    return result


def max_pairwise_product_fast(numbers):
    max_index_1 = max_index(numbers)
    max_index_2 = max_index(numbers, max_index_1)
    return max_index_1 * max_index_2


def max_index(numbers, skip_index=-1):
    top = 0
    for index in range(len(numbers) - 1):
        if numbers[index] > numbers[index + 1]:
            top = i
    return top


if __name__ == "__main__":
    input_list = []
    elements = 100
    for i in range(elements):
        input_list.append(i + 1)
    start = time.perf_counter()
    result = max_pairwise_product(input_list)
    elapsed_time = time.perf_counter() - start
    print("Result {}, Elapsed time {:0.2f} secs".format(result, elapsed_time))
    start = time.perf_counter()
    result = max_pairwise_product_fast(input_list)
    elapsed_time = time.perf_counter() - start
    print("Result {}, Elapsed time {:0.2f} secs".format(result, elapsed_time))
