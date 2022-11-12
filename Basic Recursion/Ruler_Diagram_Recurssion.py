class EnglishRuler:
    def __init__(self, num_inches, major_length):
        self.__num_inches = num_inches
        self.__major_length = major_length

    def draw_line(self, tick_length, tick_label=''):
        line = '-'*tick_length
        if tick_label:
            line += ' '+tick_label
        print(line)

    def draw_interval(self, center_length):  # to draw interior
        if center_length > 0:
            self.draw_interval(center_length - 1)
            self.draw_line(center_length)
            self.draw_interval(center_length - 1)

    def draw_ruler(self):
        self.draw_line(self.__major_length,'0')
        for j in range(1,1+self.__num_inches):
            self.draw_interval(self.__major_length - 1)
            self.draw_line(self.__major_length, str(j))

if __name__ == '__main__':
    ruler = EnglishRuler(5,6)
    ruler.draw_ruler()