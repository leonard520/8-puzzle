import sys

class EightPuzzleList():
    def __init__(self, s, f):
        self.status = s
        self.f_value = f
        self.g_value = 0

class EightPuzzle():
    open_list = []
    close_list = []
    #def __init__(self):
    def print_open_list(self):
        for i in self.open_list:
            self.print_chess(i)

    def print_chess(self, item):
        print item.g_value
        for i in range(0, 9):
            sys.stdout.write(str(item.status[i]) + " ")
            if i % 3 == 2:
                sys.stdout.write("\n")

    def is_done(self, status):
        for i in range(0, 8):
            if(status[i] != i + 1):
                return False
        return True

    def f(self, status):
        # calculate hamming distance
        hamming = 0
        for i in range(0, 8):
            if status[i] != i + 1:
                hamming += 1
        return hamming

    def g(self, status):
        # calculate manhattan distance (city block distance)
        manhattan = 0
        for i in range(0, 9):
            if(status[i] == 0):
                continue
            manhattan += abs(int((status[i] - 1) / 3) - int(i / 3)) + abs(int((status[i] - 1) % 3) - int(i % 3))
        return manhattan

    def next(self):
        status = self.open_list[0].status
        if self.is_done(status):
            print "depth " + str(self.open_list[0].f_value)
            return True
        obj = self.open_list[0]
        self.close_list.append(status)
        self.open_list.remove(obj)
        current_f = obj.f_value
        for i in range(0, 9):
            if(status[i] == 0):
                # find 0
                x = i % 3
                y = i / 3
                # print "x:" + str(x) + " y:" + str(y) + " i:" + str(i)
                break
        if x > 0: # left
            left = list(status)
            left[i] = status[i - 1]
            left[i - 1] = 0
            l_item = EightPuzzleList(left, current_f + 1)
            l_item.g_value = self.g(left) + current_f + 1
            if left not in self.close_list:
                self.open_list.append(l_item)
        if y > 0: # top
            top = list(status)
            top[i] = status[i - 3]
            top[i - 3] = 0
            t_item = EightPuzzleList(top, current_f + 1)
            t_item.g_value = self.g(top) + current_f + 1
            if top not in self.close_list:
                self.open_list.append(t_item)
        if x < 2: # right
            right = list(status)
            right[i] = status[i + 1]
            right[i + 1] = 0
            r_item = EightPuzzleList(right, current_f + 1)
            r_item.g_value = self.g(right) + current_f + 1
            if right not in self.close_list:
                self.open_list.append(r_item)
        if y < 2: # bottom
            bottom = list(status)
            bottom[i] = status[i + 3]
            bottom[i + 3] = 0
            b_item = EightPuzzleList(bottom, current_f + 1)
            b_item.g_value = self.g(bottom) + current_f + 1
            if bottom not in self.close_list:
                self.open_list.append(b_item)
        self.open_list.sort(key=lambda x: x.g_value)
        return False

    def run(self, start):
        self.open_list.append(start)
        flag = next(self)
        while flag == False and len(self.open_list) > 0:
            flag = next(self)

if __name__ == "__main__":
    puzzle = EightPuzzle()
    # status = [8,1,3,4,0,2,7,6,5]
    # status = [2, 6, 0, 3, 1, 7, 5, 8, 4]
    status = [0, 2, 3, 1, 4, 6, 7, 5, 8]
    game_start = EightPuzzleList(status, 0)
    puzzle.run(game_start)
