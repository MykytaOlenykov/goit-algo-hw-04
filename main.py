import random

from timeit import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort


def main():
    arr = [random.randint(0, 10000) for _ in range(10000)]

    time_merge_sort = timeit(lambda: merge_sort(arr[:]), number=10)
    time_insertion_sort = timeit(lambda: insertion_sort(arr[:]), number=10)
    time_timsort_sort = timeit(lambda: arr[:].sort(), number=10)
    time_timsort_sorted = timeit(lambda: sorted(arr[:]), number=10)

    print(f"{'| Algorithm': <20} | {'Time': <20}")
    print(f":{'-'*19} | :{'-'*20}")
    print(f"{'| Merge sort': <20} | {time_merge_sort: <20.5f}")
    print(f"{'| Insertion sort': <20} | {time_insertion_sort: <20.5f}")
    print(f"{'| Timsort(sort)': <20} | {time_timsort_sort: <20.5f}")
    print(f"{'| Timsort(sorted)': <20} | {time_timsort_sorted: <20.5f}")


if __name__ == "__main__":
    main()
