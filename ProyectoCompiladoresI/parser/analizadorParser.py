# Generated from analizador.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,150,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,5,0,33,8,0,10,0,12,0,36,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,58,8,2,
        1,3,1,3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,3,3,69,8,3,5,3,71,8,3,10,
        3,12,3,74,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,111,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,128,8,8,10,8,12,8,131,9,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,145,8,9,10,9,
        12,9,148,9,9,1,9,0,1,16,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,18,23,
        162,0,34,1,0,0,0,2,37,1,0,0,0,4,45,1,0,0,0,6,59,1,0,0,0,8,77,1,0,
        0,0,10,89,1,0,0,0,12,93,1,0,0,0,14,97,1,0,0,0,16,110,1,0,0,0,18,
        146,1,0,0,0,20,21,3,10,5,0,21,22,5,6,0,0,22,33,1,0,0,0,23,24,3,14,
        7,0,24,25,5,6,0,0,25,33,1,0,0,0,26,33,3,8,4,0,27,33,3,2,1,0,28,33,
        3,4,2,0,29,30,3,6,3,0,30,31,5,6,0,0,31,33,1,0,0,0,32,20,1,0,0,0,
        32,23,1,0,0,0,32,26,1,0,0,0,32,27,1,0,0,0,32,28,1,0,0,0,32,29,1,
        0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,1,1,0,0,0,36,
        34,1,0,0,0,37,38,5,2,0,0,38,39,5,7,0,0,39,40,3,12,6,0,40,41,5,8,
        0,0,41,42,5,9,0,0,42,43,3,18,9,0,43,44,5,10,0,0,44,3,1,0,0,0,45,
        46,5,3,0,0,46,47,5,7,0,0,47,48,3,12,6,0,48,49,5,8,0,0,49,50,5,9,
        0,0,50,51,3,18,9,0,51,57,5,10,0,0,52,53,5,4,0,0,53,54,5,9,0,0,54,
        55,3,18,9,0,55,56,5,10,0,0,56,58,1,0,0,0,57,52,1,0,0,0,57,58,1,0,
        0,0,58,5,1,0,0,0,59,60,5,5,0,0,60,63,5,7,0,0,61,64,5,26,0,0,62,64,
        3,16,8,0,63,61,1,0,0,0,63,62,1,0,0,0,64,72,1,0,0,0,65,68,5,12,0,
        0,66,69,5,26,0,0,67,69,3,16,8,0,68,66,1,0,0,0,68,67,1,0,0,0,69,71,
        1,0,0,0,70,65,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,75,1,0,0,0,74,72,1,0,0,0,75,76,5,8,0,0,76,7,1,0,0,0,77,78,5,1,
        0,0,78,79,5,7,0,0,79,80,3,10,5,0,80,81,5,6,0,0,81,82,3,12,6,0,82,
        83,5,6,0,0,83,84,3,10,5,0,84,85,5,8,0,0,85,86,5,9,0,0,86,87,3,18,
        9,0,87,88,5,10,0,0,88,9,1,0,0,0,89,90,5,25,0,0,90,91,5,11,0,0,91,
        92,3,16,8,0,92,11,1,0,0,0,93,94,3,16,8,0,94,95,7,0,0,0,95,96,3,16,
        8,0,96,13,1,0,0,0,97,98,5,25,0,0,98,99,5,11,0,0,99,100,3,16,8,0,
        100,101,5,16,0,0,101,102,3,16,8,0,102,15,1,0,0,0,103,104,6,8,-1,
        0,104,105,5,7,0,0,105,106,3,16,8,0,106,107,5,8,0,0,107,111,1,0,0,
        0,108,111,5,25,0,0,109,111,5,24,0,0,110,103,1,0,0,0,110,108,1,0,
        0,0,110,109,1,0,0,0,111,129,1,0,0,0,112,113,10,7,0,0,113,114,5,13,
        0,0,114,128,3,16,8,8,115,116,10,6,0,0,116,117,5,14,0,0,117,128,3,
        16,8,7,118,119,10,5,0,0,119,120,5,15,0,0,120,128,3,16,8,6,121,122,
        10,4,0,0,122,123,5,16,0,0,123,128,3,16,8,5,124,125,10,3,0,0,125,
        126,5,17,0,0,126,128,3,16,8,4,127,112,1,0,0,0,127,115,1,0,0,0,127,
        118,1,0,0,0,127,121,1,0,0,0,127,124,1,0,0,0,128,131,1,0,0,0,129,
        127,1,0,0,0,129,130,1,0,0,0,130,17,1,0,0,0,131,129,1,0,0,0,132,133,
        3,10,5,0,133,134,5,6,0,0,134,145,1,0,0,0,135,136,3,14,7,0,136,137,
        5,6,0,0,137,145,1,0,0,0,138,145,3,8,4,0,139,145,3,2,1,0,140,145,
        3,4,2,0,141,142,3,6,3,0,142,143,5,6,0,0,143,145,1,0,0,0,144,132,
        1,0,0,0,144,135,1,0,0,0,144,138,1,0,0,0,144,139,1,0,0,0,144,140,
        1,0,0,0,144,141,1,0,0,0,145,148,1,0,0,0,146,144,1,0,0,0,146,147,
        1,0,0,0,147,19,1,0,0,0,148,146,1,0,0,0,11,32,34,57,63,68,72,110,
        127,129,144,146
    ]

