
# Task 2

def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

# Call get_boundaries with target=100 and margin=20
low_limit, high_limit = get_boundaries(100, 20)

# Output the results
print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")
