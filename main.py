

class Koshy:

    def __init__(self):
        # X нулевое У нулевое
        # итые для рассчета новой строки подставить икс игрек итые
        self.x_0 = -1
        self.y_0 = -5

        # эйч!
        self.h = 0.6

        self.fi_1 = None
        self.fi_2 = None
        self.fi_3 = None
        self.fi_4 = None
        self.y_next = None

    def printer(self):
        print("x_0 y_0", self.x_0, self.y_0)
        print("fi_1", self.fi_1)
        print("fi_2", self.fi_2)
        print("fi_3", self.fi_3)
        print("fi_4", self.fi_4)
        print("y->next", self.y_next)

    @staticmethod
    def f_1_func(x, y):
        # функция f(x,y)
        x_3 = x*x*x
        xy = x*y
        xy2 = xy/2
        result = x_3 - xy2
        return result

    def f_1(self):
        func = self.f_1_func(x=self.x_0, y=self.y_0)
        result = self.h * func
        return result

    def f_2_func(self):
        x = self.x_0 + (self.h/2)
        y = self.y_0 + (self.fi_1 / 2)
        result = self.f_1_func(x=x, y=y)
        return result

    def f_2(self):
        func = self.f_2_func()
        result = self.h * func
        return result

    def f_3_func(self):
        x = self.x_0 + (self.h / 2)
        y = self.y_0 + (self.fi_2 / 2)
        result = self.f_1_func(x=x, y=y)
        return result

    def f_3(self):
        func = self.f_3_func()
        result = self.h * func
        return result

    def f_4_func(self):
        x = self.x_0 + self.h
        y = self.y_0 + self.fi_3
        result = self.f_1_func(x=x, y=y)
        return result

    def f_4(self):
        func = self.f_4_func()
        result = self.h * func
        return result

    def next_y(self):
        func = self.fi_1 + (2 * self.fi_2) + (2 * self.fi_3) + self.f_4()
        func = 1/6 * func
        result = self.y_0 + func
        return result

    def go(self):

        self.fi_1 = self.f_1()
        self.fi_2 = self.f_2()
        self.fi_3 = self.f_3()
        self.fi_4 = self.f_4()
        self.y_next = self.next_y()
        self.printer()


test = Koshy()
test.go()
