class Pertenencia():
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
                if st == 'q5':
                    return 'El elemento no pertenece al conjunto'
                if st == 'q6':
                    return'El elemento pertenece al conjunto'

            if (st, tape[position]) not in rules:
                return'no validado '

            (v1,dr,s1) = rules[(st,tape[position])]
            if st == 'q3' and SV == v1:
                v1 = '*'
                s1 = 'q4'
                dr = 'right'
            if st == 'q4' and SV == v1:
                v1 = '*'
            





            tape[position] = v1

            
            if st == 'q0' and (v1 =='a' or v1 =='b' or v1 =='c' or v1 =='d' or v1 =='e' or v1 =='f' or v1 =='g' or v1 =='h' or v1 =='i' or v1 =='j' or v1 =='k' or v1 =='l' or v1 =='m' or v1 =='n' or v1 =='o' or v1 =='p' or v1 =='q' or v1 =='r'or v1 =='s' or v1 =='t'or v1 =='u' or v1 =='v'or v1 =='w' or v1 =='x'or v1 =='y' or v1 =='z' or v1 =='0'or v1 =='1' or v1 =='2' or v1 =='3' or v1 =='4' or v1 =='5' or  v1 =='6'or v1 =='7' or v1 =='8' or v1 =='9'):
                SV = v1
            if dr == 'left':
                if position > 0: position -= 1
                else: tape.insert(0, blank)
            if dr == 'right':
                position += 1
                if position >= len(tape): tape.append(blank)

            st = s1

    def reglas_pertenencia(self,conjunto):
        validacion = self.turing_M(
                state = 'q0', # Estado inicial
                blank = 'B', # El simbolo que representa blanco
                tape = list(conjunto), # cinta
                final = 'q5',# Estado final
                final2 = 'q6',
                rules = map(tuple,
                [
                    'q0 { {} right q1'.split(), 'q0 a a right q1'.split(), 'q0 b b right q1'.split(), 'q0 c c right q1'.split(),'q0 d d right q1'.split(),'q0 e e right q1'.split(),'q0 f f right q1'.split(),'q0 g g right q1'.split(),'q0 h h right q1'.split(),'q0 i i right q1'.split(),'q0 j j right q1'.split(),'q0 k k right q1'.split(),'q0 l l right q1'.split(),'q0 m m right q1'.split(),'q0 n n right q1'.split(),'q0 o o right q1'.split(),'q0 p p right q1'.split(),'q0 q q right q1'.split(),'q0 r r right q1'.split(),'q0 s s right q1'.split(),'q0 t t right q1'.split(),'q0 u u right q1'.split(),'q0 v v right q1'.split(),'q0 w w right q1'.split(),'q0 x x right q1'.split(),'q0 y y right q1'.split(),'q0 z z right q1'.split(),'q0 0 0 right q1'.split(),'q0 1 1 right q1'.split(),'q0 2 2 right q1'.split(),'q0 3 3 right q1'.split(),'q0 4 4 right q1'.split(),'q0 5 5 right q1'.split(),'q0 6 6 right q1'.split(),'q0 7 7 right q1'.split(),'q0 8 8 right q1'.split(),'q0 9 9 right q1'.split(), 
                    'q1 E E right q2'.split(),'q1 } } right q6'.split(),
                    'q2 { { right q3'.split(),
                    'q3 } } right q5'.split(),'q3 , , right q3'.split(),'q3 a a right q3'.split(), 'q3 b b right q3'.split(), 'q3 c c right q3'.split(),'q3 d d right q3'.split(),'q3 e e right q3'.split(),'q3 f f right q3'.split(),'q3 g g right q3'.split(),'q3 h h right q3'.split(),'q3 i i right q3'.split(),'q3 j j right q3'.split(),'q3 k k right q3'.split(),'q3 l l right q3'.split(),'q3 m m right q3'.split(),'q3 n n right q3'.split(),'q3 o o right q3'.split(),'q3 p p right q3'.split(),'q3 q q right q3'.split(),'q3 r r right q3'.split(),'q3 s s right q3'.split(),'q3 t t right q3'.split(),'q3 u u right q3'.split(),'q3 v v right q3'.split(),'q3 w w right q3'.split(),'q3 x x right q3'.split(),'q3 y y right q3'.split(),'q3 z z right q3'.split(),'q3 0 0 right q3'.split(),'q3 1 1 right q3'.split(),'q3 2 2 right q3'.split(),'q3 3 3 right q3'.split(),'q3 4 4 right q3'.split(),'q3 5 5 right q3'.split(),'q3 6 6 right q3'.split(),'q3 7 7 right q3'.split(),'q3 8 8 right q3'.split(),'q3 9 9 right q3'.split(), 
                    'q4 } } right q6'.split(),'q4 , , right q4'.split(),'q4 a a right q4'.split(), 'q4 b b right q4'.split(), 'q4 c c right q4'.split(),'q4 d d right q4'.split(),'q4 e e right q4'.split(),'q4 f f right q4'.split(),'q4 g g right q4'.split(),'q4 h h right q4'.split(),'q4 i i right q4'.split(),'q4 j j right q4'.split(),'q4 k k right q4'.split(),'q4 l l right q4'.split(),'q4 m m right q4'.split(),'q4 n n right q4'.split(),'q4 o o right q4'.split(),'q4 p p right q4'.split(),'q4 q q right q4'.split(),'q4 r r right q4'.split(),'q4 s s right q4'.split(),'q4 t t right q4'.split(),'q4 u u right q4'.split(),'q4 v v right q4'.split(),'q4 w w right q4'.split(),'q4 x x right q4'.split(),'q4 y y right q4'.split(),'q4 z z right q4'.split(),'q4 0 0 right q4'.split(),'q4 1 1 right q4'.split(),'q4 2 2 right q4'.split(),'q4 3 3 right q4'.split(),'q4 4 4 right q4'.split(),'q4 5 5 right q4'.split(),'q4 6 6 right q4'.split(),'q4 7 7 right q4'.split(),'q4 8 8 right q4'.split(),'q4 9 9 right q4'.split(), 
                ], # reglas para las transiciones
                ))
        return validacion