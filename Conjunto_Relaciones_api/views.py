from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Conjunto_Relaciones_api.maquinas_de_turing.Relaciones_Conjuntos import Relaciones
from Conjunto_Relaciones_api.maquinas_de_turing.generador_conjuntos import GeneratorC
from Conjunto_Relaciones_api.maquinas_de_turing.Relaciones_Conjuntos import Relaciones
import json

class RelacionesConjuntos(APIView):

    def createJson(self,message,data,status):
        custom={"messages":message,"pay_load":data,"status":status}
        auxiliar=json.dumps(custom)
        responseOk=json.loads(auxiliar)
        return responseOk


    def get(self, request, format=None):
        responseOk=self.createJson("succes","", status =status.HTTP_200_OK)
        return Response(responseOk)

    def post(self, request, format=None):
        RL = Relaciones()
    

        #Borrar valores innecesarios del request
        datos = request.data
        conjunto = str(datos)
        size = 13 - len(conjunto) 
        conjunto = (conjunto[size:])
        size =len(conjunto)-2
        conjunto = (conjunto[:size])

        #Obtener las relaciones del conjunto
        relaciones = RL.obtener_relaciones(conjunto)
        json.dumps(relaciones)
        responseOk=self.createJson("succes",relaciones, status =status.HTTP_200_OK)
        return Response(responseOk)

class EjercicioRelacion(APIView):
        def createJson(self,message,data,status):
            custom={"messages":message,"pay_load":data,"status":status}
            auxiliar=json.dumps(custom)
            responseOk=json.loads(auxiliar)
            return responseOk

        def post(self,request, format=None):
            GT = GeneratorC()
            RL = Relaciones()
            conjunto = GT.generar()
            relaciones = RL.obtener_relaciones(conjunto)
            relaciones['conjunto'] = conjunto
            json.dumps(relaciones)
            responseOk=self.createJson("succes",relaciones, status =status.HTTP_200_OK)
            return Response(responseOk)

class ValidacionConjunto(APIView):
        def createJson(self,message,data,status):
            custom={"messages":message,"pay_load":data,"status":status}
            auxiliar=json.dumps(custom)
            responseOk=json.loads(auxiliar)
            return responseOk

        def post(self,request, format=None):
            RL = Relaciones()

            datos = request.data
            conjunto = str(datos)
            size = 13 - len(conjunto) 
            conjunto = (conjunto[size:])
            size =len(conjunto)-2
            conjunto = (conjunto[:size])

            validacion = RL.validar_conjunto(conjunto)
            json.dumps(validacion)
            responseOk=self.createJson("succes",validacion, status =status.HTTP_200_OK)
            return Response(responseOk)


        


# Create your views here.