class analizadorParser ( Parser ):

    grammarFileName = "analizador.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'para'", "'mientras'", "'si'", "'sino'", 
                     "'mostrar'", "';'", "'('", "')'", "'{'", "'}'", "'='", 
                     "','", "'*'", "'/'", "'%'", "'+'", "'-'", "'<'", "'>'", 
                     "'<='", "'>='", "'=='", "'!='" ]

    symbolicNames = [ "<INVALID>", "PARA", "MIENTRAS", "SI", "SINO", "MOSTRAR", 
                      "PYC", "PARI", "PARD", "LLAVEI", "LLAVED", "ASIGNAR", 
                      "COMA", "MULT", "DIV", "MOD", "SUMA", "RESTA", "MENOR", 
                      "MAYOR", "MENORIGUAL", "MAYORIGUAL", "IGUAL", "DIFERENTE", 
                      "NUMERO", "ID", "TEXTO", "ESPACIO", "COMENTARIO" ]

    RULE_programa = 0
    RULE_cicloMientras = 1
    RULE_condicional = 2
    RULE_accion = 3
    RULE_cicloPara = 4
    RULE_asignacion = 5
    RULE_condicion = 6
    RULE_operacion = 7
    RULE_expresion = 8
    RULE_bloque = 9

    ruleNames =  [ "programa", "cicloMientras", "condicional", "accion", 
                   "cicloPara", "asignacion", "condicion", "operacion", 
                   "expresion", "bloque" ]

    EOF = Token.EOF
    PARA=1
    MIENTRAS=2
    SI=3
    SINO=4
    MOSTRAR=5
    PYC=6
    PARI=7
    PARD=8
    LLAVEI=9
    LLAVED=10
    ASIGNAR=11
    COMA=12
    MULT=13
    DIV=14
    MOD=15
    SUMA=16
    RESTA=17
    MENOR=18
    MAYOR=19
    MENORIGUAL=20
    MAYORIGUAL=21
    IGUAL=22
    DIFERENTE=23
    NUMERO=24
    ID=25
    TEXTO=26
    ESPACIO=27
    COMENTARIO=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.AsignacionContext,i)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.PYC)
            else:
                return self.getToken(analizadorParser.PYC, i)

        def operacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.OperacionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.OperacionContext,i)


        def cicloPara(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.CicloParaContext)
            else:
                return self.getTypedRuleContext(analizadorParser.CicloParaContext,i)


        def cicloMientras(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.CicloMientrasContext)
            else:
                return self.getTypedRuleContext(analizadorParser.CicloMientrasContext,i)


        def condicional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.CondicionalContext)
            else:
                return self.getTypedRuleContext(analizadorParser.CondicionalContext,i)


        def accion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.AccionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.AccionContext,i)


        def getRuleIndex(self):
            return analizadorParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = analizadorParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33554478) != 0):
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.asignacion()
                    self.state = 21
                    self.match(analizadorParser.PYC)
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.operacion()
                    self.state = 24
                    self.match(analizadorParser.PYC)
                    pass

                elif la_ == 3:
                    self.state = 26
                    self.cicloPara()
                    pass

                elif la_ == 4:
                    self.state = 27
                    self.cicloMientras()
                    pass

                elif la_ == 5:
                    self.state = 28
                    self.condicional()
                    pass

                elif la_ == 6:
                    self.state = 29
                    self.accion()
                    self.state = 30
                    self.match(analizadorParser.PYC)
                    pass


                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloMientrasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(analizadorParser.MIENTRAS, 0)

        def PARI(self):
            return self.getToken(analizadorParser.PARI, 0)

        def condicion(self):
            return self.getTypedRuleContext(analizadorParser.CondicionContext,0)


        def PARD(self):
            return self.getToken(analizadorParser.PARD, 0)

        def LLAVEI(self):
            return self.getToken(analizadorParser.LLAVEI, 0)

        def bloque(self):
            return self.getTypedRuleContext(analizadorParser.BloqueContext,0)


        def LLAVED(self):
            return self.getToken(analizadorParser.LLAVED, 0)

        def getRuleIndex(self):
            return analizadorParser.RULE_cicloMientras

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloMientras" ):
                return visitor.visitCicloMientras(self)
            else:
                return visitor.visitChildren(self)




    def cicloMientras(self):

        localctx = analizadorParser.CicloMientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cicloMientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(analizadorParser.MIENTRAS)
            self.state = 38
            self.match(analizadorParser.PARI)
            self.state = 39
            self.condicion()
            self.state = 40
            self.match(analizadorParser.PARD)
            self.state = 41
            self.match(analizadorParser.LLAVEI)
            self.state = 42
            self.bloque()
            self.state = 43
            self.match(analizadorParser.LLAVED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(analizadorParser.SI, 0)

        def PARI(self):
            return self.getToken(analizadorParser.PARI, 0)

        def condicion(self):
            return self.getTypedRuleContext(analizadorParser.CondicionContext,0)


        def PARD(self):
            return self.getToken(analizadorParser.PARD, 0)

        def LLAVEI(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.LLAVEI)
            else:
                return self.getToken(analizadorParser.LLAVEI, i)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.BloqueContext)
            else:
                return self.getTypedRuleContext(analizadorParser.BloqueContext,i)


        def LLAVED(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.LLAVED)
            else:
                return self.getToken(analizadorParser.LLAVED, i)

        def SINO(self):
            return self.getToken(analizadorParser.SINO, 0)

        def getRuleIndex(self):
            return analizadorParser.RULE_condicional

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicional" ):
                return visitor.visitCondicional(self)
            else:
                return visitor.visitChildren(self)




    def condicional(self):

        localctx = analizadorParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(analizadorParser.SI)
            self.state = 46
            self.match(analizadorParser.PARI)
            self.state = 47
            self.condicion()
            self.state = 48
            self.match(analizadorParser.PARD)
            self.state = 49
            self.match(analizadorParser.LLAVEI)
            self.state = 50
            self.bloque()
            self.state = 51
            self.match(analizadorParser.LLAVED)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 52
                self.match(analizadorParser.SINO)
                self.state = 53
                self.match(analizadorParser.LLAVEI)
                self.state = 54
                self.bloque()
                self.state = 55
                self.match(analizadorParser.LLAVED)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(analizadorParser.MOSTRAR, 0)

        def PARI(self):
            return self.getToken(analizadorParser.PARI, 0)

        def PARD(self):
            return self.getToken(analizadorParser.PARD, 0)

        def TEXTO(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.TEXTO)
            else:
                return self.getToken(analizadorParser.TEXTO, i)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.COMA)
            else:
                return self.getToken(analizadorParser.COMA, i)

        def getRuleIndex(self):
            return analizadorParser.RULE_accion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccion" ):
                return visitor.visitAccion(self)
            else:
                return visitor.visitChildren(self)




    def accion(self):

        localctx = analizadorParser.AccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_accion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(analizadorParser.MOSTRAR)
            self.state = 60
            self.match(analizadorParser.PARI)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 61
                self.match(analizadorParser.TEXTO)
                pass
            elif token in [7, 24, 25]:
                self.state = 62
                self.expresion(0)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 65
                self.match(analizadorParser.COMA)
                self.state = 68
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [26]:
                    self.state = 66
                    self.match(analizadorParser.TEXTO)
                    pass
                elif token in [7, 24, 25]:
                    self.state = 67
                    self.expresion(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
            self.match(analizadorParser.PARD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(analizadorParser.PARA, 0)

        def PARI(self):
            return self.getToken(analizadorParser.PARI, 0)

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.AsignacionContext,i)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.PYC)
            else:
                return self.getToken(analizadorParser.PYC, i)

        def condicion(self):
            return self.getTypedRuleContext(analizadorParser.CondicionContext,0)


        def PARD(self):
            return self.getToken(analizadorParser.PARD, 0)

        def LLAVEI(self):
            return self.getToken(analizadorParser.LLAVEI, 0)

        def bloque(self):
            return self.getTypedRuleContext(analizadorParser.BloqueContext,0)


        def LLAVED(self):
            return self.getToken(analizadorParser.LLAVED, 0)

        def getRuleIndex(self):
            return analizadorParser.RULE_cicloPara

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicloPara" ):
                return visitor.visitCicloPara(self)
            else:
                return visitor.visitChildren(self)




    def cicloPara(self):

        localctx = analizadorParser.CicloParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cicloPara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(analizadorParser.PARA)
            self.state = 78
            self.match(analizadorParser.PARI)
            self.state = 79
            self.asignacion()
            self.state = 80
            self.match(analizadorParser.PYC)
            self.state = 81
            self.condicion()
            self.state = 82
            self.match(analizadorParser.PYC)
            self.state = 83
            self.asignacion()
            self.state = 84
            self.match(analizadorParser.PARD)
            self.state = 85
            self.match(analizadorParser.LLAVEI)
            self.state = 86
            self.bloque()
            self.state = 87
            self.match(analizadorParser.LLAVED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(analizadorParser.ID, 0)

        def ASIGNAR(self):
            return self.getToken(analizadorParser.ASIGNAR, 0)

        def expresion(self):
            return self.getTypedRuleContext(analizadorParser.ExpresionContext,0)


        def getRuleIndex(self):
            return analizadorParser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = analizadorParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(analizadorParser.ID)
            self.state = 90
            self.match(analizadorParser.ASIGNAR)
            self.state = 91
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.ExpresionContext,i)


        def MENOR(self):
            return self.getToken(analizadorParser.MENOR, 0)

        def MAYOR(self):
            return self.getToken(analizadorParser.MAYOR, 0)

        def MENORIGUAL(self):
            return self.getToken(analizadorParser.MENORIGUAL, 0)

        def MAYORIGUAL(self):
            return self.getToken(analizadorParser.MAYORIGUAL, 0)

        def IGUAL(self):
            return self.getToken(analizadorParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(analizadorParser.DIFERENTE, 0)

        def getRuleIndex(self):
            return analizadorParser.RULE_condicion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = analizadorParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expresion(0)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16515072) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 95
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(analizadorParser.ID, 0)

        def ASIGNAR(self):
            return self.getToken(analizadorParser.ASIGNAR, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.ExpresionContext,i)


        def SUMA(self):
            return self.getToken(analizadorParser.SUMA, 0)

        def getRuleIndex(self):
            return analizadorParser.RULE_operacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacion" ):
                return visitor.visitOperacion(self)
            else:
                return visitor.visitChildren(self)




    def operacion(self):

        localctx = analizadorParser.OperacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(analizadorParser.ID)
            self.state = 98
            self.match(analizadorParser.ASIGNAR)
            self.state = 99
            self.expresion(0)
            self.state = 100
            self.match(analizadorParser.SUMA)
            self.state = 101
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARI(self):
            return self.getToken(analizadorParser.PARI, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.ExpresionContext,i)


        def PARD(self):
            return self.getToken(analizadorParser.PARD, 0)

        def ID(self):
            return self.getToken(analizadorParser.ID, 0)

        def NUMERO(self):
            return self.getToken(analizadorParser.NUMERO, 0)

        def MULT(self):
            return self.getToken(analizadorParser.MULT, 0)

        def DIV(self):
            return self.getToken(analizadorParser.DIV, 0)

        def MOD(self):
            return self.getToken(analizadorParser.MOD, 0)

        def SUMA(self):
            return self.getToken(analizadorParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(analizadorParser.RESTA, 0)

        def getRuleIndex(self):
            return analizadorParser.RULE_expresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = analizadorParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 104
                self.match(analizadorParser.PARI)
                self.state = 105
                self.expresion(0)
                self.state = 106
                self.match(analizadorParser.PARD)
                pass
            elif token in [25]:
                self.state = 108
                self.match(analizadorParser.ID)
                pass
            elif token in [24]:
                self.state = 109
                self.match(analizadorParser.NUMERO)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 127
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = analizadorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 112
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 113
                        self.match(analizadorParser.MULT)
                        self.state = 114
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = analizadorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 115
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 116
                        self.match(analizadorParser.DIV)
                        self.state = 117
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = analizadorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 118
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 119
                        self.match(analizadorParser.MOD)
                        self.state = 120
                        self.expresion(6)
                        pass

                    elif la_ == 4:
                        localctx = analizadorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 121
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 122
                        self.match(analizadorParser.SUMA)
                        self.state = 123
                        self.expresion(5)
                        pass

                    elif la_ == 5:
                        localctx = analizadorParser.ExpresionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 124
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 125
                        self.match(analizadorParser.RESTA)
                        self.state = 126
                        self.expresion(4)
                        pass

             
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.AsignacionContext,i)


        def PYC(self, i:int=None):
            if i is None:
                return self.getTokens(analizadorParser.PYC)
            else:
                return self.getToken(analizadorParser.PYC, i)

        def operacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.OperacionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.OperacionContext,i)


        def cicloPara(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.CicloParaContext)
            else:
                return self.getTypedRuleContext(analizadorParser.CicloParaContext,i)


        def cicloMientras(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.CicloMientrasContext)
            else:
                return self.getTypedRuleContext(analizadorParser.CicloMientrasContext,i)


        def condicional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.CondicionalContext)
            else:
                return self.getTypedRuleContext(analizadorParser.CondicionalContext,i)


        def accion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(analizadorParser.AccionContext)
            else:
                return self.getTypedRuleContext(analizadorParser.AccionContext,i)


        def getRuleIndex(self):
            return analizadorParser.RULE_bloque

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = analizadorParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33554478) != 0):
                self.state = 144
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 132
                    self.asignacion()
                    self.state = 133
                    self.match(analizadorParser.PYC)
                    pass

                elif la_ == 2:
                    self.state = 135
                    self.operacion()
                    self.state = 136
                    self.match(analizadorParser.PYC)
                    pass

                elif la_ == 3:
                    self.state = 138
                    self.cicloPara()
                    pass

                elif la_ == 4:
                    self.state = 139
                    self.cicloMientras()
                    pass

                elif la_ == 5:
                    self.state = 140
                    self.condicional()
                    pass

                elif la_ == 6:
                    self.state = 141
                    self.accion()
                    self.state = 142
                    self.match(analizadorParser.PYC)
                    pass


                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




