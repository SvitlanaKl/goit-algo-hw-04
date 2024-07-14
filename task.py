import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для генерації випадкового списку
def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

# Налаштування для тестування
sizes = [100, 1000, 10000]
iterations = 5

def test_sorting_algorithms():
    results = {}
    for size in sizes:
        data = generate_random_list(size)
        
        merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=iterations)
        insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=iterations)
        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=iterations)
        
        results[size] = {
            "Merge Sort": merge_sort_time,
            "Insertion Sort": insertion_sort_time,
            "Timsort": timsort_time
        }
        
    return results

results = test_sorting_algorithms()

# Виведення результатів
for size, times in results.items():
    print(f"Array size: {size}")
    for algo, time in times.items():
        print(f"{algo}: {time:.6f} seconds")
    print()

