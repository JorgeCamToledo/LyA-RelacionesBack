class Subconjunto():
    def turing_M(self,
            state = None, # Los estados de la MT
            blank = None, # El simbolo que representa blanco
            rules = [], # reglas para las transiciones
            tape = [], # cinta
            final = None,# Estado final
            final2 = None,
            final3 = None,
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

            if st == final or st == final2 or st == final3:
                if st == 'q12':
                    return 'A es subconjunto de B'
                if st == 'q6':
                    return 'A no es subconjunto de B'
                if st == 'q13':
                    return 'A es subconjunto de B'

                
            if (st, tape[position]) not in rules:
                return 'no validado'
                

            (v1,dr,s1) = rules[(st,tape[position])]
            if st == 'q3' and SV == v1:
                v1 = '*'
            if st == 'q4' and SV == v1:
                v1 = '*'

            if st == 'q5' and SV== v1:
                v1 = '*'
                s1 = 'q7'

            if st == 'q7' and SV== v1:
                v1 = '*'
                s1 = 'q7'

            if st == 'q8' and SV == v1:
                v1 = '*'
                s1 = 'q9'
                dr = 'right'



            tape[position] = v1

            
            if st == 'q1' and (v1 =='a' or v1 =='b' or v1 =='c' or v1 =='d' or v1 =='e' or v1 =='f' or v1 =='g' or v1 =='h' or v1 =='i' or v1 =='j' or v1 =='k' or v1 =='l' or v1 =='m' or v1 =='n' or v1 =='o' or v1 =='p' or v1 =='q' or v1 =='r'or v1 =='s' or v1 =='t'or v1 =='u' or v1 =='v'or v1 =='w' or v1 =='x'or v1 =='y' or v1 =='z' or v1 =='0'or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or  v1 =='6'or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1
            if st == 'q9' and (v1 =='a' or v1 =='b' or v1 =='c' or v1 =='d' or v1 =='e' or v1 =='f' or v1 =='g' or v1 =='h' or v1 =='i' or v1 =='j' or v1 =='k' or v1 =='l' or v1 =='m' or v1 =='n' or v1 =='o' or v1 =='p' or v1 =='q' or v1 =='r'or v1 =='s' or v1 =='t'or v1 =='u' or v1 =='v'or v1 =='w' or v1 =='x'or v1 =='y' or v1 =='z' or v1 =='0'or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or  v1 =='6'or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1
            if dr == 'left':
                if position > 0: position -= 1
                else: tape.insert(0, blank)
            if dr == 'right':
                position += 1
                if position >= len(tape): tape.append(blank)

            st = s1

    def reglas_subconjunto(self,conjunto):
        validacion = self.turing_M(
                state = 'q0', # Estado inicial
                blank = 'B', # El simbolo que representa blanco
                tape = list(conjunto), # cinta
                final = 'q6',# Estado final
                final2 = 'q12',
                final3 = 'q13',
                rules = map(tuple,
                [
                    'q0 { {  right q1'.split(),
                    'q1 a a right q2'.split(), 'q1 b b right q2'.split(), 'q1 c c right q2'.split(),'q1 d d right q2'.split(),'q1 e e right q2'.split(),'q1 f f right q2'.split(),'q1 g g right q2'.split(),'q1 h h right q2'.split(),'q1 i i right q2'.split(),'q1 j j right q2'.split(),'q1 k k right q2'.split(),'q1 l l right q2'.split(),'q1 m m right q2'.split(),'q1 n n right q2'.split(),'q1 o o right q2'.split(),'q1 p p right q2'.split(),'q1 q q right q2'.split(),'q1 r r right q2'.split(),'q1 s s right q2'.split(),'q1 t t right q2'.split(),'q1 u u right q2'.split(),'q1 v v right q2'.split(),'q1 w w right q2'.split(),'q1 x x right q2'.split(),'q1 y y right q2'.split(),'q1 z z right q2'.split(),'q1 0 0 right q2'.split(),'q1 1 1 right q2'.split(),'q1 2 2 right q2'.split(),'q1 3 3 right q2'.split(),'q1 4 4 right q2'.split(),'q1 5 5 right q2'.split(),'q1 6 6 right q2'.split(),'q1 7 7 right q2'.split(),'q1 8 8 right q2'.split(),'q1 9 9 right q2'.split(), 'q1 } } right q10'.split(),
                    'q2 , , right q3'.split(), 'q2 } } right q3'.split(),
                    'q3 a a right q3'.split(), 'q3 b b right q3'.split(), 'q3 c c right q3'.split(), 'q3 , , right q3'.split(), 'q3 * * right q3'.split(), 'q3 } } right q3'.split(),'q3 E E right q4'.split(), 'q3 d d right q3'.split(), 'q3 e e right q3'.split(),'q3 f f right q3'.split(), 'q3 B B right q13'.split(),'q3 g g right q3'.split(),'q3 h h right q3'.split(),'q3 i i right q3'.split(),'q3 j j right q3'.split(),'q3 k k right q3'.split(),'q3 l l right q3'.split(),'q3 m m right q3'.split(),'q3 n n right q3'.split(),'q3 o o right q3'.split(),'q3 p p right q3'.split(),'q3 q q right q3'.split(),'q3 r r right q3'.split(),'q3 s s right q3'.split(),'q3 t t right q3'.split(),'q3 u u right q3'.split(),'q3 v v right q3'.split(),'q3 w w right q3'.split(),'q3 x x right q3'.split(),'q3 y y right q3'.split(),'q3 z z right q3'.split(),'q3 0 0 right q3'.split(),'q3 1 1 right q3'.split(),'q3 2 2 right q3'.split(),'q3 3 3 right q3'.split(),'q3 4 4 right q3'.split(),'q3 5 5 right q3'.split(),'q3 6 6 right q3'.split(),'q3 7 7 right q3'.split(),'q3 8 8 right q3'.split(),'q3 9 9 right q3'.split(),
                    'q4 { { right q5'.split(),
                    'q5 a a right q5'.split(), 'q5 b b right q5'.split(), 'q5 c c right q5'.split(), 'q5 , , right q5'.split(),'q5 } } right q6'.split(), 'q5 * * right q5'.split(),'q5 d d right q5'.split(), 'q5 e e right q5'.split(), 'q5 f f right q5'.split(),'q5 g g right q5'.split(),'q5 h h right q5'.split(),'q5 i i right q5'.split(),'q5 j j right q5'.split(),'q5 k k right q5'.split(),'q5 l l right q5'.split(),'q5 m m right q5'.split(),'q5 n n right q5'.split(),'q5 o o right q5'.split(),'q5 p p right q5'.split(),'q5 q q right q5'.split(),'q5 r r right q5'.split(),'q5 s s right q5'.split(),'q5 t t right q5'.split(),'q5 u u right q5'.split(),'q5 v v right q5'.split(),'q5 w w right q5'.split(),'q5 x x right q5'.split(),'q5 y y right q5'.split(),'q5 z z right q5'.split(),'q5 0 0 right q5'.split(),'q5 1 1 right q5'.split(),'q5 2 2 right q5'.split(),'q5 3 3 right q5'.split(),'q5 4 4 right q5'.split(),'q5 5 5 right q5'.split(),'q5 6 6 right q5'.split(),'q5 7 7 right q5'.split(),'q5 8 8 right q5'.split(),'q5 9 9 right q5'.split(),
                    'q6 B B right q6'.split(),
                    'q7 a a right q7'.split(), 'q7 b b right q7'.split(), 'q7 c c right q7'.split(), 'q7 , , right q7'.split(),'q7 } } right q8'.split(), 'q7 * * right q7'.split(),'q7 d d right q7'.split(), 'q7 e e right q7'.split(), 'q7 f f right q7'.split(), 'q7 g g right q7'.split(),'q7 h h right q7'.split(),'q7 i i right q7'.split(),'q7 j j right q7'.split(),'q7 k k right q7'.split(),'q7 l l right q7'.split(),'q7 m m right q7'.split(),'q7 n n right q7'.split(),'q7 o o right q7'.split(),'q7 p p right q7'.split(),'q7 q q right q7'.split(),'q7 r r right q7'.split(),'q7 s s right q7'.split(),'q7 t t right q7'.split(),'q7 u u right q7'.split(),'q7 v v right q7'.split(),'q7 w w right q7'.split(),'q7 x x right q7'.split(),'q7 y y right q7'.split(),'q7 z z right q7'.split(),'q7 0 0 right q7'.split(),'q7 1 1 right q7'.split(),'q7 2 2 right q7'.split(),'q7 3 3 right q7'.split(),'q7 4 4 right q7'.split(),'q7 5 5 right q7'.split(),'q7 6 6 right q7'.split(),'q7 7 7 right q7'.split(),'q7 8 8 right q7'.split(),'q7 9 9 right q7'.split(),
                    'q8 B B left q8'.split(),'q8 a a left q8'.split(), 'q8 b b left q8'.split(), 'q8 c c left q8'.split(), 'q8 * * left q8'.split(),'q8 , , left q8'.split(), 'q8 { { left q8'.split(),'q8 E E left q8'.split(),'q8 } } left q8'.split(), 'q8 d d left q8'.split(), 'q8 e e left q8'.split(), 'q8 f f left q8'.split(), 'q8 g g left q8'.split(),'q8 h h left q8'.split(),'q8 i i left q8'.split(),'q8 j j left q8'.split(),'q8 k k left q8'.split(),'q8 l l left q8'.split(),'q8 m m left q8'.split(),'q8 n n left q8'.split(),'q8 o o left q8'.split(),'q8 p p left q8'.split(),'q8 q q left q8'.split(),'q8 r r left q8'.split(),'q8 s s left q8'.split(),'q8 t t left q8'.split(),'q8 u u left q8'.split(),'q8 v v left q8'.split(),'q8 w w left q8'.split(),'q8 x x left q8'.split(),'q8 y y left q8'.split(),'q8 z z left q8'.split(),'q8 0 0 left q8'.split(),'q8 1 1 left q8'.split(),'q8 2 2 left q8'.split(),'q8 3 3 left q8'.split(),'q8 4 4 left q8'.split(),'q8 5 5 left q8'.split(),'q8 6 6 left q8'.split(),'q8 7 7 left q8'.split(),'q8 8 8 left q8'.split(),'q8 9 9 left q8'.split(),
                    'q9 , , right q9'.split(), 'q9 * * right q9'.split(),'q9 a a right q3'.split(), 'q9 b b right q3'.split(), 'q9 c c right q3'.split(), 'q9 } } right q10'.split(),'q9 d d right q3'.split(), 'q9 e e right q3'.split(), 'q9 f f right q3'.split(), 'q9 g g right q3'.split(),'q9 h h right q3'.split(),'q9 i i right q3'.split(),'q9 j j right q3'.split(),'q9 k k right q3'.split(),'q9 l l right q3'.split(),'q9 m m right q3'.split(),'q9 n n right q3'.split(),'q9 o o right q3'.split(),'q9 p p right q3'.split(),'q9 q q right q3'.split(),'q9 r r right q3'.split(),'q9 s s right q3'.split(),'q9 t t right q3'.split(),'q9 u u right q3'.split(),'q9 v v right q3'.split(),'q9 w w right q3'.split(),'q9 x x right q3'.split(),'q9 y  y right q3'.split(),'q9 z z right q3'.split(),'q9 0 0 right q3'.split(),'q9 1 1 right q3'.split(),'q9 2 2 right q3'.split(),'q9 3 3 right q3'.split(),'q9 4 4 right q3'.split(),'q9 5 5 right q3'.split(),'q9 6 6 right q3'.split(),'q9 7 7 right q3'.split(),'q9 8 8 right q3'.split(),'q9 9 9 right q3'.split(),
                    'q10 E E right q11'.split(),
                    'q11 { { right q11'.split(),'q11 , , right q11'.split(),'q11 * * right q11'.split(), 'q11 } } right q12'.split(), 'q11 a a right q3'.split(), 'q11 b b right q3'.split(), 'q11 c c right q3'.split(), 'q11 d d right q3'.split(), 'q11 e e right q3'.split(), 'q11 f f right q3'.split(),'q11 g g right q3'.split(), 'q11 h h right q3'.split(), 'q11 i i right q3'.split(), 'q11 j j right q3'.split(), 'q11 k k right q3'.split(), 'q11 l l right q3'.split(),'q11 m m right q3'.split(),'q11 n n right q3'.split(),'q11 o o right q3'.split(),'q11 p p right q3'.split(),'q11 q q right q3'.split(),'q11 r r right q3'.split(),'q11 s s right q3'.split(),'q11 t t right q3'.split(),'q11 u u right q3'.split(),'q11 v v right q3'.split(),'q11 w w right q3'.split(),'q11 x x right q3'.split(),'q11 y y right q3'.split(),'q11 z z right q3'.split(),'q11 0 0 right q3'.split(),'q11 1 1 right q3'.split(),'q11 2 2 right q3'.split(),'q11 3 3 right q3'.split(),'q11 4 4 right q3'.split(),'q11 5 5 right q3'.split(),'q11 6 6 right q3'.split(),'q11 7 7 right q3'.split(),'q11 8 8 right q3'.split(),'q11 9 9 right q3'.split(),
                    'q12 B B right q12'.split(),
                    'q13 B B right q13'.split(),
                    

                    
                ], # reglas para las transiciones
                ))
        return validacion