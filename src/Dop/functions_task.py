
# Task 1: Function to create a spreadsheet with default and custom row counts

def create_spreadsheet(title, row_count=1000):
    print(f"Создание электронной таблицы с названием {title} with {row_count} lines.")

# Call create_spreadsheet with title "Загрузки"
create_spreadsheet("Загрузки")

# Call create_spreadsheet with title "Приложения" and row_count set to 10
create_spreadsheet("Приложения", 10)

# Task 2: Function to return low and high boundaries based on target and margin

def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit

# Call get_boundaries with target=100 and margin=20
low_limit, high_limit = get_boundaries(100, 20)

# Output the results
print(f"Нижний предел: {low_limit}, верхний предел: {high_limit}")
