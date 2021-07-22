import copy
from functools import lru_cache
import numpy as np


def delete_space(text):
    if "  " in text:
        text = text.replace("  ", " ")
        text = delete_space(text)
    return text


def prepare_name(name):

    temp_name = name.replace('.', ' ')
    temp_name = temp_name.lower()
    temp_name = delete_space(temp_name)
    temp_name = temp_name[:-1] if temp_name[-1] == ' ' else temp_name
    return temp_name


def my_dist_cached(a, b):
    @lru_cache(maxsize=len(a) * len(b))         # кэш нужен для уменьшения времени подсчета

    def recursive(i, j):            # рекурсивно находим
        if i == 0 or j == 0:
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            return recursive(i - 1, j - 1)
        else:
            return 1 + min(
                recursive(i, j - 1),
                recursive(i - 1, j),
                recursive(i - 1, j - 1)
            )

    r = recursive(len(a), len(b))
    return r


string_1 = 'Tolstoy Ivan Mikhailovich qqqqqqqqqqqqqqq'
string_2 = 'Ivan tolstoi m....     '


string_1 = prepare_name(string_1)
string_2 = prepare_name(string_2)

name1 = string_1.split(' ')
name2 = string_2.split(' ')

if len(name1) != len(name2):
    name1.append('') if len(name1) < len(name2) else name2.append('')

mismatch_matrix = np.zeros((len(name1), len(name2)))

for i in range(len(name1)):
    for j in range(len(name2)):

        if 0 < len(name1[i]) < 2 or 0 < len(name2[j]) < 2:
            shorter_name = name1[i] if len(name1[i]) < len(name2[j]) else name2[j]     # Находи наиболее короткое слово
            biggest_name = name1[i] if len(name1[i]) > len(name2[j]) else name2[j]

            if shorter_name == biggest_name[:len(shorter_name)]:            # ищем короткое слово в длинном
                mismatch_matrix[i][j] = 0
            else:
                mismatch_matrix[i][j] = my_dist_cached(name1[i], name2[j])


        else:
            mismatch_matrix[i][j] = my_dist_cached(name1[i], name2[j])



def matrix_post_processing(matrix):

    temp_matrix = copy.copy(matrix)
    print(np.rot90(temp_matrix))
    temp_matrix = np.rot90(temp_matrix)
    for i in temp_matrix:
        print(min(i))
    # for i in range(temp_matrix.shape[0]):
    #     for j in range(temp_matrix.shape[1]):
    #         # print(temp_matrix[i][j])





print(name1)
print(name2)
print(mismatch_matrix)

for pos_i, mas_i in enumerate(mismatch_matrix):
    for pos_j, element_j in enumerate(mas_i):
        if element_j > min(mas_i):
            mismatch_matrix[pos_i][pos_j] = 0

print(mismatch_matrix)


# matrix_post_processing(mismatch_matrix)

