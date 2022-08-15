from tkinter.font import BOLD
from pyknow import *
from tkinter import *
from tkinter import ttk
Escala=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
EscalasProb=[]
#aux=[False,False,False]
tabla_escalas = {
    '0': 'C', '1': 'C#/Db','2': 'D', '3': 'D#/Eb','4': 'E', '5': 'F','6': 'F#/Gb', '7': 'G','8': 'G#/Ab', '9': 'A','10': 'A#/Bb', '11': 'B',
    '12': 'Cm', '13': 'C#m/Dbm','14': 'Dm', '15': 'D#m/Ebm','16': 'Em', '17': 'Fm','18': 'F#m/Gbm', '19': 'Gm','20': 'G#m/Abm', '21': 'Am','22': 'A#m/Bbm', '23': 'Bm',
}
def N_Escala(n):
    return tabla_escalas.get(n,"NA")
def PartirEscala0(Scale):
    if Scale.find('/')==-1:
        return Scale
    else:
        pos=Scale.find('/')
        N_Escala=Scale[0:pos]
        return N_Escala
def PartirEscala1(Scale):
    if Scale.find('/')==-1:
        return Scale
    else:
        pos=Scale.find('/')
        N_Escala=Scale[pos+1:len(Scale)]
        return N_Escala
def CalEscala():
    Escala=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    EscalasProb.clear()
    # C:0 C#/Db:1 D:2 D#/Eb:3 E:4 F:5 F#/Gb:6 G:7 G#/Ab:8 A:9 A#/Bb:10 B:11 Cm:12 C#m/Dbm:13 Dm:14 D#m/Ebm:15 Em:16 Fm:17 F#m/Gbm:18 Gm:19 
    # G#m/Abm:20 Am:21 A#m/Bbm:22 Bm:23 
    Acorde1=combo1.get() 
    Acorde2=combo2.get() 
    Acorde3=combo3.get() 
    Acorde4=combo4.get() 
    Acorde5=combo5.get() 
    Acorde6=combo6.get() 
    Acorde7=combo7.get() 
    class Chord1(Fact):
        pass
    class Chord2(Fact):
        pass
    class Chord3(Fact):
        pass
    class Chord4(Fact):
        pass
    class Chord5(Fact):
        pass
    class Chord6(Fact):
        pass
    class Chord7(Fact):
        pass

    class Num_EscalasProbables(Fact):
        pass
    class EscalaMayorBool(Fact):
        pass
    class EscalaMenorBool(Fact):
        pass

    class DetectarEscala(KnowledgeEngine):
        @Rule(OR(Chord1(chord='C'),Chord2(chord='C'),Chord3(chord='C'),Chord4(chord='C'),Chord5(chord='C'),Chord6(chord='C'),Chord7(chord='C'),Chord1(chord='B#'),Chord2(chord='B#'),Chord3(chord='B#'),Chord4(chord='B#'),Chord5(chord='B#'),Chord6(chord='B#'),Chord7(chord='B#')))
        def chordC(self):
            Escala[0]=Escala[0]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1
            
            Escala[21]=Escala[21]+1
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='C#'),Chord2(chord='C#'),Chord3(chord='C#'),Chord4(chord='C#'),Chord5(chord='C#'),Chord6(chord='C#'),Chord7(chord='C#'),Chord1(chord='Db'),Chord2(chord='Db'),Chord3(chord='Db'),Chord4(chord='Db'),Chord5(chord='Db'),Chord6(chord='Db'),Chord7(chord='Db')))
        def chordDb(self):
            Escala[1]=Escala[1]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1
            
            Escala[22]=Escala[22]+1
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
                
        @Rule(OR(Chord1(chord='D'),Chord2(chord='D'),Chord3(chord='D'),Chord4(chord='D'),Chord5(chord='D'),Chord6(chord='D'),Chord7(chord='D')))
        def chordD(self):
            Escala[2]=Escala[2]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1
            
            Escala[23]=Escala[23]+1
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
            
        @Rule(OR(Chord1(chord='D#'),Chord2(chord='D#'),Chord3(chord='D#'),Chord4(chord='D#'),Chord5(chord='D#'),Chord6(chord='D#'),Chord7(chord='D#'),Chord1(chord='Eb'),Chord2(chord='Eb'),Chord3(chord='Eb'),Chord4(chord='Eb'),Chord5(chord='Eb'),Chord6(chord='Eb'),Chord7(chord='Eb')))
        def chordEb(self):
            Escala[3]=Escala[3]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            
            Escala[12]=Escala[12]+1
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
            
        @Rule(OR(Chord1(chord='E'),Chord2(chord='E'),Chord3(chord='E'),Chord4(chord='E'),Chord5(chord='E'),Chord6(chord='E'),Chord7(chord='E'),Chord1(chord='Fb'),Chord2(chord='Fb'),Chord3(chord='Fb'),Chord4(chord='Fb'),Chord5(chord='Fb'),Chord6(chord='Fb'),Chord7(chord='Fb')))
        def chordE(self):
            Escala[4]=Escala[4]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            
            Escala[13]=Escala[13]+1
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
            
        @Rule(OR(Chord1(chord='F'),Chord2(chord='F'),Chord3(chord='F'),Chord4(chord='F'),Chord5(chord='F'),Chord6(chord='F'),Chord7(chord='F'),Chord1(chord='E#'),Chord2(chord='E#'),Chord3(chord='E#'),Chord4(chord='E#'),Chord5(chord='E#'),Chord6(chord='E#'),Chord7(chord='E#')))
        def chordF(self):
            Escala[5]=Escala[5]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            
            Escala[14]=Escala[14]+1
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            
        @Rule(OR(Chord1(chord='F#'),Chord2(chord='F#'),Chord3(chord='F#'),Chord4(chord='F#'),Chord5(chord='F#'),Chord6(chord='F#'),Chord7(chord='F#'),Chord1(chord='Gb'),Chord2(chord='Gb'),Chord3(chord='Gb'),Chord4(chord='Gb'),Chord5(chord='Gb'),Chord6(chord='Gb'),Chord7(chord='Gb')))
        def chordGb(self):
            Escala[6]=Escala[6]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1 
            
            Escala[15]=Escala[15]+1
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
            
        @Rule(OR(Chord1(chord='G'),Chord2(chord='G'),Chord3(chord='G'),Chord4(chord='G'),Chord5(chord='G'),Chord6(chord='G'),Chord7(chord='G')))
        def chordG(self):
            Escala[7]=Escala[7]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            
            Escala[16]=Escala[16]+1
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            
        @Rule(OR(Chord1(chord='G#'),Chord2(chord='G#'),Chord3(chord='G#'),Chord4(chord='G#'),Chord5(chord='G#'),Chord6(chord='G#'),Chord7(chord='G#'),Chord1(chord='Ab'),Chord2(chord='Ab'),Chord3(chord='Ab'),Chord4(chord='Ab'),Chord5(chord='Ab'),Chord6(chord='Ab'),Chord7(chord='Ab')))
        def chordAb(self):
            Escala[8]=Escala[8]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1 
            
            Escala[17]=Escala[17]+1
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            
        @Rule(OR(Chord1(chord='A'),Chord2(chord='A'),Chord3(chord='A'),Chord4(chord='A'),Chord5(chord='A'),Chord6(chord='A'),Chord7(chord='A')))
        def chordA(self):
            Escala[9]=Escala[9]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1 
            
            Escala[18]=Escala[18]+1
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
        
        @Rule(OR(Chord1(chord='A#'),Chord2(chord='A#'),Chord3(chord='A#'),Chord4(chord='A#'),Chord5(chord='A#'),Chord6(chord='A#'),Chord7(chord='A#'),Chord1(chord='Bb'),Chord2(chord='Bb'),Chord3(chord='Bb'),Chord4(chord='Bb'),Chord5(chord='Bb'),Chord6(chord='Bb'),Chord7(chord='Bb')))
        def chordBb(self):
            Escala[10]=Escala[10]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1   
            
            Escala[19]=Escala[19]+1
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
        
        @Rule(OR(Chord1(chord='B'),Chord2(chord='B'),Chord3(chord='B'),Chord4(chord='B'),Chord5(chord='B'),Chord6(chord='B'),Chord7(chord='B'),Chord1(chord='Cb'),Chord2(chord='Cb'),Chord3(chord='Cb'),Chord4(chord='Cb'),Chord5(chord='Cb'),Chord6(chord='Cb'),Chord7(chord='Cb')))
        def chordB(self):
            Escala[11]=Escala[11]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1   
            
            Escala[20]=Escala[20]+1
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1 
        
        @Rule(OR(Chord1(chord='Cm'),Chord2(chord='Cm'),Chord3(chord='Cm'),Chord4(chord='Cm'),Chord5(chord='Cm'),Chord6(chord='Cm'),Chord7(chord='Cm'),Chord1(chord='B#m'),Chord2(chord='B#m'),Chord3(chord='B#m'),Chord4(chord='B#m'),Chord5(chord='B#m'),Chord6(chord='B#m'),Chord7(chord='B#m')))
        def chordCm(self):
            Escala[3]=Escala[3]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            
            Escala[12]=Escala[12]+1
            Escala[19]=Escala[19]+1
            Escala[17]=Escala[17]+1
            
        @Rule(OR(Chord1(chord='C#m'),Chord2(chord='C#m'),Chord3(chord='C#m'),Chord4(chord='C#m'),Chord5(chord='C#m'),Chord6(chord='C#m'),Chord7(chord='C#m'),Chord1(chord='Dbm'),Chord2(chord='Dbm'),Chord3(chord='Dbm'),Chord4(chord='Dbm'),Chord5(chord='Dbm'),Chord6(chord='Dbm'),Chord7(chord='Dbm')))
        def chordDbm(self):
            Escala[4]=Escala[4]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            
            Escala[13]=Escala[13]+1
            Escala[20]=Escala[20]+1
            Escala[18]=Escala[18]+1
                
        @Rule(OR(Chord1(chord='Dm'),Chord2(chord='Dm'),Chord3(chord='Dm'),Chord4(chord='Dm'),Chord5(chord='Dm'),Chord6(chord='Dm'),Chord7(chord='Dm')))
        def chordDm(self):
            Escala[5]=Escala[5]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            
            Escala[14]=Escala[14]+1
            Escala[21]=Escala[21]+1
            Escala[19]=Escala[19]+1
            
        @Rule(OR(Chord1(chord='D#m'),Chord2(chord='D#m'),Chord3(chord='D#m'),Chord4(chord='D#m'),Chord5(chord='D#m'),Chord6(chord='D#m'),Chord7(chord='D#m'),Chord1(chord='Ebm'),Chord2(chord='Ebm'),Chord3(chord='Ebm'),Chord4(chord='Ebm'),Chord5(chord='Ebm'),Chord6(chord='Ebm'),Chord7(chord='Ebm')))
        def chordEbm(self):
            Escala[6]=Escala[6]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1 
            
            Escala[15]=Escala[15]+1
            Escala[22]=Escala[22]+1
            Escala[20]=Escala[20]+1 
            
        @Rule(OR(Chord1(chord='Em'),Chord2(chord='Em'),Chord3(chord='Em'),Chord4(chord='Em'),Chord5(chord='Em'),Chord6(chord='Em'),Chord7(chord='Em'),Chord1(chord='Fbm'),Chord2(chord='Fbm'),Chord3(chord='Fbm'),Chord4(chord='Fbm'),Chord5(chord='Fbm'),Chord6(chord='Fbm'),Chord7(chord='Fbm')))
        def chordEm(self):
            Escala[7]=Escala[7]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            
            Escala[16]=Escala[16]+1
            Escala[23]=Escala[23]+1
            Escala[21]=Escala[21]+1 
            
        @Rule(OR(Chord1(chord='Fm'),Chord2(chord='Fm'),Chord3(chord='Fm'),Chord4(chord='Fm'),Chord5(chord='Fm'),Chord6(chord='Fm'),Chord7(chord='Fm'),Chord1(chord='E#m'),Chord2(chord='E#m'),Chord3(chord='E#m'),Chord4(chord='E#m'),Chord5(chord='E#m'),Chord6(chord='E#m'),Chord7(chord='E#m')))
        def chordFm(self):
            Escala[8]=Escala[8]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1
            
            Escala[17]=Escala[17]+1
            Escala[12]=Escala[12]+1
            Escala[22]=Escala[22]+1 
            
        @Rule(OR(Chord1(chord='F#m'),Chord2(chord='F#m'),Chord3(chord='F#m'),Chord4(chord='F#m'),Chord5(chord='F#m'),Chord6(chord='F#m'),Chord7(chord='F#m'),Chord1(chord='Gbm'),Chord2(chord='Gbm'),Chord3(chord='Gbm'),Chord4(chord='Gbm'),Chord5(chord='Gbm'),Chord6(chord='Gbm'),Chord7(chord='Gbm')))
        def chordGbm(self):
            Escala[9]=Escala[9]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1 
            
            Escala[18]=Escala[18]+1
            Escala[13]=Escala[13]+1
            Escala[23]=Escala[23]+1 
            
        @Rule(OR(Chord1(chord='Gm'),Chord2(chord='Gm'),Chord3(chord='Gm'),Chord4(chord='Gm'),Chord5(chord='Gm'),Chord6(chord='Gm'),Chord7(chord='Gm')))
        def chordGm(self):
            Escala[10]=Escala[10]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1
            
            Escala[19]=Escala[19]+1
            Escala[14]=Escala[14]+1
            Escala[12]=Escala[12]+1 
        @Rule(OR(Chord1(chord='G#m'),Chord2(chord='G#m'),Chord3(chord='G#m'),Chord4(chord='G#m'),Chord5(chord='G#m'),Chord6(chord='G#m'),Chord7(chord='G#m'),Chord1(chord='Abm'),Chord2(chord='Abm'),Chord3(chord='Abm'),Chord4(chord='Abm'),Chord5(chord='Abm'),Chord6(chord='Abm'),Chord7(chord='Abm')))
        def chordAbm(self):
            Escala[11]=Escala[11]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1 
            
            Escala[20]=Escala[20]+1
            Escala[15]=Escala[15]+1
            Escala[13]=Escala[13]+1
            
        @Rule(OR(Chord1(chord='Am'),Chord2(chord='Am'),Chord3(chord='Am'),Chord4(chord='Am'),Chord5(chord='Am'),Chord6(chord='Am'),Chord7(chord='Am')))
        def chordAm(self):
            Escala[0]=Escala[0]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1 
            
            Escala[21]=Escala[21]+1
            Escala[16]=Escala[16]+1
            Escala[14]=Escala[14]+1 
        
        @Rule(OR(Chord1(chord='A#m'),Chord2(chord='A#m'),Chord3(chord='A#m'),Chord4(chord='A#m'),Chord5(chord='A#m'),Chord6(chord='A#m'),Chord7(chord='A#m'),Chord1(chord='Bbm'),Chord2(chord='Bbm'),Chord3(chord='Bbm'),Chord4(chord='Bbm'),Chord5(chord='Bbm'),Chord6(chord='Bbm'),Chord7(chord='Bbm')))
        def chordBbm(self):
            Escala[1]=Escala[1]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1   
            
            Escala[22]=Escala[22]+1
            Escala[17]=Escala[17]+1
            Escala[15]=Escala[15]+1 
        
        @Rule(OR(Chord1(chord='Bm'),Chord2(chord='Bm'),Chord3(chord='Bm'),Chord4(chord='Bm'),Chord5(chord='Bm'),Chord6(chord='Bm'),Chord7(chord='Bm'),Chord1(chord='Cbm'),Chord2(chord='Cbm'),Chord3(chord='Cbm'),Chord4(chord='Cbm'),Chord5(chord='Cbm'),Chord6(chord='Cbm'),Chord7(chord='Cbm')))
        def chordAm(self):
            Escala[2]=Escala[2]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1  
            
            Escala[23]=Escala[23]+1
            Escala[18]=Escala[18]+1
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='C7'),Chord2(chord='C7'),Chord3(chord='C7'),Chord4(chord='C7'),Chord5(chord='C7'),Chord6(chord='C7'),Chord7(chord='C7'),Chord1(chord='B#7'),Chord2(chord='B#7'),Chord3(chord='B#7'),Chord4(chord='B#7'),Chord5(chord='B#7'),Chord6(chord='B#7'),Chord7(chord='B#7')))
        def chordC7(self):
            Escala[5]=Escala[5]+1

            Escala[14]=Escala[14]+1
            
        @Rule(OR(Chord1(chord='C#7'),Chord2(chord='C#7'),Chord3(chord='C#7'),Chord4(chord='C#7'),Chord5(chord='C#7'),Chord6(chord='C#7'),Chord7(chord='C#7'),Chord1(chord='Db7'),Chord2(chord='Db7'),Chord3(chord='Db7'),Chord4(chord='Db7'),Chord5(chord='Db7'),Chord6(chord='Db7'),Chord7(chord='Db7')))
        def chordDb7(self):
            Escala[6]=Escala[6]+1
            
            Escala[15]=Escala[15]+1
                
        @Rule(OR(Chord1(chord='D7'),Chord2(chord='D7'),Chord3(chord='D7'),Chord4(chord='D7'),Chord5(chord='D7'),Chord6(chord='D7'),Chord7(chord='D7')))
        def chordD7(self):
            Escala[7]=Escala[7]+1
            
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='D#7'),Chord2(chord='D#7'),Chord3(chord='D#7'),Chord4(chord='D#7'),Chord5(chord='D#7'),Chord6(chord='D#7'),Chord7(chord='D#7'),Chord1(chord='Eb7'),Chord2(chord='Eb7'),Chord3(chord='Eb7'),Chord4(chord='Eb7'),Chord5(chord='Eb7'),Chord6(chord='Eb7'),Chord7(chord='Eb7')))
        def chordEb7(self):
            Escala[8]=Escala[8]+1
            
            Escala[17]=Escala[17]+1
            
        @Rule(OR(Chord1(chord='E7'),Chord2(chord='E7'),Chord3(chord='E7'),Chord4(chord='E7'),Chord5(chord='E7'),Chord6(chord='E7'),Chord7(chord='E7'),Chord1(chord='Fb7'),Chord2(chord='Fb7'),Chord3(chord='Fb7'),Chord4(chord='Fb7'),Chord5(chord='Fb7'),Chord6(chord='Fb7'),Chord7(chord='Fb7')))
        def chordE7(self):
            Escala[9]=Escala[9]+1
            
            Escala[18]=Escala[18]+1
            
        @Rule(OR(Chord1(chord='F7'),Chord2(chord='F7'),Chord3(chord='F7'),Chord4(chord='F7'),Chord5(chord='F7'),Chord6(chord='F7'),Chord7(chord='F7'),Chord1(chord='E#7'),Chord2(chord='E#7'),Chord3(chord='E#7'),Chord4(chord='E#7'),Chord5(chord='E#7'),Chord6(chord='E#7'),Chord7(chord='E#7')))
        def chordF7(self):
            Escala[10]=Escala[10]+1
            
            Escala[19]=Escala[19]+1
            
        @Rule(OR(Chord1(chord='F#7'),Chord2(chord='F#7'),Chord3(chord='F#7'),Chord4(chord='F#7'),Chord5(chord='F#7'),Chord6(chord='F#7'),Chord7(chord='F#7'),Chord1(chord='Gb7'),Chord2(chord='Gb7'),Chord3(chord='Gb7'),Chord4(chord='Gb7'),Chord5(chord='Gb7'),Chord6(chord='Gb7'),Chord7(chord='Gb7')))
        def chordGb7(self):
            Escala[11]=Escala[11]+1
            
            Escala[20]=Escala[20]+1
            
        @Rule(OR(Chord1(chord='G7'),Chord2(chord='G7'),Chord3(chord='G7'),Chord4(chord='G7'),Chord5(chord='G7'),Chord6(chord='G7'),Chord7(chord='G7')))
        def chordG7(self):
            Escala[0]=Escala[0]+1
            
            Escala[21]=Escala[21]+1
            
        @Rule(OR(Chord1(chord='G#7'),Chord2(chord='G#7'),Chord3(chord='G#7'),Chord4(chord='G#7'),Chord5(chord='G#7'),Chord6(chord='G#7'),Chord7(chord='G#7'),Chord1(chord='Ab7'),Chord2(chord='Ab7'),Chord3(chord='Ab7'),Chord4(chord='Ab7'),Chord5(chord='Ab7'),Chord6(chord='Ab7'),Chord7(chord='Ab7')))
        def chordAb7(self):
            Escala[1]=Escala[1]+1
            
            Escala[22]=Escala[22]+1
            
        @Rule(OR(Chord1(chord='A7'),Chord2(chord='A7'),Chord3(chord='A7'),Chord4(chord='A7'),Chord5(chord='A7'),Chord6(chord='A7'),Chord7(chord='A7')))
        def chordA7(self):
            Escala[2]=Escala[2]+1
            
            Escala[23]=Escala[23]+1
        
        @Rule(OR(Chord1(chord='A#7'),Chord2(chord='A#7'),Chord3(chord='A#7'),Chord4(chord='A#7'),Chord5(chord='A#7'),Chord6(chord='A#7'),Chord7(chord='A#7'),Chord1(chord='Bb7'),Chord2(chord='Bb7'),Chord3(chord='Bb7'),Chord4(chord='Bb7'),Chord5(chord='Bb7'),Chord6(chord='Bb7'),Chord7(chord='Bb7')))
        def chordBb7(self):
            Escala[3]=Escala[3]+1
            
            Escala[12]=Escala[12]+1
        
        @Rule(OR(Chord1(chord='B7'),Chord2(chord='B7'),Chord3(chord='B7'),Chord4(chord='B7'),Chord5(chord='B7'),Chord6(chord='B7'),Chord7(chord='B7'),Chord1(chord='Cb7'),Chord2(chord='Cb7'),Chord3(chord='Cb7'),Chord4(chord='Cb7'),Chord5(chord='Cb7'),Chord6(chord='Cb7'),Chord7(chord='Cb7')))
        def chordB7(self):
            Escala[4]=Escala[4]+1 
            
            Escala[13]=Escala[13]+1
        
        @Rule(OR(Chord1(chord='Cm7'),Chord2(chord='Cm7'),Chord3(chord='Cm7'),Chord4(chord='Cm7'),Chord5(chord='Cm7'),Chord6(chord='Cm7'),Chord7(chord='Cm7'),Chord1(chord='B#m7'),Chord2(chord='B#m7'),Chord3(chord='B#m7'),Chord4(chord='B#m7'),Chord5(chord='B#m7'),Chord6(chord='B#m7'),Chord7(chord='B#m7')))
        def chordCm7(self):
            Escala[3]=Escala[3]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            
            Escala[12]=Escala[12]+1
            Escala[19]=Escala[19]+1
            Escala[17]=Escala[17]+1
            
        @Rule(OR(Chord1(chord='C#m7'),Chord2(chord='C#m7'),Chord3(chord='C#m7'),Chord4(chord='C#m7'),Chord5(chord='C#m7'),Chord6(chord='C#m7'),Chord7(chord='C#m7'),Chord1(chord='Dbm7'),Chord2(chord='Dbm7'),Chord3(chord='Dbm7'),Chord4(chord='Dbm7'),Chord5(chord='Dbm7'),Chord6(chord='Dbm7'),Chord7(chord='Dbm7')))
        def chordDbm7(self):
            Escala[4]=Escala[4]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            
            Escala[13]=Escala[13]+1
            Escala[20]=Escala[20]+1
            Escala[18]=Escala[18]+1
                
        @Rule(OR(Chord1(chord='Dm7'),Chord2(chord='Dm7'),Chord3(chord='Dm7'),Chord4(chord='Dm7'),Chord5(chord='Dm7'),Chord6(chord='Dm7'),Chord7(chord='Dm7')))
        def chordDm7(self):
            Escala[5]=Escala[5]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            
            Escala[14]=Escala[14]+1
            Escala[21]=Escala[21]+1
            Escala[19]=Escala[19]+1
            
        @Rule(OR(Chord1(chord='D#m7'),Chord2(chord='D#m7'),Chord3(chord='D#m7'),Chord4(chord='D#m7'),Chord5(chord='D#m7'),Chord6(chord='D#m7'),Chord7(chord='D#m7'),Chord1(chord='Ebm7'),Chord2(chord='Ebm7'),Chord3(chord='Ebm7'),Chord4(chord='Ebm7'),Chord5(chord='Ebm7'),Chord6(chord='Ebm7'),Chord7(chord='Ebm7')))
        def chordEbm7(self):
            Escala[6]=Escala[6]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1 
            
            Escala[15]=Escala[15]+1
            Escala[22]=Escala[22]+1
            Escala[20]=Escala[20]+1 
            
        @Rule(OR(Chord1(chord='Em7'),Chord2(chord='Em7'),Chord3(chord='Em7'),Chord4(chord='Em7'),Chord5(chord='Em7'),Chord6(chord='Em7'),Chord7(chord='Em7'),Chord1(chord='Fbm7'),Chord2(chord='Fbm7'),Chord3(chord='Fbm7'),Chord4(chord='Fbm7'),Chord5(chord='Fbm7'),Chord6(chord='Fbm7'),Chord7(chord='Fbm7')))
        def chordEm7(self):
            Escala[7]=Escala[7]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            
            Escala[16]=Escala[16]+1
            Escala[23]=Escala[23]+1
            Escala[21]=Escala[21]+1 
            
        @Rule(OR(Chord1(chord='Fm7'),Chord2(chord='Fm7'),Chord3(chord='Fm7'),Chord4(chord='Fm7'),Chord5(chord='Fm7'),Chord6(chord='Fm7'),Chord7(chord='Fm7'),Chord1(chord='E#m7'),Chord2(chord='E#m7'),Chord3(chord='E#m7'),Chord4(chord='E#m7'),Chord5(chord='E#m7'),Chord6(chord='E#m7'),Chord7(chord='E#m7')))
        def chordFm7(self):
            Escala[8]=Escala[8]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1
            
            Escala[17]=Escala[17]+1
            Escala[12]=Escala[12]+1
            Escala[22]=Escala[22]+1 
            
        @Rule(OR(Chord1(chord='F#m7'),Chord2(chord='F#m7'),Chord3(chord='F#m7'),Chord4(chord='F#m7'),Chord5(chord='F#m7'),Chord6(chord='F#m7'),Chord7(chord='F#m7'),Chord1(chord='Gbm7'),Chord2(chord='Gbm7'),Chord3(chord='Gbm7'),Chord4(chord='Gbm7'),Chord5(chord='Gbm7'),Chord6(chord='Gbm7'),Chord7(chord='Gbm7')))
        def chordGbm7(self):
            Escala[9]=Escala[9]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1 
            
            Escala[18]=Escala[18]+1
            Escala[13]=Escala[13]+1
            Escala[23]=Escala[23]+1 
            
        @Rule(OR(Chord1(chord='Gm7'),Chord2(chord='Gm7'),Chord3(chord='Gm7'),Chord4(chord='Gm7'),Chord5(chord='Gm7'),Chord6(chord='Gm7'),Chord7(chord='Gm7')))
        def chordGm7(self):
            Escala[10]=Escala[10]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1
            
            Escala[19]=Escala[19]+1
            Escala[14]=Escala[14]+1
            Escala[12]=Escala[12]+1 
        @Rule(OR(Chord1(chord='G#m7'),Chord2(chord='G#m7'),Chord3(chord='G#m7'),Chord4(chord='G#m7'),Chord5(chord='G#m7'),Chord6(chord='G#m7'),Chord7(chord='G#m7'),Chord1(chord='Abm7'),Chord2(chord='Abm7'),Chord3(chord='Abm7'),Chord4(chord='Abm7'),Chord5(chord='Abm7'),Chord6(chord='Abm7'),Chord7(chord='Abm7')))
        def chordAbm7(self):
            Escala[11]=Escala[11]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1 
            
            Escala[20]=Escala[20]+1
            Escala[15]=Escala[15]+1
            Escala[13]=Escala[13]+1
            
        @Rule(OR(Chord1(chord='Am7'),Chord2(chord='Am7'),Chord3(chord='Am7'),Chord4(chord='Am7'),Chord5(chord='Am7'),Chord6(chord='Am7'),Chord7(chord='Am7')))
        def chordAm7(self):
            Escala[0]=Escala[0]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1 
            
            Escala[21]=Escala[21]+1
            Escala[16]=Escala[16]+1
            Escala[14]=Escala[14]+1 
        
        @Rule(OR(Chord1(chord='A#m7'),Chord2(chord='A#m7'),Chord3(chord='A#m7'),Chord4(chord='A#m7'),Chord5(chord='A#m7'),Chord6(chord='A#m7'),Chord7(chord='A#m7'),Chord1(chord='Bbm7'),Chord2(chord='Bbm7'),Chord3(chord='Bbm7'),Chord4(chord='Bbm7'),Chord5(chord='Bbm7'),Chord6(chord='Bbm7'),Chord7(chord='Bbm7')))
        def chordBbm7(self):
            Escala[1]=Escala[1]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1   
            
            Escala[22]=Escala[22]+1
            Escala[17]=Escala[17]+1
            Escala[15]=Escala[15]+1 
        
        @Rule(OR(Chord1(chord='Bm7'),Chord2(chord='Bm7'),Chord3(chord='Bm7'),Chord4(chord='Bm7'),Chord5(chord='Bm7'),Chord6(chord='Bm7'),Chord7(chord='Bm7'),Chord1(chord='Cbm7'),Chord2(chord='Cbm7'),Chord3(chord='Cbm7'),Chord4(chord='Cbm7'),Chord5(chord='Cbm7'),Chord6(chord='Cbm7'),Chord7(chord='Cbm7')))
        def chordAm7(self):
            Escala[2]=Escala[2]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1  
            
            Escala[23]=Escala[23]+1
            Escala[18]=Escala[18]+1
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='Cmaj7'),Chord2(chord='Cmaj7'),Chord3(chord='Cmaj7'),Chord4(chord='Cmaj7'),Chord5(chord='Cmaj7'),Chord6(chord='Cmaj7'),Chord7(chord='Cmaj7'),Chord1(chord='B#maj7'),Chord2(chord='B#maj7'),Chord3(chord='B#maj7'),Chord4(chord='B#maj7'),Chord5(chord='B#maj7'),Chord6(chord='B#maj7'),Chord7(chord='B#maj7')))
        def chordCmaj7(self):
            Escala[0]=Escala[0]+1
            Escala[7]=Escala[7]+1
            
            Escala[21]=Escala[21]+1
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='C#maj7'),Chord2(chord='C#maj7'),Chord3(chord='C#maj7'),Chord4(chord='C#maj7'),Chord5(chord='C#maj7'),Chord6(chord='C#maj7'),Chord7(chord='C#maj7'),Chord1(chord='Dbmaj7'),Chord2(chord='Dbmaj7'),Chord3(chord='Dbmaj7'),Chord4(chord='Dbmaj7'),Chord5(chord='Dbmaj7'),Chord6(chord='Dbmaj7'),Chord7(chord='Dbmaj7')))
        def chordDbmaj7(self):
            Escala[1]=Escala[1]+1
            Escala[8]=Escala[8]+1
            
            Escala[22]=Escala[22]+1
            Escala[17]=Escala[17]+1
                
        @Rule(OR(Chord1(chord='Dmaj7'),Chord2(chord='Dmaj7'),Chord3(chord='Dmaj7'),Chord4(chord='Dmaj7'),Chord5(chord='Dmaj7'),Chord6(chord='Dmaj7'),Chord7(chord='Dmaj7')))
        def chordDmaj7(self):
            Escala[2]=Escala[2]+1
            Escala[9]=Escala[9]+1
            
            Escala[23]=Escala[23]+1
            Escala[18]=Escala[18]+1
            
        @Rule(OR(Chord1(chord='D#maj7'),Chord2(chord='D#maj7'),Chord3(chord='D#maj7'),Chord4(chord='D#maj7'),Chord5(chord='D#maj7'),Chord6(chord='D#maj7'),Chord7(chord='D#maj7'),Chord1(chord='Ebmaj7'),Chord2(chord='Ebmaj7'),Chord3(chord='Ebmaj7'),Chord4(chord='Ebmaj7'),Chord5(chord='Ebmaj7'),Chord6(chord='Ebmaj7'),Chord7(chord='Ebmaj7')))
        def chordEbmaj7(self):
            Escala[3]=Escala[3]+1
            Escala[10]=Escala[10]+1
            
            Escala[12]=Escala[12]+1
            Escala[19]=Escala[19]+1
            
        @Rule(OR(Chord1(chord='Emaj7'),Chord2(chord='Emaj7'),Chord3(chord='Emaj7'),Chord4(chord='Emaj7'),Chord5(chord='Emaj7'),Chord6(chord='Emaj7'),Chord7(chord='Emaj7'),Chord1(chord='Fbmaj7'),Chord2(chord='Fbmaj7'),Chord3(chord='Fbmaj7'),Chord4(chord='Fbmaj7'),Chord5(chord='Fbmaj7'),Chord6(chord='Fbmaj7'),Chord7(chord='Fbmaj7')))
        def chordEmaj7(self):
            Escala[4]=Escala[4]+1
            Escala[11]=Escala[11]+1
            
            Escala[13]=Escala[13]+1
            Escala[20]=Escala[20]+1
            
        @Rule(OR(Chord1(chord='Fmaj7'),Chord2(chord='Fmaj7'),Chord3(chord='Fmaj7'),Chord4(chord='Fmaj7'),Chord5(chord='Fmaj7'),Chord6(chord='Fmaj7'),Chord7(chord='Fmaj7'),Chord1(chord='E#maj7'),Chord2(chord='E#maj7'),Chord3(chord='E#maj7'),Chord4(chord='E#maj7'),Chord5(chord='E#maj7'),Chord6(chord='E#maj7'),Chord7(chord='E#maj7')))
        def chordFmaj7(self):
            Escala[5]=Escala[5]+1
            Escala[0]=Escala[0]+1
            
            Escala[14]=Escala[14]+1
            Escala[21]=Escala[21]+1
            
        @Rule(OR(Chord1(chord='F#maj7'),Chord2(chord='F#maj7'),Chord3(chord='F#maj7'),Chord4(chord='F#maj7'),Chord5(chord='F#maj7'),Chord6(chord='F#maj7'),Chord7(chord='F#maj7'),Chord1(chord='Gbmaj7'),Chord2(chord='Gbmaj7'),Chord3(chord='Gbmaj7'),Chord4(chord='Gbmaj7'),Chord5(chord='Gbmaj7'),Chord6(chord='Gbmaj7'),Chord7(chord='Gbmaj7')))
        def chordGbmaj7(self):
            Escala[6]=Escala[6]+1
            Escala[1]=Escala[1]+1 
            
            Escala[15]=Escala[15]+1
            Escala[22]=Escala[22]+1
            
        @Rule(OR(Chord1(chord='Gmaj7'),Chord2(chord='Gmaj7'),Chord3(chord='Gmaj7'),Chord4(chord='Gmaj7'),Chord5(chord='Gmaj7'),Chord6(chord='Gmaj7'),Chord7(chord='Gmaj7')))
        def chordGmaj7(self):
            Escala[7]=Escala[7]+1
            Escala[2]=Escala[2]+1
            
            Escala[16]=Escala[16]+1
            Escala[23]=Escala[23]+1
            
        @Rule(OR(Chord1(chord='G#maj7'),Chord2(chord='G#maj7'),Chord3(chord='G#maj7'),Chord4(chord='G#maj7'),Chord5(chord='G#maj7'),Chord6(chord='G#maj7'),Chord7(chord='G#maj7'),Chord1(chord='Abmaj7'),Chord2(chord='Abmaj7'),Chord3(chord='Abmaj7'),Chord4(chord='Abmaj7'),Chord5(chord='Abmaj7'),Chord6(chord='Abmaj7'),Chord7(chord='Abmaj7')))
        def chordAbmaj7(self):
            Escala[8]=Escala[8]+1
            Escala[3]=Escala[3]+1 
            
            Escala[17]=Escala[17]+1
            Escala[12]=Escala[12]+1
            
        @Rule(OR(Chord1(chord='Amaj7'),Chord2(chord='Amaj7'),Chord3(chord='Amaj7'),Chord4(chord='Amaj7'),Chord5(chord='Amaj7'),Chord6(chord='Amaj7'),Chord7(chord='Amaj7')))
        def chordAmaj7(self):
            Escala[9]=Escala[9]+1
            Escala[4]=Escala[4]+1 
            
            Escala[18]=Escala[18]+1
            Escala[13]=Escala[13]+1
        
        @Rule(OR(Chord1(chord='A#maj7'),Chord2(chord='A#maj7'),Chord3(chord='A#maj7'),Chord4(chord='A#maj7'),Chord5(chord='A#maj7'),Chord6(chord='A#maj7'),Chord7(chord='A#maj7'),Chord1(chord='Bbmaj7'),Chord2(chord='Bbmaj7'),Chord3(chord='Bbmaj7'),Chord4(chord='Bbmaj7'),Chord5(chord='Bbmaj7'),Chord6(chord='Bbmaj7'),Chord7(chord='Bbmaj7')))
        def chordBbmaj7(self):
            Escala[10]=Escala[10]+1
            Escala[5]=Escala[5]+1   
            
            Escala[19]=Escala[19]+1
            Escala[14]=Escala[14]+1
        
        @Rule(OR(Chord1(chord='Bmaj7'),Chord2(chord='Bmaj7'),Chord3(chord='Bmaj7'),Chord4(chord='Bmaj7'),Chord5(chord='Bmaj7'),Chord6(chord='Bmaj7'),Chord7(chord='Bmaj7'),Chord1(chord='Cbmaj7'),Chord2(chord='Cbmaj7'),Chord3(chord='Cbmaj7'),Chord4(chord='Cbmaj7'),Chord5(chord='Cbmaj7'),Chord6(chord='Cbmaj7'),Chord7(chord='Cbmaj7')))
        def chordBmaj7(self):
            Escala[11]=Escala[11]+1
            Escala[6]=Escala[6]+1   
            
            Escala[20]=Escala[20]+1
            Escala[15]=Escala[15]+1 
            
        @Rule(OR(Chord1(chord='Csus2'),Chord2(chord='Csus2'),Chord3(chord='Csus2'),Chord4(chord='Csus2'),Chord5(chord='Csus2'),Chord6(chord='Csus2'),Chord7(chord='Csus2'),Chord1(chord='B#sus2'),Chord2(chord='B#sus2'),Chord3(chord='B#sus2'),Chord4(chord='B#sus2'),Chord5(chord='B#sus2'),Chord6(chord='B#sus2'),Chord7(chord='B#sus2')))
        def chordCsus2(self):
            Escala[0]=Escala[0]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1
            Escala[10]=Escala[10]+1
            
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            
        @Rule(OR(Chord1(chord='C#sus2'),Chord2(chord='C#sus2'),Chord3(chord='C#sus2'),Chord4(chord='C#sus2'),Chord5(chord='C#sus2'),Chord6(chord='C#sus2'),Chord7(chord='C#sus2'),Chord1(chord='Dbsus2'),Chord2(chord='Dbsus2'),Chord3(chord='Dbsus2'),Chord4(chord='Dbsus2'),Chord5(chord='Dbsus2'),Chord6(chord='Dbsus2'),Chord7(chord='Dbsus2')))
        def chordDbsus2(self):
            Escala[1]=Escala[1]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1
            Escala[11]=Escala[11]+1
            
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
                
        @Rule(OR(Chord1(chord='Dsus2'),Chord2(chord='Dsus2'),Chord3(chord='Dsus2'),Chord4(chord='Dsus2'),Chord5(chord='Dsus2'),Chord6(chord='Dsus2'),Chord7(chord='Dsus2')))
        def chordDsus2(self):
            Escala[2]=Escala[2]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1
            Escala[0]=Escala[0]+1
            
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            
        @Rule(OR(Chord1(chord='D#sus2'),Chord2(chord='D#sus2'),Chord3(chord='D#sus2'),Chord4(chord='D#sus2'),Chord5(chord='D#sus2'),Chord6(chord='D#sus2'),Chord7(chord='D#sus2'),Chord1(chord='Ebsus2'),Chord2(chord='Ebsus2'),Chord3(chord='Ebsus2'),Chord4(chord='Ebsus2'),Chord5(chord='Ebsus2'),Chord6(chord='Ebsus2'),Chord7(chord='Ebsus2')))
        def chordEbsus2(self):
            Escala[3]=Escala[3]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            Escala[1]=Escala[1]+1
            
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            
        @Rule(OR(Chord1(chord='Esus2'),Chord2(chord='Esus2'),Chord3(chord='Esus2'),Chord4(chord='Esus2'),Chord5(chord='Esus2'),Chord6(chord='Esus2'),Chord7(chord='Esus2'),Chord1(chord='Fbsus2'),Chord2(chord='Fbsus2'),Chord3(chord='Fbsus2'),Chord4(chord='Fbsus2'),Chord5(chord='Fbsus2'),Chord6(chord='Fbsus2'),Chord7(chord='Fbsus2')))
        def chordEsus2(self):
            Escala[4]=Escala[4]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            Escala[2]=Escala[2]+1
            
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
            
        @Rule(OR(Chord1(chord='Fsus2'),Chord2(chord='Fsus2'),Chord3(chord='Fsus2'),Chord4(chord='Fsus2'),Chord5(chord='Fsus2'),Chord6(chord='Fsus2'),Chord7(chord='Fsus2'),Chord1(chord='E#sus2'),Chord2(chord='E#sus2'),Chord3(chord='E#sus2'),Chord4(chord='E#sus2'),Chord5(chord='E#sus2'),Chord6(chord='E#sus2'),Chord7(chord='E#sus2')))
        def chordFsus2(self):
            Escala[5]=Escala[5]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            Escala[3]=Escala[3]+1
            
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
            
        @Rule(OR(Chord1(chord='F#sus2'),Chord2(chord='F#sus2'),Chord3(chord='F#sus2'),Chord4(chord='F#sus2'),Chord5(chord='F#sus2'),Chord6(chord='F#sus2'),Chord7(chord='F#sus2'),Chord1(chord='Gbsus2'),Chord2(chord='Gbsus2'),Chord3(chord='Gbsus2'),Chord4(chord='Gbsus2'),Chord5(chord='Gbsus2'),Chord6(chord='Gbsus2'),Chord7(chord='Gbsus2')))
        def chordGbsus2(self):
            Escala[6]=Escala[6]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1
            Escala[4]=Escala[4]+1
            
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1
            
        @Rule(OR(Chord1(chord='Gsus2'),Chord2(chord='Gsus2'),Chord3(chord='Gsus2'),Chord4(chord='Gsus2'),Chord5(chord='Gsus2'),Chord6(chord='Gsus2'),Chord7(chord='Gsus2')))
        def chordGsus2(self):
            Escala[7]=Escala[7]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            Escala[5]=Escala[5]+1
            
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='G#sus2'),Chord2(chord='G#sus2'),Chord3(chord='G#sus2'),Chord4(chord='G#sus2'),Chord5(chord='G#sus2'),Chord6(chord='G#sus2'),Chord7(chord='G#sus2'),Chord1(chord='Absus2'),Chord2(chord='Absus2'),Chord3(chord='Absus2'),Chord4(chord='Absus2'),Chord5(chord='Absus2'),Chord6(chord='Absus2'),Chord7(chord='Absus2')))
        def chordAbsus2(self):
            Escala[8]=Escala[8]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1
            Escala[6]=Escala[6]+1
            
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
            
        @Rule(OR(Chord1(chord='Asus2'),Chord2(chord='Asus2'),Chord3(chord='Asus2'),Chord4(chord='Asus2'),Chord5(chord='Asus2'),Chord6(chord='Asus2'),Chord7(chord='Asus2')))
        def chordAsus2(self):
            Escala[9]=Escala[9]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1
            Escala[7]=Escala[7]+1
            
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
        
        @Rule(OR(Chord1(chord='A#sus2'),Chord2(chord='A#sus2'),Chord3(chord='A#sus2'),Chord4(chord='A#sus2'),Chord5(chord='A#sus2'),Chord6(chord='A#sus2'),Chord7(chord='A#sus2'),Chord1(chord='Bbsus2'),Chord2(chord='Bbsus2'),Chord3(chord='Bbsus2'),Chord4(chord='Bbsus2'),Chord5(chord='Bbsus2'),Chord6(chord='Bbsus2'),Chord7(chord='Bbsus2')))
        def chordBbsus2(self):
            Escala[10]=Escala[10]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1
            Escala[8]=Escala[8]+1
            
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
        
        @Rule(OR(Chord1(chord='Bsus2'),Chord2(chord='Bsus2'),Chord3(chord='Bsus2'),Chord4(chord='Bsus2'),Chord5(chord='Bsus2'),Chord6(chord='Bsus2'),Chord7(chord='Bsus2'),Chord1(chord='Cbsus2'),Chord2(chord='Cbsus2'),Chord3(chord='Cbsus2'),Chord4(chord='Cbsus2'),Chord5(chord='Cbsus2'),Chord6(chord='Cbsus2'),Chord7(chord='Cbsus2')))
        def chordBsus2(self):
            Escala[11]=Escala[11]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1
            Escala[9]=Escala[9]+1
            
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
            
        @Rule(OR(Chord1(chord='Csus4'),Chord2(chord='Csus4'),Chord3(chord='Csus4'),Chord4(chord='Csus4'),Chord5(chord='Csus4'),Chord6(chord='Csus4'),Chord7(chord='Csus4'),Chord1(chord='B#sus4'),Chord2(chord='B#sus4'),Chord3(chord='B#sus4'),Chord4(chord='B#sus4'),Chord5(chord='B#sus4'),Chord6(chord='B#sus4'),Chord7(chord='B#sus4')))
        def chordCsus4(self):
            Escala[0]=Escala[0]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            
        @Rule(OR(Chord1(chord='C#sus4'),Chord2(chord='C#sus4'),Chord3(chord='C#sus4'),Chord4(chord='C#sus4'),Chord5(chord='C#sus4'),Chord6(chord='C#sus4'),Chord7(chord='C#sus4'),Chord1(chord='Dbsus4'),Chord2(chord='Dbsus4'),Chord3(chord='Dbsus4'),Chord4(chord='Dbsus4'),Chord5(chord='Dbsus4'),Chord6(chord='Dbsus4'),Chord7(chord='Dbsus4')))
        def chordDbsus4(self):
            Escala[1]=Escala[1]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
                
        @Rule(OR(Chord1(chord='Dsus4'),Chord2(chord='Dsus4'),Chord3(chord='Dsus4'),Chord4(chord='Dsus4'),Chord5(chord='Dsus4'),Chord6(chord='Dsus4'),Chord7(chord='Dsus4')))
        def chordDsus4(self):
            Escala[2]=Escala[2]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            
        @Rule(OR(Chord1(chord='D#sus4'),Chord2(chord='D#sus4'),Chord3(chord='D#sus4'),Chord4(chord='D#sus4'),Chord5(chord='D#sus4'),Chord6(chord='D#sus4'),Chord7(chord='D#sus4'),Chord1(chord='Ebsus4'),Chord2(chord='Ebsus4'),Chord3(chord='Ebsus4'),Chord4(chord='Ebsus4'),Chord5(chord='Ebsus4'),Chord6(chord='Ebsus4'),Chord7(chord='Ebsus4')))
        def chordEbsus4(self):
            Escala[3]=Escala[3]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1
            
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            
        @Rule(OR(Chord1(chord='Esus4'),Chord2(chord='Esus4'),Chord3(chord='Esus4'),Chord4(chord='Esus4'),Chord5(chord='Esus4'),Chord6(chord='Esus4'),Chord7(chord='Esus4'),Chord1(chord='Fbsus4'),Chord2(chord='Fbsus4'),Chord3(chord='Fbsus4'),Chord4(chord='Fbsus4'),Chord5(chord='Fbsus4'),Chord6(chord='Fbsus4'),Chord7(chord='Fbsus4')))
        def chordEsus4(self):
            Escala[4]=Escala[4]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
            
        @Rule(OR(Chord1(chord='Fsus4'),Chord2(chord='Fsus4'),Chord3(chord='Fsus4'),Chord4(chord='Fsus4'),Chord5(chord='Fsus4'),Chord6(chord='Fsus4'),Chord7(chord='Fsus4'),Chord1(chord='E#sus4'),Chord2(chord='E#sus4'),Chord3(chord='E#sus4'),Chord4(chord='E#sus4'),Chord5(chord='E#sus4'),Chord6(chord='E#sus4'),Chord7(chord='E#sus4')))
        def chordFsus4(self):
            Escala[5]=Escala[5]+1
            Escala[8]=Escala[8]+1
            Escala[10]=Escala[10]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1
            
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
            
        @Rule(OR(Chord1(chord='F#sus4'),Chord2(chord='F#sus4'),Chord3(chord='F#sus4'),Chord4(chord='F#sus4'),Chord5(chord='F#sus4'),Chord6(chord='F#sus4'),Chord7(chord='F#sus4'),Chord1(chord='Gbsus4'),Chord2(chord='Gbsus4'),Chord3(chord='Gbsus4'),Chord4(chord='Gbsus4'),Chord5(chord='Gbsus4'),Chord6(chord='Gbsus4'),Chord7(chord='Gbsus4')))
        def chordGbsus4(self):
            Escala[6]=Escala[6]+1
            Escala[9]=Escala[9]+1
            Escala[11]=Escala[11]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1
            
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1
            
        @Rule(OR(Chord1(chord='Gsus4'),Chord2(chord='Gsus4'),Chord3(chord='Gsus4'),Chord4(chord='Gsus4'),Chord5(chord='Gsus4'),Chord6(chord='Gsus4'),Chord7(chord='Gsus4')))
        def chordGsus4(self):
            Escala[7]=Escala[7]+1
            Escala[10]=Escala[10]+1
            Escala[0]=Escala[0]+1
            Escala[3]=Escala[3]+1
            Escala[5]=Escala[5]+1
            
            Escala[19]=Escala[19]+1
            Escala[21]=Escala[21]+1
            Escala[12]=Escala[12]+1
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            
        @Rule(OR(Chord1(chord='G#sus4'),Chord2(chord='G#sus4'),Chord3(chord='G#sus4'),Chord4(chord='G#sus4'),Chord5(chord='G#sus4'),Chord6(chord='G#sus4'),Chord7(chord='G#sus4'),Chord1(chord='Absus4'),Chord2(chord='Absus4'),Chord3(chord='Absus4'),Chord4(chord='Absus4'),Chord5(chord='Absus4'),Chord6(chord='Absus4'),Chord7(chord='Absus4')))
        def chordAbsus4(self):
            Escala[8]=Escala[8]+1
            Escala[11]=Escala[11]+1
            Escala[1]=Escala[1]+1
            Escala[4]=Escala[4]+1
            Escala[6]=Escala[6]+1
            
            Escala[20]=Escala[20]+1
            Escala[22]=Escala[22]+1
            Escala[13]=Escala[13]+1
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
            
        @Rule(OR(Chord1(chord='Asus4'),Chord2(chord='Asus4'),Chord3(chord='Asus4'),Chord4(chord='Asus4'),Chord5(chord='Asus4'),Chord6(chord='Asus4'),Chord7(chord='Asus4')))
        def chordAsus4(self):
            Escala[9]=Escala[9]+1
            Escala[0]=Escala[0]+1
            Escala[2]=Escala[2]+1
            Escala[5]=Escala[5]+1
            Escala[7]=Escala[7]+1
            
            Escala[21]=Escala[21]+1
            Escala[23]=Escala[23]+1
            Escala[14]=Escala[14]+1
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
        
        @Rule(OR(Chord1(chord='A#sus4'),Chord2(chord='A#sus4'),Chord3(chord='A#sus4'),Chord4(chord='A#sus4'),Chord5(chord='A#sus4'),Chord6(chord='A#sus4'),Chord7(chord='A#sus4'),Chord1(chord='Bbsus4'),Chord2(chord='Bbsus4'),Chord3(chord='Bbsus4'),Chord4(chord='Bbsus4'),Chord5(chord='Bbsus4'),Chord6(chord='Bbsus4'),Chord7(chord='Bbsus4')))
        def chordBbsus4(self):
            Escala[10]=Escala[10]+1
            Escala[1]=Escala[1]+1
            Escala[3]=Escala[3]+1
            Escala[6]=Escala[6]+1
            Escala[8]=Escala[8]+1
            
            Escala[22]=Escala[22]+1
            Escala[12]=Escala[12]+1
            Escala[15]=Escala[15]+1
            Escala[17]=Escala[17]+1
            Escala[19]=Escala[19]+1
        
        @Rule(OR(Chord1(chord='Bsus4'),Chord2(chord='Bsus4'),Chord3(chord='Bsus4'),Chord4(chord='Bsus4'),Chord5(chord='Bsus4'),Chord6(chord='Bsus4'),Chord7(chord='Bsus4'),Chord1(chord='Cbsus4'),Chord2(chord='Cbsus4'),Chord3(chord='Cbsus4'),Chord4(chord='Cbsus4'),Chord5(chord='Cbsus4'),Chord6(chord='Cbsus4'),Chord7(chord='Cbsus4')))
        def chordBsus4(self):
            Escala[11]=Escala[11]+1
            Escala[2]=Escala[2]+1
            Escala[4]=Escala[4]+1
            Escala[7]=Escala[7]+1
            Escala[9]=Escala[9]+1
            
            Escala[23]=Escala[23]+1
            Escala[13]=Escala[13]+1
            Escala[16]=Escala[16]+1
            Escala[18]=Escala[18]+1
            Escala[20]=Escala[20]+1
    engine = DetectarEscala()
    engine.reset()
    engine.declare(Chord1(chord=Acorde1))
    engine.declare(Chord2(chord=Acorde2))
    engine.declare(Chord3(chord=Acorde3))
    engine.declare(Chord4(chord=Acorde4))
    engine.declare(Chord5(chord=Acorde5))
    engine.declare(Chord6(chord=Acorde6))
    engine.declare(Chord7(chord=Acorde7))
    engine.run()
    print(Escala)
    aux=[False,False,False,False]
    max_p = max(Escala)
    for i in range(len(Escala)):
        if Escala[i]==max_p:
            EscalasProb.append(N_Escala(str(i)))  
    print(EscalasProb)          
    class ElegirEscala(KnowledgeEngine):     
        @Rule(AND(Num_EscalasProbables(Num='2'),OR(
            Chord1(chord=PartirEscala0(EscalasProb[0])),Chord2(chord=PartirEscala0(EscalasProb[0])),Chord3(chord=PartirEscala0(EscalasProb[0])),Chord4(chord=PartirEscala0(EscalasProb[0])),Chord5(chord=PartirEscala0(EscalasProb[0])),Chord6(chord=PartirEscala0(EscalasProb[0])),Chord7(chord=PartirEscala0(EscalasProb[0])),
            Chord1(chord=PartirEscala1(EscalasProb[0])),Chord2(chord=PartirEscala1(EscalasProb[0])),Chord3(chord=PartirEscala1(EscalasProb[0])),Chord4(chord=PartirEscala1(EscalasProb[0])),Chord5(chord=PartirEscala1(EscalasProb[0])),Chord6(chord=PartirEscala1(EscalasProb[0])),Chord7(chord=PartirEscala1(EscalasProb[0]))
            )))
        def EscalaM(self):
            engine.declare(EscalaMayorBool(valor='True'))
        @Rule(AND(Num_EscalasProbables(Num='2'),OR(
            Chord1(chord=PartirEscala0(EscalasProb[1])),Chord2(chord=PartirEscala0(EscalasProb[1])),Chord3(chord=PartirEscala0(EscalasProb[1])),Chord4(chord=PartirEscala0(EscalasProb[1])),Chord5(chord=PartirEscala0(EscalasProb[1])),Chord6(chord=PartirEscala0(EscalasProb[1])),Chord7(chord=PartirEscala0(EscalasProb[1])),
            Chord1(chord=PartirEscala1(EscalasProb[1])),Chord2(chord=PartirEscala1(EscalasProb[1])),Chord3(chord=PartirEscala1(EscalasProb[1])),Chord4(chord=PartirEscala1(EscalasProb[1])),Chord5(chord=PartirEscala1(EscalasProb[1])),Chord6(chord=PartirEscala1(EscalasProb[1])),Chord7(chord=PartirEscala1(EscalasProb[1]))
            )))
        def Escalam(self):
            engine.declare(EscalaMenorBool(valor='True'))
        @Rule(AND(Num_EscalasProbables(Num='2'),EscalaMayorBool(valor='True'),EscalaMenorBool(valor='True')))
        def Ambas(self):
            aux[0]=True
        @Rule(AND(Num_EscalasProbables(Num='2'),EscalaMayorBool(valor='True'),EscalaMenorBool(valor='False')))
        def Mayor(self):
            aux[1]=True
        @Rule(AND(Num_EscalasProbables(Num='2'),EscalaMayorBool(valor='False'),EscalaMenorBool(valor='True')))
        def Menor(self):
            aux[2]=True
        @Rule(AND(Num_EscalasProbables(Num='2'),EscalaMayorBool(valor='False'),EscalaMenorBool(valor='False')))
        def Ambas2(self):
            aux[3]=True
        @Rule(NOT(Num_EscalasProbables(Num='2')))
        def Faltante(self):
            texto.set("Faltan Acordes para ser mas precisos, las "+str(len(EscalasProb))+" posibles escalas son: ")
            texto1.set(str(EscalasProb))
            ventana.geometry("565x335")
            print("Faltan Acordes para ser mas precisos, las "+str(len(EscalasProb))+" posibles escalas son: "+str(EscalasProb))
    engine = ElegirEscala()
    engine.reset()
    engine.declare(Chord1(chord=Acorde1))
    engine.declare(Chord2(chord=Acorde2))
    engine.declare(Chord3(chord=Acorde3))
    engine.declare(Chord4(chord=Acorde4))
    engine.declare(Chord5(chord=Acorde5))
    engine.declare(Chord6(chord=Acorde6))
    engine.declare(Chord7(chord=Acorde7))
    engine.declare(Num_EscalasProbables(Num=str(len(EscalasProb))))
    engine.declare(EscalaMayorBool(valor='False'))
    engine.declare(EscalaMenorBool(valor='False'))
    engine.run()
    print(aux)
    if aux[0] and (aux[1] and aux[2]):
        texto.set("Las dos posibles escalas son: ")
        texto1.set(EscalasProb[0]+" y "+EscalasProb[1])
        print("Las dos posibles escalas son: "+EscalasProb[0]+" y "+EscalasProb[1])
        ventana.geometry("565x300")
    elif aux[1]:
        texto.set("La escala mas probable es : ")
        texto1.set(EscalasProb[0])
        print("La escala mas probable es : "+EscalasProb[0])
        ventana.geometry("565x300")
    elif aux[2]:
        texto.set("La escala mas probable es : ")  
        texto1.set(EscalasProb[1])  
        print("La escala mas probable es : "+EscalasProb[1])  
        ventana.geometry("565x300")
    elif aux[3]:
        texto.set("Las dos posibles escalas son: ")
        texto1.set(EscalasProb[0]+" y "+EscalasProb[1])
        print("Las dos posibles escalas son: "+EscalasProb[0]+" y "+EscalasProb[1]) 
        ventana.geometry("565x300")
