import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Linear Search Algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            yield arr, i
        yield arr, -1

# Binary Search Algorithm
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        yield arr, mid
        if arr[mid] == target:
            yield arr, mid
            return
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    yield arr, -1

# Function to update the bars in the graph
def update_plot(data, bars, index):
    arr, target_index = data
    for i, rect in enumerate(bars):
        rect.set_height(arr[i])
        rect.set_color('blue' if i == target_index else 'gray')

# Function to visualize search algorithm
def visualize_search(algorithm, arr, target):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, align='edge')
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, int(1.1 * max(arr)))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def init():
        update_plot((arr, -1), bars, -1)
        return bars

    def update(data):
        arr, target_index = data
        update_plot(data, bars, target_index)
        return bars

    ani = animation.FuncAnimation(fig, update, frames=algorithm, init_func=init, interval=500, repeat=False, save_count=200)
    plt.show()

# Driver code to test search algorithms
if __name__ == "__main__":
    n = 20  # Number of elements
    arr = sorted([random.randint(1, n * 5) for _ in range(n)])
    target = random.choice(arr)

    print("Select search algorithm: \n1. Linear Search\n2. Binary Search")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        algorithm = linear_search(arr, target)
        print(f"Visualizing Linear Search for target: {target}")
    elif choice == 2:
        algorithm = binary_search(arr, target)
        print(f"Visualizing Binary Search for target: {target}")
    else:
        print("Invalid choice!")
        exit()

    visualize_search(algorithm, arr, target)
