from functools import lru_cache
import numpy as np
import pandas as pd
import difflib


def transliterate(name):
    # Слоаврь с заменами
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ya', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'YO',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': ' ', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}

    # Циклически заменяем все буквы в строке
    for key in slovar:
        name = name.replace(key, slovar[key])
    return name


def show_matrix(matrix, first_man, second_man):
    df = pd.DataFrame(matrix, columns=second_man, index=first_man)
    return df


def prepare_name(name) -> str:
    text = name.replace('.', ' ')
    text = text.lower()

    if "  " in text:
        text = text.replace("  ", " ")

    temp_name = text[:-1] if text[-1] == ' ' else text
    return temp_name


def similarity(s1, s2) -> float:
    matcher = difflib.SequenceMatcher(None, s1, s2)
    return matcher.ratio()


def convert_name(name_1, name_2, translate_eng=True):
    name_1 = prepare_name(name_1).split()
    name_2 = prepare_name(name_2).split()

    if translate_eng:
        name_1 = list(map(lambda x: transliterate(x), name_1))
        name_2 = list(map(lambda x: transliterate(x), name_2))

    return name_1, name_2


def mix_list(list_name) -> list:
    """
    Append first element of list to list
    :param list_name:
    :return:
    """
    first_element = list_name[0]
    list_name = list_name[1:]
    list_name.append(first_element)
    return list_name


def calculate_name_distance(name_1, name_2) -> bool:

    mismatch_matrix = np.zeros((len(name_1)))
    bool_mismatch_matrix = np.zeros((len(name_1)))
    count = 0

    for i in range(len(name_1)):
        if len(name_1[i]) > 2 and len(name_2[i]) > 2:
            mismatch_matrix[i] = similarity(name_1[i], name_2[i])
            if len(name_1[i]) or len(name_2[i]):
                bool_mismatch_matrix[i] = similarity(name_1[i], name_2[i]) > 0.8
            else:
                bool_mismatch_matrix[i] = similarity(name_1[i], name_2[i]) > 0.7

        elif 0 < len(name_1[i]) <= 2 or 0 < len(name_2[i]) <= 2:
            short_word = name_1[i] if len(name_1[i]) <= len(name_2[i]) else name_2[i]
            long_word = name_1[i] if len(name_1[i]) >= len(name_2[i]) else name_2[i]

            if long_word[:len(short_word)] == short_word:
                mismatch_matrix[i] = 1
                bool_mismatch_matrix[i] = True
            else:
                mismatch_matrix[i] = 0
                bool_mismatch_matrix[i] = False

    if bool_mismatch_matrix.all():
        return True
    else:
        count += 1
        if count < len(name_1):
            return calculate_name_distance(mix_list(name_1), name_2)
        else:
            return False



string_1 = 'Е Кебаб'
string_2 = 'keybab Е'

string_1, string_2 = convert_name(string_1, string_2)

# def calculate_name_distance(name_1, name_2, translate_eng=True):
#
#     name_1 = prepare_name(name_1).split()
#     name_2 = prepare_name(name_2).split()
#
#     if translate_eng:
#         name_1 = list(map(lambda x: transliterate(x), name_1))
#         name_2 = list(map(lambda x: transliterate(x), name_2))
#
#     mismatch_matrix = np.zeros((len(name_1)))
#     bool_mismatch_matrix = np.zeros((len(name_1)))
#
#     for i in range(len(name_1)):
#
#         if len(name_1[i]) > 2 and len(name_2[i]) > 2:
#             mismatch_matrix[i] = similarity(name_1[i], name_2[i])
#             if len(name_1[i]) or len(name_2[i]):
#                 bool_mismatch_matrix[i] = similarity(name_1[i], name_2[i]) > 0.8
#             else:
#                 bool_mismatch_matrix[i] = similarity(name_1[i], name_2[i]) > 0.7
#
#         elif 0 < len(name_1[i]) <= 2 or 0 < len(name_2[i]) <= 2:
#             short_word = name_1[i] if len(name_1[i]) <= len(name_2[i]) else name_2[i]
#             long_word = name_1[i] if len(name_1[i]) >= len(name_2[i]) else name_2[i]
#
#             if long_word[:len(short_word)] == short_word:
#                 mismatch_matrix[i] = 1
#                 bool_mismatch_matrix[i] = True
#             else:
#                 mismatch_matrix[i] = 0
#                 bool_mismatch_matrix[i] = False
#
#     print(mismatch_matrix)
#     if bool_mismatch_matrix.all():
#         return True
#     else:
#         return False

#
# def my_dist_cached(a, b) -> int:
#     # расчет дистанции
#     @lru_cache(maxsize=len(a) * len(b))  # кэш нужен для уменьшения времени подсчета
#     def recursive(i, j):  # рекурсивно находим
#         if i == 0 or j == 0:
#             return max(i, j)
#         elif a[i - 1] == b[j - 1]:
#             return recursive(i - 1, j - 1)
#         else:
#             return 1 + min(
#                 recursive(i, j - 1),
#                 recursive(i - 1, j),
#                 recursive(i - 1, j - 1)
#             )
#
#     r = recursive(len(a), len(b))
#     return r


