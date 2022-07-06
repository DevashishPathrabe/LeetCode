class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0
        for log in logs:
            string = log[0:2]
            if string == "..":
                if operations > 0:
                    operations -= 1
                else:
                    operations = 0
            elif string != "./":
                operations += 1
        return operations