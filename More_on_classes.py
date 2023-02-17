class Colors:
    def __init__(self, f_color):
        self.f_color = f_color
    def check(self):
        colors = ['Blue', 'Red', 'Yellow', 'White']
        if self.f_color.capitalize() in colors:
            print('Correct')
        else:
            print('incorrect')
    def hint(self):
        print('''Choose between the following colors: 
        Blue, Red, Yellow, white.
        ''')
    def solution(self):
        print('''The correct answer is one of the following colors: 
        Blue, Red, Yellow, white.
        ''')
        
q1 = Colors("RED")
print('\n',q1.f_color,'\n')
q1.check()
print('\n')
q1.hint()
print('\n')
q1.solution()