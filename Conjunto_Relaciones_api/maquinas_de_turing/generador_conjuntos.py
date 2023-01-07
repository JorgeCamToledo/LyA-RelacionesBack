import string, random

class GeneratorC():
    def randletter(self,x,y):
        return chr(random.randint(ord(x), ord(y)))

    def generate_letters(self):
        rand = self.randletter('a','f')
        rand = (rand, rand)[random.randint(0, 1)]
        return rand

    def generate_conjunto(self,lon):
        longitud_con = random.randint(0,lon)
        conjunto = []
        conjunto.append('{')
        if longitud_con > 0:
            for i in range(longitud_con):
                conjunto.append(self.generate_letters())
                if i < longitud_con-1:
                    conjunto.append(',')
                else:
                    conjunto.append('}')
            return conjunto
        else:
            conjunto.append('}')
            return conjunto
    

    def borrar_repetidos(self,list):
        new_list = []
        for item in list:
                if item not in new_list and item != ',':
                    new_list.append(item)
        conjunto = []
        for index, item in enumerate(new_list):
            conjunto.append(item)
            if index < len(new_list)-2 and index > 0:
                conjunto.append(',')
        return conjunto


    def generarRandom(self):
        stringc = ''.join(self.generate_conjunto(5)) +'E'+''.join(self.generate_conjunto(5)) 
        return stringc
    
    def generarIgualdad(self):
        conjunto = ''.join(self.generate_conjunto(5))
        stringc = conjunto +"E"+conjunto
        return stringc
    
    def generarPertenencia(self):
        letra = self.generate_letters()
        conjunto = ''.join(self.generate_conjunto(5))
        stringc = letra +'E'+conjunto
        return stringc
    
    def generarSubconjunto(self):
        conjunto = ''.join(self.generate_conjunto(2))
        conjunto2 = ''.join(self.generate_conjunto(7))
        stringc = conjunto +"E"+conjunto2
        return stringc

    def generar(self):
        choice = random.randint(0,100)
        print(choice)
        if choice >= 0 and choice < 50: return self.generarRandom()
        if choice > 49 and choice < 70: return self.generarIgualdad()
        if choice > 69 and choice < 80: return self.generarPertenencia()
        if choice > 79 and choice <=100: return self.generarSubconjunto()


