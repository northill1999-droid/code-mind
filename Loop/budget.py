def budget(lst):
    save = []
    left = 0
    for idx, expenses in enumerate(lst):
        left += 300
        save_money = 0

        if expenses > left:
            return f"-{idx+1}"

        if left - expenses >= 100:
            save_money = 100 * ((left - expenses) // 100)
            save.append(save_money)

        left = left - expenses - save_money
        print(f"budget: {expenses}, save money: {save_money}, left: {left}\nnext month: {left + 300}\n")

    final_money = sum(save) + sum(save)*0.2 + left
    return final_money


if __name__ == "__main__":
    # lst = list(map(int, input().split()))
    lst = [290, 230, 280, 200, 300, 170, 330, 50, 90, 80, 200, 60]
    if len(lst) != 12:
        print(False)
    else:
        print(budget(lst))
    