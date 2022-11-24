import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']

large = ["nemo" for i in range(100000)]


def find_nemo(array):
    t0 = time.time()
    for i in range(len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!")
            break
    t1 = time.time()
    print(f"Search took {t1 - t0} seconds.")


# find_nemo(nemo)
# find_nemo(everyone)
find_nemo(large)


# O(n) runs multiple times because it is in a loop
# O(1) only runs once

# Fun Challenge
def fun_challenge(user_input):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in range(len(user_input)):  # O(n)
        stranger = True  # O(n)
        a += 1  # O(n)
    return a  # O(1)


# BIG O NOTATION
# BIG O(3 + 4n) = O(n)

# Second Fun Challenge
def another_fun_challenge(user_input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    for i in range(len(user_input)):  # O(n)
        x = i + 1  # O(n)
        y = i + 2  # O(n)
        z = i + 3  # O(n)

    for j in range(len(user_input)):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    who_am_i = "I don't know"  # O(1)

# BIG O NOTATION
# Big O(4 + 5n) = O(n)

# Rule Book for Big O
# Rule 1: Worst Case
# - Always assume the worst case; can't assume things will go well
# Rule 2: Remove Constants
# - Constant numbered values such as '1' or '100' always get removed (ex. O(n + 1(100)) removes the numerical value for
# just O(n)
# Rule 3: Different terms for inputs
# Rule 4: Drop Non Dominants
