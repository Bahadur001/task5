class Sum():
    def __init__(self, my_list):
        self.my_list = my_list

    def iki_ededin_cemi(self):
        return [(self.my_list[i] + self.my_list[j])
                for i in range(len(self.my_list))
                for j in range(i+1, len(self.my_list))]
    
    def netice(self, reqem):
        for toplam in self.iki_ededin_cemi():
            if reqem == toplam:
                return f"{reqem} listde var."
        return f"{reqem} ."

sum_goster = Sum([1, 2, 3, 4, 5])
result = sum_goster.iki_ededin_cemi()
print("cemi:", result)

metod_ikinci_reqem = 6
mesaj = sum_goster.netice(metod_ikinci_reqem)
print(mesaj)
