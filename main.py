#

from re import S


unsorted_list = [33, 22, 19, 27, 6, 2, 31, 10, 1]

# Write your solution for algorithm 1 below


def algo1(unsorted):
    s = unsorted.copy()
    s.sort()
    return s


print(algo1(unsorted_list))


# Write your solution for algorithm 2 below


def algo2(unsorted):
    return sorted(unsorted)


print(algo2(unsorted_list))


# Write your solution for algorithm 3 below


def algo3(unsorted):
    return sorted(unsorted, reverse=True)


print(algo3(unsorted_list))


# 4

def algo4(string_sentence):
    lst = string_sentence.split(" ")
    return sorted(lst, key=lambda word: word[0])


sample = "I love software engineering"
print(algo4(sample))


# 5

def algo5(int_list, target=11):
    s = sorted(int_list)

    i = 0
    j = len(int_list) - 1

    left = s[i]
    right = s[j]

    while (left < right):
        sum = left + right
        if sum == target:
            return [left, right]
        elif sum < target:
            i = i+1
            left = s[i]
        else:
            j = j-1
            right = s[j]
    return f"no pairs sum to target = {target}"


print(algo5(unsorted_list))
print(algo5(unsorted_list, target=46))
print(algo5(unsorted_list, target=53))
print(algo5(unsorted_list, target=17))
