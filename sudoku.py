from random import shuffle
from PIL import Image, ImageDraw, ImageFont
from random import randint, choice

column_order = [[[2, 0, 0], [0, 1, 1], [1, 2, 2]], [[1, 0, 0], [2, 1, 1], [0, 2, 2]], [[0, 2, 0], [1, 0, 1], [2, 1, 2]], [[0, 1, 0], [1, 2, 1], [2, 0, 2]], [[0, 0, 2], [1, 1, 0], [2, 2, 1]], [[0, 0, 1], [1, 1, 2], [2, 2, 0]], [[0, 0, 0], [1, 1, 1], [2, 2, 2]], [[1, 2, 2], [2, 0, 0], [0, 1, 1]], [[0, 2, 2], [1, 0, 0], [2, 1, 1]], [[2, 1, 2], [0, 2, 0], [1, 0, 1]], [[2, 0, 2], [0, 1, 0], [1, 2, 1]], [[2, 2, 1], [0, 0, 2], [1, 1, 0]], [[2, 2, 0], [0, 0, 1], [1, 1, 2]], [[2, 2, 2], [0, 0, 0], [1, 1, 1]], [[0, 1, 1], [1, 2, 2], [2, 0, 0]], [[2, 1, 1], [0, 2, 2], [1, 0, 0]], [[1, 0, 1], [2, 1, 2], [0, 2, 0]], [[1, 2, 1], [2, 0, 2], [0, 1, 0]], [[1, 1, 0], [2, 2, 1], [0, 0, 2]], [[1, 1, 2], [2, 2, 0], [0, 0, 1]], [[1, 1, 1], [2, 2, 2], [0, 0, 0]]]
row_order = [[[2, 0, 1], [0, 1, 2], [0, 1, 2]], [[1, 2, 0], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [2, 0, 1], [0, 1, 2]], [[0, 1, 2], [1, 2, 0], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [2, 0, 1]], [[0, 1, 2], [0, 1, 2], [1, 2, 0]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[1, 2, 0], [2, 0, 1], [2, 0, 1]], [[0, 1, 2], [2, 0, 1], [2, 0, 1]], [[2, 0, 1], [1, 2, 0], [2, 0, 1]], [[2, 0, 1], [0, 1, 2], [2, 0, 1]], [[2, 0, 1], [2, 0, 1], [1, 2, 0]], [[2, 0, 1], [2, 0, 1], [0, 1, 2]], [[2, 0, 1], [2, 0, 1], [2, 0, 1]], [[0, 1, 2], [1, 2, 0], [1, 2, 0]], [[2, 0, 1], [1, 2, 0], [1, 2, 0]], [[1, 2, 0], [0, 1, 2], [1, 2, 0]], [[1, 2, 0], [2, 0, 1], [1, 2, 0]], [[1, 2, 0], [1, 2, 0], [0, 1, 2]], [[1, 2, 0], [1, 2, 0], [2, 0, 1]], [[1, 2, 0], [1, 2, 0], [1, 2, 0]]]

class Sudoku:
    def __init__(self, level = 1):
        base = [i + 1 for i in range(9)]
        shuffle(base)
        base = [base[0:3], base[3:6], base[6:9]]
        self.base = base
        self.row = ["123", "312", "231"]
        self.column = ["123", "312", "231"]
        self.order_row = choice(row_order)
        self.order_column = choice(row_order)
        self.sudoku = self.create(base)
        self.level = level
    def create(self, base):
        whole = []
        for i in range(3):
            three_rows = ["", "", ""]
            for ii in range(3):
                row = self.row[self.order_row[i][ii]]
                column = self.column[self.order_column[i][ii]]
                first = self.sort(base[int(row[0])-1], column)
                second = self.sort(base[int(row[1])-1], column)
                third = self.sort(base[int(row[2])-1], column)
                cols = [first, second, third]
                for a in range(3):
                    three_rows[a] += "".join(cols[a])
            whole.extend(three_rows)
        return whole
    def sort(self, who, how):
        new = []
        for i in how:
            new.append(str(who[int(i)-1]))
        return new
    def save(self, name = "sudoku.jpg", resolution = (500, 500)):
        img = Image.new("RGB", resolution, "white")
        font = ImageFont.truetype("Arial.ttf", 20)
        img_draw = ImageDraw.Draw(img)

        for i in range(8):
            w = 1
            if i == 2 or i == 5:
                w = 3
            img_draw.line((0, resolution[1]*(i+1)/9, resolution[1], resolution[1]*(i+1)/9), fill="black", width = w)
            img_draw.line((resolution[1]*(i+1)/9, 0,  resolution[1]*(i+1)/9, resolution[1]), fill="black", width = w)
        self.hide()
        for i, row in enumerate(self.sudoku):
            for ii, char in enumerate(row):
                if char != "*":
                    img_draw.text(font = font, xy = ((i+0.3)*resolution[0]/9, (ii+0.3)*resolution[1]/9), text = char, fill =(0,0,0))
        img.save(name)
    def hide(self):
        new = []
        for row in self.sudoku:
            new_row = ""
            for char in row:
                if randint(0,self.level):
                    char = "*"
                new_row += char
            new.append(new_row)
        self.sudoku = new
        return new

sudoku = Sudoku().save()