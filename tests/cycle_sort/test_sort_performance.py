"""

To run these tests:
pytest tests/cycle_sort/test_sort_performance.py -v -s

"""

import pytest
import time
import random
from typing import List, Callable

# Chanage sort1/sort2 depending on what you want to test
from cycle_sorts import cycle_sort, wiki_cycle_sort
sort1 = cycle_sort
sort2 = wiki_cycle_sort

# Test data generators

def generate_random_data(size: int) -> List[int]:
    return [random.randint(1, 1000) for _ in range(size)]

def generate_sorted_data(size: int) -> List[int]:
    return list(range(size))

def generate_reverse_sorted_data(size: int) -> List[int]:
    return list(range(size, 0, -1))

def time_algorithm(sort_func: Callable, data: List[int], runs: int = 3) -> float:
    # Time a sorting algorithm over multiple runs and return average time
    times = []
    for _ in range(runs):
        test_data = data.copy()
        start_time = time.perf_counter()
        sort_func(test_data)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return sum(times) / len(times)

# Pytest fixtures for test data

@pytest.fixture(params=[1000, 5000, 10000])
def data_size(request):
    # Parametrized fixture for different data sizes
    return request.param

@pytest.fixture
def random_data(data_size):
    random.seed(42)  # Same seed for  reproducible results
    return generate_random_data(data_size)

@pytest.fixture
def sorted_data(data_size):
    return generate_sorted_data(data_size)

@pytest.fixture
def reverse_sorted_data(data_size):
    return generate_reverse_sorted_data(data_size)

# Test class for comparing sorting algorithm performance

class TestSortingPerformance:
    
    def test_correctness_first(self, random_data):
        # Ensure both algorithms produce correct results before timing
        expected = sorted(random_data)
        assert sort1(random_data) == expected
        assert sort2(random_data) == expected
    
    @pytest.mark.parametrize("data_type", ["random", "sorted", "reverse"])
    def test_speed_comparison(self, data_size, data_type, request):
        # Get the appropriate data fixture
        if data_type == "random":
            data = request.getfixturevalue("random_data")
        elif data_type == "sorted":
            data = request.getfixturevalue("sorted_data")
        else:  # reverse
            data = request.getfixturevalue("reverse_sorted_data")
        
        # Time both algorithms
        time1 = time_algorithm(sort1, data)
        time2 = time_algorithm(sort2, data)

        # Print results for analysis
        print(f"\n{data_type.title()} data (size {data_size}):")
        print(f"  Sort #1: {time1:.6f}s")
        print(f"  Sort #2: {time2:.6f}s")
        print(f"  Speedup:     {time1/time2:.2f}x")

    def test_scalability_analysis(self):
        # Analyze how algorithms scale with input size
        sizes = [50, 100, 200, 500]
        results = {"sort1": [], "sort2": []}
        
        for size in sizes:
            data = generate_random_data(size)
            
            time1 = time_algorithm(sort1, data, runs=3)
            time2 = time_algorithm(sort2, data, runs=3)
            
            results["sort1"].append(time1)
            results["sort2"].append(time2)
        
        print("\nScalability Analysis:")
        print("Size\tSort #1\t\tSort #2\t\tRatio")
        for i, size in enumerate(sizes):
            ratio = results["sort1"][i] / results["sort2"][i]
            print(f"{size}\t{results['sort1'][i]:.6f}s\t{results['sort2'][i]:.6f}s\t{ratio:.2f}x")