import random
list_1M = [[] for _ in range(1000003)]
list_1M_size: int = len(list_1M)
fill = 0.5
hit_table = [[] for _ in range(int(fill * list_1M_size))]
f = open("big_random.txt", "r")
hash_table_input = f.readlines()
hash_table_input = [int(word[:-1]) for word in hash_table_input]  # ints
#hash_table_input = [word[:-1] for word in hash_table_input]  # strings
f.close()

f = open("miss.txt", "r")
miss_table = f.readlines()
#miss_table = [word[:-1] for word in miss_table]  # remove '\n' from each line
miss_table = [int(word[:-1]) for word in miss_table]  # remove '\n' from each line
f.close()

f = open("names.txt", "r")
names = f.readlines()
names = [word[:-1] for word in names]  # remove '\n' from each line
f.close()
# the file 'names' is taken from:
# https://www.usna.edu/Users/cs/roche/courses/s15si335/proj1/files.php%3Ff=names.txt&downloadcode=yes
# list_1M[10] = 20
# if not list_1M[10]:
#     print("empty")
# else:
#     print(list_1M[10])

#
# def hashing_function_lin(key, i):
#     if not i:
#         return key % list_1M_size
#     else:
#         return (key % list_1M_size + 3 * i) % list_1M_size


def hashing_function_lin(key, i):
    if type(key) is int:
        if not i:
            return key % list_1M_size
        else:
            return (key % list_1M_size + 3 * i) % list_1M_size
    elif type(key) is str:
        h = 0
        c = 29
        for j in range(0, len(key)):
            h = (c * h + ord(key[j])) % list_1M_size
            #print("h: ", h)
        return (h + 2 * i) % list_1M_size


def lin_probing_insert(key):
    for i in range(0, list_1M_size):
        k = hashing_function_lin(key, i)
        if not list_1M[k]:
            list_1M[k] = key
            return True
    return False


def lin_get(key):  # ????????????????????????????
    i = 0
    for i in range(0, list_1M_size):
        k = hashing_function_lin(key, i)
        #print(i, "list_1M[k]: ", list_1M[k])
        if list_1M[k] == key:
            #print("hit : ", i + 1)
            return [True, i + 1]
        if not list_1M[k]:
            #print("miss: ", i + 1)
            return [False, i + 1]
    print("not found : ", i + 1)
    return False

# def lin_get(key):  # ????????????????????????????
#     i = 0
#     for i in range(0, list_1M_size):
#         k = hashing_function_lin(key, i)
#         if list_1M[k] == key:
#             print("found : ", i + 1)
#             return True
#     print("not found : ", i + 1)
#     return False


def hashing_function_double(key, i):
    if type(key) is str:
        h = 0
        c = 29
        for j in range(0, len(key)):
            h = (c * h + ord(key[j])) % list_1M_size
            # print("h: ", h)
        return ((h + 2 * i) % list_1M_size + i * 2 * (h + 2 * i) % (list_1M_size - 2) + 1) % list_1M_size
    if type(key) is list:
        if type(key[0]) is str:
            h = 0
            c = 29
            for j in range(0, len(key[0])):
                h = (c * h + ord(key[0][j])) % list_1M_size
                # print("h: ", h)
            return ((h + 2 * i) % list_1M_size + i * 2 * (h + 2 * i) % (list_1M_size - 2) + 1) % list_1M_size
        return (key[0] % list_1M_size + i * 2 * key[0] % (list_1M_size - 2) + 1) % list_1M_size
    return (key % list_1M_size + i * 2 * key % (list_1M_size - 2) + 1) % list_1M_size


def double_insert(key):
    for i in range(0, list_1M_size):
        k = hashing_function_double(key, i)
        if not list_1M[k]:
            list_1M[k] = key
            return True
    return False


def double_insert_book(key, _list):
    for i in range(0, list_1M_size):
        k = hashing_function_double(key, i)
        if not _list[k]:
            _list[k] = key
            return True
    return False


def double_get(key):
    i = 0
    for i in range(0, list_1M_size):
        k = hashing_function_double(key, i)
        if not list_1M[k]:
            return [False, i + 1]
        # print(key, " :::: ", list_1M[k])
        if type(list_1M[k]) is list and len(list_1M[k]) > 0:  # for phonebook
            if list_1M[k][0] == key:
                print(list_1M[k])
                return True
        if list_1M[k] == key:
            # print("found : ", i + 1)
            if type(key) is list:
                print(key)
            return [True, i+1]
    # print("not found : ", i + 1)
    return [False, i+1]


