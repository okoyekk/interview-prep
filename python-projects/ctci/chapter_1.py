# # Check Permutation
# def is_permutation(a:str, b:str):
#     if sorted(a) == sorted(b):
#         print("True")
#     else:
#         print("False")

# s1 = "hello"
# s2 = "lleho"
# s3 = "eloho"
# is_permutation(s1, s2)
# is_permutation(s1, s3)

# # URLify
# def urlify(s):
#     new_string = []
#     s = s.strip()
#     for index, char in enumerate(s):
#         if char == " ":
#             new_string.append("%20")
#         else:
#             new_string.append(char)
#     s = "".join(new_string)
#     return s

# print(urlify("Mr John Smith   "))

# # Palindrome Permutation
# def is_permutation(word: str):
#     # make take out all spaces and join word
#     word = "".join(word.lower().split())
#     # count occurences of each letter
#     counts = [0] * 26
#     odd_count = 0
#     for char in word:
#         index = ord(char) - ord("a")
#         counts[index] += 1
#         # check if letter is odd or not (increase odd count if true, else decrease it)
#         if counts[index] % 2 == 1:
#             odd_count += 1
#         else:
#             odd_count -= 1

#     if odd_count > 1:
#         return False
#     else:
#         return True

# words = ["Tact Coa", "Han Han", "Kene chi", "Jojo Wawa"]
# for word in words:
#     print(is_permutation(word))

# # One away
# def get_edits(before, after):
#     edits = 0
#     # check if they are the same (0 edits)
#     if before == after:
#         print("No edits done")
#         return True
#     # check if the length difference between both strings is > 1
#     elif abs(len(before) - len(after)) > 1:
#         return False
#     # count occurences of each letter in both strings
#     counts = [0] * 26
#     for char in before + after:
#         index = ord("z") - ord(char)
#         counts[index] += 1
#     # return False if there are more than 3 odd occurences
#     odd_count = 0
#     for i in counts:
#         if i % 2 == 1:
#             odd_count += 1
#     if odd_count > 3:
#         return False
#     return True


# pairs = [("pale", "ple"), ("pales", "pale"),
#          ("pale", "bale"), ("pale", "bake")]
# for pair in pairs:
#     print(get_edits(pair[0], pair[1]))


# # String compression
# def compress(s):
#     s_list = []
#     count = 0
#     for index, char in enumerate(s):
#         if index == 0:
#             count +=1
#             s_list.append(char)
#         # check if previous and current char are equal
#         elif char == s[index - 1]:
#             count += 1
#         # append count to list, reset it to 1 and append new char to list
#         else:
#             s_list.append(count)
#             count = 1
#             s_list.append(char)
#     # append count of last letter sequence
#     s_list.append(count)
#     s_list = list(map(lambda x: str(x), s_list))

#     compressed_s = "".join(s_list)
#     # return shorter word
#     return min((s, compressed_s), key=len)

# print(compress("aabcccccaaa"))
# print(compress("abc"))


# # Rotate N*N Matrix
# def rotate(matrix):
#     # check if matrix dimension is valid
#     if len(matrix) == 0 or len(matrix) != len(matrix[0]):
#         return False
#     N = len(matrix)
#     # iterate over rows and columns to flip matrix diagonally
#     for i in range(N):
#         for j in range(i, N):
#             # check if element lies on diagonal
#             if i == j:
#                 continue
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp
#     # iterate over rows of matrix (and columns halfway) to
#     # flip is horizontally using 2 pointers
#     for i in range(N):
#         for j in range(0, N//2):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[i][N-1-j]
#             matrix[i][N-1-j] = temp
#     return matrix

# image = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# print(rotate(image))
# expected = [[7, 4, 1],
#             [8, 5, 2],
#             [9, 6, 3]]
# print(expected)


# # Zero Matrix for M*N matrix
# def zero_matrix(matrix):
#     # check if matrix is valid
#     if len(matrix) == 0:
#         return False
#     elif len(matrix[0]) == 0:
#         return False

#     # iterate over matrix and store the positions of all zeros
#     zeros = []
#     M = len(matrix)
#     N = len(matrix[0])
#     for i in range(M):
#         for j in range(N):
#             if matrix[i][j] == 0:
#                 zeros.append((i, j))
#     # iterate over zeros list to find rows and columns to set to 0
#     rows = set()
#     cols = set()
#     for pos in zeros:
#         rows.add(pos[0])
#         cols.add(pos[1])
#     # set rows to zero
#     for i in range(M):
#         for j in range(N):
#             if (i in rows) or (j in cols):
#                 matrix[i][j] = 0
#     return matrix

# image = [[0, 2, 3, 4],
#          [5, 6, 7, 0],
#          [9, 10, 11, 12]]
# print(zero_matrix(image))
# expected = [[0, 0, 0, 0],
#             [0, 0, 0, 0],
#             [0, 10, 11, 0]]
# print(expected)


# # String rotation
# def is_substring(s1, s2):
#     if s1 in s2:
#         return True
#     return False

# def is_rotation(s1, s2):
#     # this function checks if s2 is a rotation of s1
#     if not(type(s1) == str and type(s2) == str):
#         # check if both parameters are strings
#         return False

#     # concatenate s2 to s2 annd check if s1 is a substring of it
#     s2_double = s2 + s2
#     return is_substring(s1, s2_double)

# print(is_rotation("waterbottle", "erbottlewat"))
# print(is_rotation("kenechi", "chikene"))
