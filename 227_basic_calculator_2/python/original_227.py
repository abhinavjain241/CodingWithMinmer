class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        last_number, curr_number = 0, 0
        result = 0
        operation = '+'
        for i, current in enumerate(s):
            if current.isdigit():
                curr_number = curr_number * 10 + int(current)
            if (not current.isdigit() and current != " ") or i == len(s) - 1:
                match operation:
                    case '-' | '+':
                        result += last_number
                        last_number = curr_number if operation == '+' else -curr_number
                    case '*':
                        last_number *= curr_number
                    case '/':
                        last_number = int(last_number / curr_number)
                operation = current
                curr_number = 0
        result += last_number
        return result