def double_get_book(key, book):
    i = 0
    for i in range(0, list_1M_size):
        k = hashing_function_double(key, i)
        if not book[k]:
            return [False, i + 1]
        # print(key, " :::: ", list_1M[k])
        if type(book[k]) is list and len(book[k]) > 0:  # for phonebook
            if book[k][0] == key:
                print(book[k])
                return True
        if book[k] == key:
            # print("found : ", i + 1)
            if type(key) is list:
                print(key)
            return [True, i+1]
    # print("not found : ", i + 1)
    return [False, i+1]



def run_hit_miss(table, _get):
    cnt_miss = 0
    cnt_m = 0

    cnt_hit = 0
    cnt_h = 0
    for record in table:

        if not _get(record)[0]:
            cnt_miss = cnt_miss + 1
            cnt_m = cnt_m + _get(record)[1]
        else:
            cnt_hit = cnt_hit + 1
            cnt_h = cnt_h + _get(record)[1]

    if cnt_miss:
        print("mean miss: ", cnt_m / cnt_miss)
    else:
        print("no misses")

    if cnt_hit:
        print("mean hit: ", cnt_h / cnt_hit)
    else:
        print("no hits")


#
# for i in range(int(0.5 * list_1M_size)):
#     lin_probing_insert(hash_table_input[i])
#
# insert into 'fill' of max size, fill is set at the beginning LINEAR PROBING INSERT and SEARCH
for i in range(int(fill * list_1M_size)):
    lin_probing_insert(hash_table_input[i])
    hit_table[i] = hash_table_input[i]


run_hit_miss(miss_table, lin_get)
run_hit_miss(hit_table, lin_get)

# # piece for double hash version:
# for i in range(int(fill * list_1M_size)):
#     double_insert(hash_table_input[i])
#     hit_table[i] = hash_table_input[i]
# run_hit_miss(hit_table, double_get)
# run_hit_miss(miss_table, double_get)

# for value in hash_table_input:
#     lin_probing_insert(value)

# for val in range(list_1M_size):
#     if list_1M[val]:
#         print(val, " : ", list_1M[val])

# ['ania', 666 111 111]
phone_book_entries = [[random.randint(100000000, 999999999), names[i % 18239]] for i in range(100000)]
phone_book_entries_by_names = [[phone_book_entries[i][1],phone_book_entries[i][0]] for i in range(len(phone_book_entries))]
phone_book = [[] for _ in range(100000)]
phone_book_1 = [[] for _ in range(100000)]
phone_book_2 = [[] for _ in range(100000)]


# phone book:
list_1M = phone_book
list_1M_size = len(phone_book)

for i in range(int(0.5 * list_1M_size)):
    double_insert_book(phone_book_entries[i], phone_book_1)  # hashing by phone
    double_insert_book(phone_book_entries_by_names[i], phone_book_2)  # hashing by name
print(phone_book_1)

contin = 'y'
while contin == 'y':
    print("1 - add number and name, 2 - search using number, 3 - search using name")
    user_input = input("Choice: ")
    if user_input == '1':
        user_input = input("number: ")
        user_input_2 = input("name: ")
        double_insert_book([int(user_input), user_input_2], phone_book_1)
        double_insert_book([user_input_2, int(user_input)], phone_book_2)
        list_1M_size = len(phone_book_1)

    if user_input == '2':
        user_input = input('enter number to find')
        double_get_book(int(user_input), phone_book_1)
    if user_input == '3':
        user_input = input('enter name to find')
        double_get_book(user_input, phone_book_2)
    contin = input("continue? y/n")


# # phone book:
# def pb():
#     phone_book_entries = [[random.randint(100000000, 999999999), names[i % 18239]] for i in range(100000)]
#     phone_book_entries_by_num = phone_book_entries
#     phone_book = [[] for _ in range(100000)]
#
#     list_1M = phone_book
#     list_1M_size = len(phone_book)
#
#     for i in range(int(0.5 * list_1M_size)):
#         double_insert(phone_book_entries[i])  # hashing by phone
#     print(list_1M)
#
#     contin = 'y'
#     while contin == 'y':
#         print("1 - add number and name, 2 - search using number, 3 - search using name")
#         user_input = input('enter number to find')
#         double_get(int(user_input))
#         contin = input("continue? y/n")
#
#
# pb()