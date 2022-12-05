def load_elf_cals(fname):
    """Build the list of elf carrying calories"""
    ecal = []
    count = 0
    with open('data/' + fname) as inf:
        content = inf.read().splitlines()
        for line in content:
            if len(line) == 0:
                ecal.append(count)
                count = 0
            else:
                count += int(line)
        if count > 0:
            ecal.append(count)
    return ecal


def elf_max_calories(fname):
    """Find the elf carrying the most calories and report how many he has"""
    elf_cals = load_elf_cals(fname)
    print(elf_cals)

    elf_cals.sort()
    print(elf_cals)
    return elf_cals[-1]


ans = elf_max_calories('test_01a.txt')
print(f'Elf max calories is {ans} - should be 24000')
