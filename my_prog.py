class lst_com():
    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2
        flag = 0
        i = 0
        for s1 in self.lst1:
                if s1 != self.lst2[i]:
                    flag = 1
                i += 1
        if flag is 0:
            print("lists are equal")
        else:
            print("unequal")


if __name__ == "__main__":
    l1 = ["a", "b", "c"]
    l2 = ["a", "b", "c"]
    lst = lst_com(l1, l2)
