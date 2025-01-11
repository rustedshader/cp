def composite_check(x: int) -> bool:
    # All even numbers are composite
    if x % 2 == 0:
        return True
    if x <= 3:
        return False

    # Time complexity of O(rootN)
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return True
    return False


print(composite_check(100))
