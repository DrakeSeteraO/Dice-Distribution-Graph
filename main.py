import matplotlib.pyplot as plt


def create_list(die_amount: int) -> list:
    lst = [[0 for i in range(die_amount)] for j in range(die_amount * 6)]
    for i in range(6):
        lst[i][0] = 1
    return lst


def calculate_amount(lst: list, die_amount: int) -> list:
    for i in range(die_amount * 6):
        for j in range(die_amount - 1):
            total = 0
            for k in range(1, 7):
                if i - k >= 0:
                    total += lst[i - k][j]
            lst[i][j + 1] = total
    return lst


def main():
    die_amount = int(input('How many dice would you like to calculate for? '))
    if die_amount < 1:
        die_amount = 1
    
    amount = create_list(die_amount)
    amount = calculate_amount(amount, die_amount)
    total = [0] * (die_amount * 6)
    for i in range(len(amount)):
        total[i] = amount[i][-1]
    everything = sum(total)
    for i in range(len(amount)):
        total[i] = total[i] / everything
    
    name = [0] * (die_amount * 6)
    for i in range(len(total)):
        name[i] = i
        
    plt.bar(name, total,width = 1, align='edge')
    plt.title('Dice Distribution')
    plt.xlabel('Dice Sum')
    plt.ylabel('Percentage of possibilities')
    plt.show()


if __name__ == '__main__':
    main()