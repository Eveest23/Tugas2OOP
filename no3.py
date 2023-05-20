class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def hitung_luas(self):
        luas = 0.5 * self.alas * self.tinggi
        with open('output.txt', 'a') as file:
            file.write('\n\nalas = {}\ntinggi = {}\nluas = 0.5 x {} x {} = {}'.format(self.alas, self.tinggi, self.alas, self.tinggi, luas))
        print('alas = ', self.alas)
        print('tinggi = ', self.tinggi)
        print('luas = 0.5 x', self.alas, 'x', self.tinggi, '=', luas)