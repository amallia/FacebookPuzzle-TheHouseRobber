import argparse

if __name__ == '__main__':
    argparse = argparse.ArgumentParser(description="Facebook Puzzle: maximize the total robbed amount")
    argparse.add_argument("-i", dest="input", metavar="<g_1,g_2,...,g_n>", required=True)
    args = argparse.parse_args()
    amounts = [int(x) for x in args.input.split(",")]
    mem = [-1,]*len(amounts)

    for i in range(0,len(amounts)):
        if i == 0:
            mem[0] = amounts[0]
            print amounts[0]
        elif i == 1:
            mem[1] = max(mem[0], amounts[1])
            print amounts[1]
        else:
            mem[i] = max(mem[i-2] + amounts[i], mem[i-1])
            print amounts[i]

    print "Best rob: ",mem[len(amounts)-1]