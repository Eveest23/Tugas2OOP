class PersegiPanjang:
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def hitung_luas(self):
        luas = self.p * self.l
        with open('output.txt', 'a') as file:
            file.write('\n\npanjang = {}\nlebar = {}\n luas = {} x {} = {}'.format(self.p, self.l, self.p, self.l, luas))
        print('panjang = ', self.p)
        print('lebar = ', self.l)
        print('luas = ', self.p, 'x', self.l, '=', luas)