# def calculate_distance_old(name_1, name_2):
#     if len(name_1) != len(name_2):
#         name_1.append('') if len(name_1) < len(name_2) else name_2.append('')
#
#     mismatch_matrix = np.zeros((len(name_1), len(name_2)))
#     distance = 0
#
#     for i in range(len(name_1)):
#         for j in range(len(name_2)):
#
#             if 0 < len(name_1[i]) < 2 or 0 < len(name_2[j]) < 2:
#                 shorter_name = name_1[i] if len(name_1[i]) < len(name_2[j]) else name_2[
#                     j]  # Находи наиболее короткое слово
#                 biggest_name = name_1[i] if len(name_1[i]) > len(name_2[j]) else name_2[j]
#
#                 if shorter_name == biggest_name[:len(shorter_name)]:  # ищем короткое слово в длинном
#                     mismatch_matrix[i][j] = 0.5
#                 else:
#                     mismatch_matrix[i][j] = my_dist_cached(name_1[i], name_2[j]) / (len(name_1[i]) + len(name_2[j]))
#                 distance = distance + my_dist_cached(name_1[i], name_2[j])
#
#             elif len(name_1[i]) == 0 or len(name_2[j]) == 0:
#                 mismatch_matrix[i][j] = max(len(name_1[i]), len(name_2[i])) / (len(name_1[i] + len(name_2[j])))
#
#             else:
#                 print(type(my_dist_cached(name_1[i], name_2[j])))
#
#                 mismatch_matrix[i][j] = my_dist_cached(name_1[i], name_2[j]) / (len(name_1[i]) + len(name_2[j]))
#
#     return mismatch_matrix
#
#
# def calculate_distance(name_1, name_2):
#     # Расчет расстояние между именами
#     if len(name_1) != len(name_2):
#         name_1.append('') if len(name_1) < len(name_2) else name_2.append('')
#     mismatch_matrix = np.zeros((len(name_1), len(name_2)))
#
#     for i in range(len(name_1)):
#         for j in range(len(name_2)):
#             mismatch_matrix[i][j] = my_dist_cached(name_1[i], name_2[j])
#
#     return mismatch_matrix
#
#
# def juxtaposition_name(pd_matrix):
#     # сопоставление имен
#     pd_matrix_copy = pd_matrix.copy()
#     distance = 0
#
#     for num, element in enumerate(pd_matrix_copy.index):
#
#         min_element = int(min(pd_matrix_copy.iloc[num]))
#         row = pd_matrix_copy.iloc[num].to_list()  # возращаем список значений строки
#
#         if row.count(min_element) == 1 and min_element < 3:  # проверяем сколько мин значений
#             min_elem_pos = row.index(min_element)
#             column = pd_matrix_copy.loc[:, pd_matrix_copy.columns[num]].to_list()  # возращаем все колонки из таблицы
#
#             if min_element == min(column) and column.count(min_element) == 1:
#                 # pd_matrix_copy = pd_matrix_copy.drop(index=pd_matrix_copy.index[num],
#                 # columns=pd_matrix_copy.columns[min_elem_pos])
#                 print(pd_matrix_copy.index[num], pd_matrix_copy.columns[min_elem_pos])
#
#             distance = distance + min_element
#
#             # if column.count(min_element) == 1:
#             # pd_matrix_copy.drop(index=pd_matrix_copy.index[num], columns=pd_matrix_copy.columns[min_elem_pos])
#
#         else:
#
#             distance = distance + min_element
#
#     return pd_matrix_copy, distance
#
#
# def comparison_name(name_1, name_2):
#     name1 = prepare_name(name_1).split()
#     name2 = prepare_name(name_2).split()
#     mis_matrix = calculate_distance_old(name1, name2)
#     pd_matrix = show_matrix(mis_matrix, name1, name2)
#     print(pd_matrix)
#     matrix, dist = juxtaposition_name(pd_matrix)
#
#     max_len_name = max(len(name_1), len(name_2))
#     dist = dist / max_len_name
#     if dist < 0.3:
#         return True
#     else:
#         return False

#
# string_1 = transliterate(string_1)
# dist = comparison_name(string_1, string_2)
# print(dist)


#
# def calculate_distance_old(name_1, name_2):
#     if len(name_1) != len(name_2):
#         name_1.append('') if len(name_1) < len(name_2) else name_2.append('')
#
#     mismatch_matrix = np.zeros((len(name_1), len(name_2)))
#     distance = 0
#
#     for i in range(len(name_1)):
#         for j in range(len(name_2)):
#
#             if 0 < len(name_1[i]) < 2 or 0 < len(name_2[j]) < 2:
#                 shorter_name = name_1[i] if len(name_1[i]) < len(name_2[j]) else name_2[
#                     j]  # Находи наиболее короткое слово
#                 biggest_name = name_1[i] if len(name_1[i]) > len(name_2[j]) else name_2[j]
#
#                 if shorter_name == biggest_name[:len(shorter_name)]:  # ищем короткое слово в длинном
#                     mismatch_matrix[i][j] = 0
#                 else:
#                     mismatch_matrix[i][j] = my_dist_cached(name_1[i], name_2[j])
#                 distance = distance + my_dist_cached(name_1[i], name_2[j])
#
#             elif len(name_1[i]) == 0 or len(name_2[j]) == 0:
#                 mismatch_matrix[i][j] = max(len(name_1[i]), len(name_2[i]))
#
#             else:
#                 mismatch_matrix[i][j] = my_dist_cached(name_1[i], name_2[j])
#
#     return mismatch_matrix
