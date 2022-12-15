class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
             self.ligada = True
    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

#print(__name__)
if __name__ == '__main__':
    televisao = Televisao()
    print(f'televisão ligada? {televisao.ligada}')
    televisao.power()
    print(f'televisão ligada? {televisao.ligada}')
    televisao.power()
    print(f'televisão ligada? {televisao.ligada}')
    print(f'canal: {televisao.canal}')
    print(f'televisão ligada? {televisao.ligada}')
    televisao.aumenta_canal()
    televisao.power()
    print(f'televisão ligada? {televisao.ligada}')
    televisao.aumenta_canal()
    print(f'canal: {televisao.canal}')
    televisao.diminui_canal()
    print(f'canal: {televisao.canal}')
