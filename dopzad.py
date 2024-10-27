def univers_calculate(data_structure):
    data_structure_sum = 0
    if isinstance(data_structure, (int, float)):
        data_structure_sum = data_structure_sum + data_structure
    elif isinstance(data_structure, str):
        data_structure_sum += len(data_structure)
    elif isinstance(data_structure, (tuple, set, list)):
        for i in data_structure:
            data_structure_sum = data_structure_sum + univers_calculate(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            data_structure_sum = data_structure_sum + univers_calculate(key)
            data_structure_sum = data_structure_sum + univers_calculate(value)
    return data_structure_sum


data_structure = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),
  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}])]
rezult = univers_calculate(data_structure)
print(rezult)
