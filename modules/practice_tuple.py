immutable_var = 1, True, "test"

print(immutable_var)

# immutable_var[0] = "test" Кортежи не поддерживают изменение значения элементов

mutable_list = [1, "Test", True]

print(mutable_list)

mutable_list[0] = 2
mutable_list[1] = "Not Test"

print(mutable_list)