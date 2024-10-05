import numpy as np

#[+] 1. Отсортировать значения массива по частоте встречания.
#[+] 2. Дана картинка высоты h, ширины w, тип данных np.uint8 (от 0 до 255). Найти количество уникальных цветов.
#[+] 3. Написать функцию, вычислающую плавающее среднее вектора
#[+] 4. Дана матрица (n, 3). Вывести те тройки чисел, которые являются длинами сторон треугольника.
#[ ] 5. Решить следующую систему линейных уравнений (не используя np.linalg.solve):
#   3x + 4y + 2z = 17  \\
#   5x + 2y + 3z = 23  \\
#   4x + 3y + 2z = 19  \\ 
#[ ] 6.  Выполнить сингулярное разложение матрицы: \
#   A = np.matrix("1 0 1; 0 1 0; 1 0 1")

###EXAMPLES

np.random.seed(18182)
#a = np.random.randint(5, size=10)
#print('Исходный:', a)
#print('Уникальные значения', np.unique(a))
#print('Уникальные значения и их частота', np.unique(a, return_counts=True))
#print(len(np.unique(a)))

#a2 = np.unique(a, return_counts=True)
#print(a2[0])
#print(np.argsort(a2[1]))
#print(a2[0][np.argsort(a2[1])])

#in_arr = np.array([2, 0, 1, 5, 4, 1, 9])
#print("Input unsorted array : ", in_arr)
 
#out_arr = np.argsort(in_arr)
#print("Output sorted array indices : ", out_arr)
#print("Output sorted array : ", in_arr[out_arr])
###
print("\n----1----")
orig_arr = np.random.randint(5, size=20)
uniq_arr = np.unique(orig_arr, return_counts = True)
sort_arr = np.argsort(uniq_arr[1])
print("array        :", orig_arr)
print("values       :", uniq_arr[0])
print("frequency    :", uniq_arr[1])
print("sorted array :", uniq_arr[0][sort_arr])

print("\n----2----")
h = 200
w = 300
screen = np.random.randint(0, high = 226, size = (h, w, 3), dtype = np.uint8)
#print(screen)
print("Colour count :", len(np.unique(screen.reshape(-1, 3), axis = 0)))

print("\n----3----")
arr3 = np.random.randint(10, size = 10)
print(arr3)
for i in range (len(arr3)-2):
    print(arr3[i:i+2].mean())

print("\n----4----")
n = 10
tri_matrix = np.random.randint(10, size = (n, 3))
print(tri_matrix)
tris = np.unique(tri_matrix, axis = 0)
print("valid triangles:")
for tri in tris:
    if tri[0] < tri[1] + tri[2] and tri[1] < tri[2] + tri[0] and tri[2] < tri[0] + tri[1]:
        print(tri)
print("-----")
valid_mask = (np.sum(tri_matrix[:, [1, 2]], axis = 1) > tri_matrix[:, 0])
print(valid_mask)
valid_mask *= (np.sum(tri_matrix[:, [0, 2]], axis = 1) > tri_matrix[:, 1])
print(valid_mask)
valid_mask *= (np.sum(tri_matrix[:, [0, 1]], axis = 1) > tri_matrix[:, 2])
print(valid_mask)
print(tri_matrix[valid_mask])

print("\n----5----")
A = np.matrix("3 4 2; 5 2 3; 4 3 2")
B = np.matrix("17; 23; 19")
A_inv = np.linalg.inv(A)
X = A_inv * B
print(A, "\n")
print(B, "\n")
print(X, "\n")
