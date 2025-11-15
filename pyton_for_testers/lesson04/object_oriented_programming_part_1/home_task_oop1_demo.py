import statistics

class Demo:

    def handle_numbers(self, numbers):
        print('The minimum number of the list is: ' + str(self.min_number(numbers)))
        print('The maximum number of the list is: ' + str(self.max_number(numbers)))
        print('The average number of the list is: ' + str(self.averge_number(numbers)))

    def min_number(self,numbers):
        return min(numbers)

    def max_number(self,numbers):
        return max(numbers)

    def averge_number(self, numbers):
        if not numbers:  # בדיקה שהרשימה לא ריקה
            return "הרשימה ריקה"
        average = statistics.mean(numbers)
        return average

demo1=Demo()
demo1.handle_numbers([1,3,5])



