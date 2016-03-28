# staircase.py


class Solution(object):

    def staircase(self, n):
        result = ''
        for i in range(1, n+1):
            for j in range(1, n+1):
                result += '#' if n-i < j else ' '
            result += '\n'
        return result

    def main(self):
        n = int(input())
        result = self.staircase(n)
        print(result, end='')

if __name__ == '__main__':
    Solution().main()
