import itertools as it

def is_solution(perm1):
    for (i1, i2) in it.combinations(range(len(perm1)), 2):
        if abs(i1 - i2) == abs(perm1[i1] - perm1[i2]):
            return False

    return True

if __name__ == "__main__":
    for perm in it.permutations(range(12)):
        if is_solution(perm):
           print(perm)
           exit()