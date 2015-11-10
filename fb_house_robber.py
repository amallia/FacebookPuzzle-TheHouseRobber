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
        elif i == 1:
            mem[1] = max(mem[0], amounts[1])
        else:
            mem[i] = max(mem[i-2] + amounts[i], mem[i-1])

    robs = []
    i=len(amounts)-1
    while (i>=0):
        if(i>=2):
            if mem[i] == mem[i-2] + amounts[i]:
                robs.append(i)
                i = i-2
            else:
                i = i-1
        elif (i == 1):
            if mem[i] == amounts[i]:
                robs.append(i)
                i=-1
            else:
                i=0
        else:
            robs.append(i)
            i=-1
    robs.reverse()
    print "Best rob: ",mem[len(amounts)-1]
    print "Robbed houses", robs