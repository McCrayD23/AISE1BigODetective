import random
import time

def count_pairs_nested(data, target):
    """Finds pairs summing to target using nested loops. O(n²)"""
    count = 0
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] + data[j] == target:
                count += 1
    return count


def count_pairs_set(data, target):
    """Finds pairs summing to target using a set. O(n)"""
    count = 0
    seen = set()
    for item in data:
        complement = target - item
        if complement in seen:
            count += 1
        seen.add(item)
    return count

def benchmark(func, data, target):        
    """Time how long a function takes and return the result along with elapsed time."""
    start = time.time()
    result = func(data, target)
    end = time.time()
    return result, end - start   # Return both result and timing

sizes = [1000, 5000, 10000]
target = 1000
print(f"{'n':>7}     |      {'Nested (n²)':>12}  |    {'Set (n)':>10}")
print("=" * 50)

for size in sizes:
    data = list(range(size))
    random.shuffle(data)

    # Unpack both the pair count and timing
    pairs1, t1 = benchmark(count_pairs_nested, data, target)
    pairs2, t2 = benchmark(count_pairs_set, data, target)

    # Print the pair count and timing details for this run
    print(f"Pairs found: {pairs1}")
    print(f"n={size:>6}    |    {t1:>10.4f}s    |  {t2:>8.4f}s")
    print("-" * 50)