ventana = Tk()
ventana.configure(bg='#1d2025')
texto=StringVar()
texto1=StringVar()
texto.set("Escala: ")
acordesCB=('C','Cm','B#','B#m','C#','C#m','Db','Dbm','D','Dm','D#','D#m','Eb','Ebm','E','Em','Fb','Fbm','F','Fm','E#','E#m','F#','F#m','Gb','Gbm','G','Gm','G#','G#m','Ab','Abm',
'A','Am','A#','A#m','Bb','Bbm','B','Bm','Cb','Cbm','C7','Cm7','B#7','B#m7','C#7','C#m7','Db7','Dbm7','D7','Dm7','D#7','D#m7','Eb7','Ebm7','E7','Em7','Fb7','Fbm7','F7','Fm7','E#7','E#m7','F#7',
'F#m7','Gb7','Gbm7','G7','Gm7','G#7','G#m7','Ab7','Abm7','A7','Am7','A#7','A#m7','Bb7','Bbm7','B7','Bm7','Cb7','Cbm7','Csus2','Cmaj7','B#sus2','B#maj7','C#sus2','C#maj7','Dbsus2','Dbmaj7','Dsus2',
'Dmaj7','D#sus2','D#maj7','Ebsus2','Ebmaj7','Esus2','Emaj7','Fbsus2','Fbmaj7','Fsus2','Fmaj7','E#sus2','E#maj7','F#sus2','F#maj7','Gbsus2','Gbmaj7','Gsus2','Gmaj7','G#sus2','G#maj7','Absus2','Abmaj7',
'Asus2','Amaj7','A#sus2','A#maj7','Bbsus2','Bbmaj7','Bsus2','Bmaj7','Cbsus2','Cbmaj7','Csus4','B#sus4','C#sus4','Dbsus4','Dsus4','D#sus4','Ebsus4','Esus4','Fbsus4','Fsus4','E#sus4','F#sus4','Gbsus4',
'Gsus4','G#sus4','Absus4','Asus4','A#sus4','Bbsus4','Bsus4','Cbsus4')
combo1 = ttk.Combobox(ventana,font='Verdana 10')
combo1.place(x=110,y=11)
combo1['values']=acordesCB
combo2 = ttk.Combobox(ventana,font='Verdana 10')
combo2.place(x=110,y=43)
combo2['values']=acordesCB
combo3 = ttk.Combobox(ventana,font='Verdana 10')
combo3.place(x=110,y=75)
combo3['values']=acordesCB
combo4 = ttk.Combobox(ventana,font='Verdana 10')
combo4.place(x=110,y=107)
combo4['values']=acordesCB
combo5 = ttk.Combobox(ventana,font='Verdana 10')
combo5.place(x=110,y=139)
combo5['values']=acordesCB
combo6 = ttk.Combobox(ventana,font='Verdana 10')
combo6.place(x=110,y=171)
combo6['values']=acordesCB
combo7 = ttk.Combobox(ventana,font='Verdana 10')
combo7.place(x=110,y=203)
combo7['values']=acordesCB
boton=Button(ventana,command=CalEscala,text="Detectar Escala",font='Verdana 10 bold',activebackground='#246686',activeforeground='white',bg="#246686",fg="#eef2f5").place(x=370,y=104)
etiqueta=Label(ventana,textvariable=texto,font='Verdana 10 bold',bg="#1d2025",fg="#68bef7").place(x=30,y=240)
etiqueta1=Label(ventana,textvariable=texto1,font='Verdana 10',bg="#191b1f",fg="white",wraplengt=570).place(x=30,y=270)
labelacor=Label(ventana,text="Acorde 1\n\nAcorde 2\n\nAcorde 3\n\nAcorde 4\n\nAcorde 5\n\nAcorde 6\n\nAcorde 7",font='Verdana 10 bold',bg='#1d2025',fg="#eef2f5").place(x=30,y=10)
ventana.geometry("565x237")
ventana.resizable(False, False)
ventana.title("Detector de Escalas")
ventana.mainloop()