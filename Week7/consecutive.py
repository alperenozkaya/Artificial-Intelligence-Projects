sequence = 'TTTTTHHHHH' * 1000
#print(sequence)
print(len(sequence))


def check_outputs(f, s):
    count = 0
    total = 0
    for i in range(0, len(sequence)):
        if sequence[i] == f:
            total += 1
            if i + 1 < len(sequence):
                if sequence[i + 1] == s:
                    count += 1
    return count, total

def main():
    print('Enter the first side(T or H):')
    first = input()
    print('Enter the second side(T or H):')
    second = input()
    count, total = check_outputs(first, second)

    prob = float(count / total)
    print(prob)

main()



