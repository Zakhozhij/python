# Имеется упорядоченный список:
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали (имеющие равные индексы), превратить в нули.
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for indx, value in enumerate(A):
    value[indx]=0
print(A)