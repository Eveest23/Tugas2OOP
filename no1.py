class Bilangan:
    def __init__(self, n):
        self.n = n

    def tampil_bilangan(self):
        with open('output.txt', 'a') as file:
            for i in range(1, self.n+1):
                print(i, end=' ')
                file.write(str(i) + ' ')
