
class Disjuntos():
    def turing_M(self,
                state = None, # Los estados de la MT
                blank = None, # El simbolo que representa blanco
                rules = [], # reglas para las transiciones
                tape = [], # cinta
                final = None,# Estado final
                final2 = None,
                position = 0 #posicion del cabezal
                ):
        st = state
        if not tape: tape = [blank]
        if position < 0: position += len(tape)
        if position >= len(tape) or position < 0: raise Exception("Se inicializo mal la posicion")
        SV = ''
        rules = dict(((s0,v0),(v1,dr,s1)) for (s0,v0,v1,dr,s1) in rules)
        """
        Estado         Simbolo a leer       Simbolo a escribir       Mov     Sig. EStado
        q0(s0)            {(v0)                  {(v1)             D(dr)      q1(s1)
        """
        while True:
            print(st,'\t', end = '  ')
            for i, v in enumerate(tape):
                if i == position:
                    print("[%s]"%(v,),end=" ")
                else: print (v, end=" ")
            print()
            print('valor de SV '+SV)

            if st == final or st == final2:
                if st == 'q8':
                    return 'No disjuntos'
                if st == 'q13':
                    return 'Disjuntos'

               
            if (st, tape[position]) not in rules:
                return 'No valido'

            (v1,dr,s1) = rules[(st,tape[position])]
            if st == 'q3' and SV == v1:
                v1 = '*'
            if st == 'q4' and SV == v1:
                v1 = '*'
            if st == 'q6' and SV ==v1:
                s1 = 'q7'
            if st == 'q6' and SV !=v1:
                s1 = 'q9'


            if st == 'q10' and SV != v1:
                dr = 'left'
            if st == 'q10' and SV == v1:
                s1 = 'q11'
                dr = 'right'
            tape[position] = v1

            
            if st == 'q1' and (v1 =='a' or v1 =='b' or v1 =='c'or v1 =='d' or v1 =='e'or v1 =='f'or v1 =='g'or v1 =='h'or v1 =='i'or v1 =='j'or v1 =='k'or v1 =='l'or v1 =='n'or v1 =='m'or v1 =='o'or v1 =='p'or v1 =='q'or v1 =='r'or v1 =='s'or v1 =='t'or v1 =='u'or v1 =='w'or v1 =='v'or v1 =='x'or v1 =='y'or v1 =='z' or v1 =='0' or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or v1 =='6' or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1
            if st == 'q11' and (v1 =='a' or v1 =='b' or v1 =='c'or v1 =='d' or v1 =='e'or v1 =='f'or v1 =='g'or v1 =='h'or v1 =='i'or v1 =='j'or v1 =='k'or v1 =='l'or v1 =='n'or v1 =='m'or v1 =='o'or v1 =='p'or v1 =='q'or v1 =='r'or v1 =='s'or v1 =='t'or v1 =='u'or v1 =='w'or v1 =='v'or v1 =='x'or v1 =='y'or v1 =='z' or v1 =='0' or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or v1 =='6' or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1

                
            if dr == 'left':
                if position > 0: position -= 1
                else: tape.insert(0, blank)
            if dr == 'right':
                position += 1
                if position >= len(tape): tape.append(blank)

            st = s1

    def reglas_disjunto(self,conjunto):

        validacion = self.turing_M(
                state = 'q0', # Estado inicial
                blank = 'B', # El simbolo que representa blanco
                tape = list(conjunto), # cinta
                final = 'q8',# Estado final
                final2 = 'q13',
                rules = map(tuple,
                [
                    'q0 { { right q1'.split(),
                    'q1 } } right q14'.split(),'q1 a a right q2'.split(), 'q1 b b right q2'.split(), 'q1 c c right q2'.split(), 'q1 d d right q2'.split(), 'q1 e e right q2'.split(), 'q1 f f right q2'.split(), 'q1 g g right q2'.split(), 'q1 h h right q2'.split(), 'q1 i i right q2'.split(), 'q1 j j right q2'.split(),'q1 k k right q2'.split(),'q1 l l right q2'.split(),'q1 m m right q2'.split(),'q1 n n right q2'.split(),'q1 o o right q2'.split(),'q1 p p right q2'.split(),'q1 q q right q2'.split(),'q1 r r right q2'.split(),'q1 s s right q2'.split(),'q1 t t right q2'.split(),'q1 u u right q2'.split(),'q1 v v right q2'.split(),'q1 w w right q2'.split(),'q1 x x right q2'.split(),'q1 y y right q2'.split(),'q1 z z right q2'.split(),'q1 1 1 right q2'.split(),'q1 2 2 right q2'.split(),'q1 3 3 right q2'.split(),'q1 4 4 right q2'.split(),'q1 5 5 right q2'.split(),'q1 6 6 right q2'.split(),'q1 7 7 right q2'.split(),'q1 8 8 right q2'.split(),'q1 9 9 right q2'.split(),'q1 0 0 right q2'.split(),
                    'q2 , , right q3'.split(), 'q2 } } right q4'.split(),
                    'q3 * * right q2'.split(),'q3 a a right q2'.split(), 'q3 b b right q2'.split(), 'q3 c c right q2'.split(),  'q3 d d right q2'.split(), 'q3 e e right q2'.split(), 'q3 f f right q2'.split(),'q3 g g right q2'.split(), 'q3 h h right q2'.split(), 'q3 i i right q2'.split(), 'q3 j j right q2'.split(), 'q3 k k right q2'.split(), 'q3 l l right q2'.split(), 'q3 m m right q2'.split(),'q3 n n right q2'.split(), 'q3 o o right q2'.split(),'q3 p p right q2'.split(),'q3 q q right q2'.split(),'q3 r r right q2'.split(),'q3 s s right q2'.split(),'q3 t t right q2'.split(),'q3 u u right q2'.split(),'q3 v v right q2'.split(),'q3 w w right q2'.split(),'q3 x x right q2'.split(),'q3 y y right q2'.split(), 'q3 z z right q2'.split(),'q3 1 1 right q2'.split(),'q3 2 2 right q2'.split(),'q3 3 3 right q2'.split(),'q3 4 4 right q2'.split(),'q3 5 5 right q2'.split(),'q3 6 6 right q2'.split(),'q3 7 7 right q2'.split(),'q3 8 8 right q2'.split(),'q3 9 9 right q2'.split(),'q3 0 0 right q2'.split(),
                    'q4 D D right q5'.split(),'q4 E E right q5'.split(),
                    'q5 { { right q6'.split(),
                    'q6 } } right q15'.split(),'q6 a a right q7'.split(), 'q6 b b right q7'.split(), 'q6 c c right q7'.split(), 'q6 d d right q7'.split(), 'q6 e e right q7'.split(), 'q6 f f right q7'.split(), 'q6 g g right q7'.split(), 'q6 h h right q7'.split(),'q6 i i right q7'.split(), 'q6 j j right q7'.split(), 'q6 k k right q7'.split(),'q6 l l right q7'.split(),'q6 m m right q7'.split(),'q6 n n right q7'.split(), 'q6 o o right q7'.split(),'q6 p p right q7'.split(), 'q6 q q right q7'.split(), 'q6 r r right q7'.split(), 'q6 s s right q7'.split(), 'q6 t t right q7'.split(), 'q6 u u right q7'.split(),'q6 v v right q7'.split(), 'q6 w w right q7'.split(), 'q6 x x right q7'.split(),'q6 y y right q7'.split(),'q6 z z right q7'.split(),'q6 1 1 right q7'.split(),'q6 2 2 right q7'.split(),'q6 3 3 right q7'.split(),'q6 4 4 right q7'.split(),'q6 5 5 right q7'.split(),'q6 6 6 right q7'.split(),'q6 7 7 right q7'.split(),'q6 8 8 right q7'.split(),'q6 9 9 right q7'.split(),'q6 0 0 right q7'.split(),
                    'q7 a a right q7'.split(), 'q7 b b right q7'.split(), 'q7 c c right q7'.split(),'q7 d d right q7'.split(), 'q7 e e right q7'.split(),'q7 f f right q7'.split(),'q7 g g right q7'.split(),'q7 h h right q7'.split(),'q7 i i right q7'.split(),'q7 j j right q7'.split(),'q7 k k right q7'.split(),'q7 l l right q7'.split(),'q7 m m right q7'.split(),'q7 n n right q7'.split(),'q7 o o right q7'.split(),'q7 p p right q7'.split(),'q7 q q right q7'.split(),'q7 r r right q7'.split(),'q7 s s right q7'.split(),'q7 t t right q7'.split(),'q7 u u right q7'.split(),'q7 v v right q7'.split(),'q7 w w right q7'.split(),'q7 x x right q7'.split(),'q7 y y right q7'.split(),'q7 z z right q7'.split(), 'q7 , , right q7'.split(),'q7 * * right q7'.split(), 'q7 { { right q7'.split(), 'q7 } } right q7'.split(),'q7 B B right q8'.split(),'q7 1 1 right q7'.split(),'q7 2 2 right q7'.split(),'q7 3 3 right q7'.split(),'q7 4 4 right q7'.split(),'q7 5 5 right q7'.split(),'q7 6 6 right q7'.split(),'q7 7 7 right q7'.split(),'q7 8 8 right q7'.split(),'q7 9 9 right q7'.split(),'q7 0 0 right q7'.split(),
                    'q9 , , right q6'.split(), 'q9 } } right q9'.split(), 'q9 B B left q10'.split(),
                    'q10 a a left q10'.split(), 'q10 b b left q10'.split(), 'q10 c c left q10'.split(), 'q10 d d left q10'.split(), 'q10 e e left q10'.split(), 'q10 f f left q10'.split(),'q10 g g left q10'.split(),'q10 h h left q10'.split(),'q10 i i left q10'.split(),'q10 j j left q10'.split(),'q10 k k left q10'.split(),'q10 l l left q10'.split(),'q10 m m left q10'.split(),'q10 n n left q10'.split(),'q10 o o left q10'.split(),'q10 p p left q10'.split(),'q10 q q left q10'.split(),'q10 r r left q10'.split(),'q10 s s left q10'.split(),'q10 t t left q10'.split(),'q10 u u left q10'.split(),'q10 v v left q10'.split(),'q10 w w left q10'.split(),'q10 x x left q10'.split(),'q10 y y left q10'.split(),'q10 z z left q10'.split(), 'q10 } } left q10'.split(), 'q10 * * left q10'.split(), 'q10 , , left q10'.split(),'q10 { { left q10'.split(), 'q10 D D left q10'.split(), 'q10 E E left q10'.split(),'q10 0 0 left q10'.split(),'q10 1 1 left q10'.split(),'q10 2 2 left q10'.split(),'q10 3 3 left q10'.split(),'q10 4 4 left q10'.split(),'q10 5 5 left q10'.split(),'q10 6 6 left q10'.split(),'q10 7 7 left q10'.split(),'q10 8 8 left q10'.split(),'q10 9 9 left q10'.split(),
                    'q11 , , right q11'.split(), 'q11 * * right q11'.split(), 'q11 { { right q11'.split(), 'q11 } } right q11'.split(),'q11 D D right q12'.split(),'q11 E E right q12'.split(),'q11 a a right q2'.split(), 'q11 b b right q2'.split(), 'q11 c c right q2'.split(), 'q11 d d right q2'.split(), 'q11 e e right q2'.split(), 'q11 f f right q2'.split(), 'q11 g g right q2'.split(), 'q11 h h right q2'.split(), 'q11 i i right q2'.split(), 'q11 j j right q2'.split(), 'q11 k k right q2'.split(), 'q11 l l right q2'.split(), 'q11 m m right q2'.split(), 'q11 n n right q2'.split(), 'q11 o o right q2'.split(), 'q11 p p right q2'.split(), 'q11 q q right q2'.split(),'q11 r r right q2'.split(), 'q11 s s right q2'.split(),'q11 t t right q2'.split(), 'q11 u u right q2'.split(), 'q11 v v right q2'.split(), 'q11 w w right q2'.split(), 'q11 x x right q2'.split(), 'q11 y y right q2'.split(),'q11 z z right q2'.split(),'q11 1 1 right q2'.split(),'q11 2 2 right q2'.split(),'q11 3 3 right q2'.split(),'q11 4 4 right q2'.split(),'q11 5 5 right q2'.split(),'q11 6 6 right q2'.split(),'q11 7 7 right q2'.split(),'q11 8 8 right q2'.split(),'q11 9 9 right q2'.split(),'q11 0 0 right q2'.split(),   
                    'q12 { { right q12'.split(), 'q12 } } right q12'.split(), 'q12 * * right q12'.split(), 'q12 * * right q12'.split(), 'q12 a a right q12'.split(), 'q12 b b right q12'.split(), 'q12 c c right q12'.split(),'q12 d d right q12'.split(), 'q12 e e right q12'.split(), 'q12 f f right q12'.split(),'q12 g g  right q12'.split(),'q12 h h right q12'.split(),'q12 i i right q12'.split(),'q12 j j right q12'.split(),'q12 k k right q12'.split(),'q12 l l right q12'.split(),'q12 n n right q12'.split(),'q12 m m right q12'.split(),'q12 o o right q12'.split(),'q12 p p right q12'.split(),'q12 q q right q12'.split(),'q12 r r right q12'.split(),'q12 s s right q12'.split(),'q12 t t right q12'.split(),'q12 u u right q12'.split(),'q12 v v right q12'.split(),'q12 w w right q12'.split(),'q12 x x right q12'.split(),'q12 y y right q12'.split(),'q12 z z right q12'.split(), 'q12 B B right q13'.split(),'q12 , , right q12'.split(),'q12 1 1 right q12'.split(),'q12 2 2 right q12'.split(),'q12 3 3 right q12'.split(),'q12 4 4 right q12'.split(),'q12 5 5 right q12'.split(),'q12 6 6 right q12'.split(),'q12 7 7 right q12'.split(),'q12 8 8 right q12'.split(),'q12 9 9 right q12'.split(),'q12 0 0 right q12'.split(),
                    'q14 B B right q13'.split(),'q14 E E right q14'.split(),'q14 , , right q14'.split(),'q14 * * right q14'.split(),'q14 { { right q14'.split(),'q14 } } right q14'.split(),'q14 a a right q14'.split(), 'q14 b b right q14'.split(), 'q14 c c right q14'.split(),'q14 d d right q14'.split(),'q14 e e right q14'.split(),'q14 f f right q14'.split(),'q14 g g right q14'.split(),'q14 h h right q14'.split(),'q14 i i right q14'.split(),'q14 j j right q14'.split(),'q14 k k right q14'.split(),'q14 l l right q14'.split(),'q14 m m right q14'.split(),'q14 n n right q14'.split(),'q14 o o right q14'.split(),'q14 p p right q14'.split(),'q14 q q right q14'.split(),'q14 r r right q14'.split(),'q14 s s right q14'.split(), 'q14 t t right q14'.split(),'q14 u u right q14'.split(),'q14 v v right q14'.split(),'q14 w w right q14'.split(),'q14 x x right q14'.split(),'q14 y y right q14'.split(),'q14 z z right q14'.split(),'q14 1 1 right q14'.split(),'q14 2 2 right q14'.split(),'q14 3 3 right q14'.split(),'q14 4 4 right q14'.split(),'q14 5 5 right q14'.split(),'q14 6 6 right q14'.split(),'q14 7 7 right q14'.split(),'q14 8 8 right q14'.split(),'q14 9 9 right q14'.split(),'q14 0 0 right q14'.split(),
                    'q15 B B right q13'.split(),
                ], # reglas para las transiciones
                ))
        return validacion
               