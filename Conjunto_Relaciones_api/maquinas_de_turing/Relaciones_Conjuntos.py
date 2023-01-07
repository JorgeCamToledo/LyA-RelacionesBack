from Conjunto_Relaciones_api.maquinas_de_turing.pertenencia import Pertenencia
from Conjunto_Relaciones_api.maquinas_de_turing.disjuntos import Disjuntos
from Conjunto_Relaciones_api.maquinas_de_turing.igualdad import Igualdad
from Conjunto_Relaciones_api.maquinas_de_turing.generador_conjuntos import GeneratorC
from Conjunto_Relaciones_api.maquinas_de_turing.sub_propio import Subconjunto_Propio
from Conjunto_Relaciones_api.maquinas_de_turing.subconjunto import Subconjunto
from Conjunto_Relaciones_api.maquinas_de_turing.AFD_conjunto import AFD_Conjunto

class Relaciones():
    def obtener_relaciones(self,conjunto):
        MT_disjuntos = Disjuntos()
        MT_igualdad = Igualdad()
        MT_sub_propio = Subconjunto_Propio()
        MT_subconjunto = Subconjunto()
        MT_pertenencia = Pertenencia()
        conjuntos = conjunto.split("E")
        validA = self.validar_conjunto(conjuntos[0])
        validB = self.validar_conjunto(conjuntos[1])
        disjuntos = MT_disjuntos.reglas_disjunto(conjunto)
        igualdad = MT_igualdad.reglas_igualdad(conjunto)
        sub_propio = MT_sub_propio.reglas_sub_propio(conjunto)
        subconjunto= MT_subconjunto.reglas_subconjunto(conjunto)
        pertenencia = MT_pertenencia.reglas_pertenencia(conjunto)
        if validA == 'Valor' and validB == 'Conjunto':
            relaciones_dict = {
            "Disjuntos": "Disjuntos",
            "Igualdad": "No Iguales",
            "Subconjunto": "A no es subconjunto de B",
            "Subconjunto_Propio": "A no es subconjunto propio de B",
            "Pertenencia": pertenencia,
            "A":conjuntos[0],
            "A_isValid": validA,
            "B": conjuntos[1],
            "B_isValid":validB,
        }
            return relaciones_dict
        if validA == 'Conjunto' and validB == 'Conjunto':

            relaciones_dict = {
                "Disjuntos": disjuntos,
                "Igualdad": igualdad,
                "Subconjunto": subconjunto,
                "Subconjunto_Propio": sub_propio,
                "Pertenencia": "El elemento no pertenece al conjunto",
                "A":conjuntos[0],
                "A_isValid": validA,
                "B": conjuntos[1],
                "B_isValid":validB,
            }
            return relaciones_dict

        if validA == 'no validado' or validB == 'no validado':
            relaciones_dict = {
                "A":conjuntos[0],
                "A_isValid": validA,
                "B": conjuntos[1],
                "B_isValid":validB,
            }
            return relaciones_dict
        if validB == 'Valor' or validB == 'Valor':
            relaciones_dict = {
                'req':'se requiere un conjunto en b',
                "A":conjuntos[0],
                "A_isValid": validA,
                "B": conjuntos[1],
                "B_isValid":validB,
            }
            return relaciones_dict
    
    def ejercicio(self):
        generador = GeneratorC()
        conjuntoAutomatico = generador.generar()
        print(conjuntoAutomatico)
        print(self.obtener_relaciones)


    def validar_conjunto(self,text):
        AFD = AFD_Conjunto()
        validacion = AFD.reglas_AFD_conjunto(text)
        return validacion