class Validator:
    def isEmail(self, arr):
        res = 0
        for num in arr:
            res += num

        return res

    def isDomain(self, arr):
        if (len(arr) > 0):
            sum = self.getSum(arr)
            return sum / len(arr)
        else:
            return 0
    def isNumber:
        if (len(arr) > 0):
            sum = self.getSum(arr)
            return sum / len(arr)
        else:
            return 0