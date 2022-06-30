def solution(xs):
    pos_max, neg_max, rol_max = xs[0], xs[0], xs[0]
    for val in xs[1:]:
        if val != 0:
            temp = max(max(val, val * pos_max), val * neg_max)
            neg_max = min(min(val, val * pos_max), val * neg_max)
            pos_max = temp
            rol_max = max(rol_max, pos_max)
    return str(rol_max)


def main():
    # case 1
    array1 = [2, 0, 2, 2, 0]
    print("-- Case 1 --")
    print("Expected output: 8")
    print(f"Actual output: {solution(array1)}\n")

    # case 2
    array2 = [-2, -3, 4, -5]
    print("-- Case 2 --")
    print("Expected output: 60")
    print(f"Actual output: {solution(array2)}\n")

    # case 3
    array3 = [2, -3, 1, 0, -5]
    print("-- Case 3 --")
    print("Expected output: 30")
    print(f"Actual output: {solution(array3)}")


if __name__ == "__main__":
    main()