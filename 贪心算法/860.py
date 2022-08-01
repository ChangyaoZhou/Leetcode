def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    一共有三种情况；
        情况一：账单是5，直接收下。
        情况二：账单是10，消耗一个5，增加一个10
        情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5
    ***贪心思想: 因为美元10只能给账单20找零，而美元5可以给账单10和账单20找零，美元5更万能！
               所以要满足局部最优：遇到账单20，优先消耗美元10，完成本次找零。全局最优：完成全部账单的找零。
    """
    five, ten, twenty = 0, 0, 0
    for pay in bills:
        if pay == 5:
            five += 1
        elif pay == 10:
            ten += 1
            five -= 1
        else:
            twenty += 1
            if ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
        if five < 0:
            return False
    return True

bills = [5,5,5,5,20,20,5,5,5,5]
print(lemonadeChange(bills))