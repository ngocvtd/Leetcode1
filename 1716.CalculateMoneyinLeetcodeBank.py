class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        money = 1
        monday_money = 1

        for day in range(1, n + 1):
            total += money
            money += 1

            if day % 7 == 0:
                money = monday_money + 1
                monday_money += 1

        return total
