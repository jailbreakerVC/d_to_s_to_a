import re


def main():
    sum = 0
    N = int(input())
    if N > 0:
        inp = (input())
        match inp:
            case _ if len(inp) > 1:
                print("does this mean, more than one input?")
            case _:
                print("only one input")

    # do not use a for loop
    for i in range(N):
        x = int(input())
        if x < 0:
            pass
        sum += (x**2)
    print(sum)


if __name__ == "__main__":
    main()
