class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for el in self.my_list:
            for i in el:
                print(f"{i:2}", end="  ")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
new_m = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(new_m)
print(m.__add__(new_m))