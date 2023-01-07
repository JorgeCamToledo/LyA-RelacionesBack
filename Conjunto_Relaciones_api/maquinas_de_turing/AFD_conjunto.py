class AFD_Conjunto():
    def AFD(self,
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
        rules = dict(((s0,v0),(s1)) for (s0,v0,s1) in rules)
        """
        Estado         Simbolo a leer       Sig. EStado
        q0(s0)            {(v0)              q1(s1)
        """
        while True:
            print(st,'\t', end = '  ')
            for i, v in enumerate(tape):
                if i == position:
                    print("[%s]"%(v,),end=" ")
                else: print (v, end=" ")
            print()

            if st == final or st == final2:
                if st == 'q1':
                    return 'Valor'
                if st == 'q5':
                    return'Conjunto'

            if (st, tape[position]) not in rules:
                return'no validado'
            
            

            (s1) = rules[(st,tape[position])]

            position += 1
            if position >= len(tape): tape.append(blank)
            st = s1
            

    def reglas_AFD_conjunto(self,conjunto):
        validacion = self.AFD(
                state = 'q0', # Estado inicial
                blank = 'B', # El simbolo que representa blanco
                tape = list(conjunto), # cinta
                final = 'q1',# Estado final
                final2 = 'q5',
                rules = map(tuple,
                [
                    'q0 { q2'.split(), 'q0 a q1'.split(), 'q0 b q1'.split(), 'q0 c q1'.split(), 'q0 d q1'.split(), 'q0 e q1'.split(), 'q0 f q1'.split(), 'q0 g q1'.split(), 'q0 h q1'.split(), 'q0 i q1'.split(), 'q0 j q1'.split(), 'q0 k q1'.split(), 'q0 l q1'.split(), 'q0 n q1'.split(), 'q0 m q1'.split(), 'q0 o q1'.split(), 'q0 p q1'.split(), 'q0 q q1'.split(), 'q0 r q1'.split(), 'q0 s q1'.split(), 'q0 t q1'.split(), 'q0 u q1'.split(), 'q0 v q1'.split(), 'q0 w q1'.split(), 'q0 x q1'.split(), 'q0 y q1'.split(), 'q0 z q1'.split(), 'q0 0 q1'.split(), 'q0 1 q1'.split(), 'q0 2 q1'.split(), 'q0 3 q1'.split(), 'q0 4 q1'.split(), 'q0 5 q1'.split(), 'q0 6 q1'.split(), 'q0 7 q1'.split(), 'q0 8 q1'.split(), 'q0 9 q1'.split(), 
                    'q2 } q5'.split(), 'q2 a q3'.split(), 'q2 b q3'.split(), 'q2 c q3'.split(), 'q2 d q3'.split(), 'q2 e q3'.split(), 'q2 f q3'.split(), 'q2 g q3'.split(), 'q2 h q3'.split(), 'q2 i q3'.split(), 'q2 j q3'.split(), 'q2 k q3'.split(), 'q2 l q3'.split(), 'q2 n q3'.split(), 'q2 m q3'.split(), 'q2 o q3'.split(), 'q2 p q3'.split(), 'q2 q q3'.split(), 'q2 r q3'.split(), 'q2 s q3'.split(), 'q2 t q3'.split(), 'q2 u q3'.split(), 'q2 v q3'.split(), 'q2 w q3'.split(), 'q2 x q3'.split(), 'q2 y q3'.split(), 'q2 z q3'.split(), 'q2 0 q3'.split(),'q2 1 q3'.split(),'q2 2 q3'.split(), 'q2 3 q3'.split(), 'q2 4 q3'.split(), 'q2 5 q3'.split(), 'q2 6 q3'.split(), 'q2 7 q3'.split(), 'q2 8 q3'.split(), 'q2 9 q3'.split(),
                    'q3 , q4'.split(), 'q3 } q5'.split(),
                    'q4 a q3'.split(), 'q4 b q3'.split(), 'q4 c q3'.split(),'q4 d q3'.split(), 'q4 e q3'.split(), 'q4 f q3'.split(), 'q4 g q3'.split(), 'q4 h q3'.split(), 'q4 i q3'.split(), 'q4 j q3'.split(), 'q4 k q3'.split(), 'q4 l q3'.split(), 'q4 n q3'.split(), 'q4 m q3'.split(), 'q4 o q3'.split(), 'q4 p q3'.split(), 'q4 q q3'.split(), 'q4 r q3'.split(), 'q4 s q3'.split(), 'q4 t q3'.split(), 'q4 u q3'.split(), 'q4 v q3'.split(), 'q4 w q3'.split(), 'q4 x q3'.split(), 'q4 y q3'.split(), 'q4 z q3'.split(), 'q4 0 q3'.split(), 'q4 1 q3'.split(),'q4 2 q3'.split(),'q4 3 q3'.split(),'q4 4 q3'.split(),'q4 5 q3'.split(),'q4 6 q3'.split(),'q4 7 q3'.split(),'q4 8 q3'.split(),'q4 9 q3'.split(),
                    ], # reglas para las transiciones
                ))
        return validacion
