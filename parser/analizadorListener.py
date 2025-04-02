# Generated from analizador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .analizadorParser import analizadorParser
else:
    from analizadorParser import analizadorParser

# This class defines a complete listener for a parse tree produced by analizadorParser.
class analizadorListener(ParseTreeListener):

    # Enter a parse tree produced by analizadorParser#programa.
    def enterPrograma(self, ctx:analizadorParser.ProgramaContext):
        pass

    # Exit a parse tree produced by analizadorParser#programa.
    def exitPrograma(self, ctx:analizadorParser.ProgramaContext):
        pass


    # Enter a parse tree produced by analizadorParser#instruccion.
    def enterInstruccion(self, ctx:analizadorParser.InstruccionContext):
        pass

    # Exit a parse tree produced by analizadorParser#instruccion.
    def exitInstruccion(self, ctx:analizadorParser.InstruccionContext):
        pass


    # Enter a parse tree produced by analizadorParser#declaracion.
    def enterDeclaracion(self, ctx:analizadorParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by analizadorParser#declaracion.
    def exitDeclaracion(self, ctx:analizadorParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by analizadorParser#tipo.
    def enterTipo(self, ctx:analizadorParser.TipoContext):
        pass

    # Exit a parse tree produced by analizadorParser#tipo.
    def exitTipo(self, ctx:analizadorParser.TipoContext):
        pass


    # Enter a parse tree produced by analizadorParser#asignacion.
    def enterAsignacion(self, ctx:analizadorParser.AsignacionContext):
        pass

    # Exit a parse tree produced by analizadorParser#asignacion.
    def exitAsignacion(self, ctx:analizadorParser.AsignacionContext):
        pass


    # Enter a parse tree produced by analizadorParser#suma.
    def enterSuma(self, ctx:analizadorParser.SumaContext):
        pass

    # Exit a parse tree produced by analizadorParser#suma.
    def exitSuma(self, ctx:analizadorParser.SumaContext):
        pass


    # Enter a parse tree produced by analizadorParser#accion.
    def enterAccion(self, ctx:analizadorParser.AccionContext):
        pass

    # Exit a parse tree produced by analizadorParser#accion.
    def exitAccion(self, ctx:analizadorParser.AccionContext):
        pass


    # Enter a parse tree produced by analizadorParser#returnStmt.
    def enterReturnStmt(self, ctx:analizadorParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by analizadorParser#returnStmt.
    def exitReturnStmt(self, ctx:analizadorParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by analizadorParser#funcionDecl.
    def enterFuncionDecl(self, ctx:analizadorParser.FuncionDeclContext):
        pass

    # Exit a parse tree produced by analizadorParser#funcionDecl.
    def exitFuncionDecl(self, ctx:analizadorParser.FuncionDeclContext):
        pass


    # Enter a parse tree produced by analizadorParser#parametros.
    def enterParametros(self, ctx:analizadorParser.ParametrosContext):
        pass

    # Exit a parse tree produced by analizadorParser#parametros.
    def exitParametros(self, ctx:analizadorParser.ParametrosContext):
        pass


    # Enter a parse tree produced by analizadorParser#parametro.
    def enterParametro(self, ctx:analizadorParser.ParametroContext):
        pass

    # Exit a parse tree produced by analizadorParser#parametro.
    def exitParametro(self, ctx:analizadorParser.ParametroContext):
        pass


    # Enter a parse tree produced by analizadorParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:analizadorParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by analizadorParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:analizadorParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by analizadorParser#argumentos.
    def enterArgumentos(self, ctx:analizadorParser.ArgumentosContext):
        pass

    # Exit a parse tree produced by analizadorParser#argumentos.
    def exitArgumentos(self, ctx:analizadorParser.ArgumentosContext):
        pass


    # Enter a parse tree produced by analizadorParser#forLoop.
    def enterForLoop(self, ctx:analizadorParser.ForLoopContext):
        pass

    # Exit a parse tree produced by analizadorParser#forLoop.
    def exitForLoop(self, ctx:analizadorParser.ForLoopContext):
        pass


    # Enter a parse tree produced by analizadorParser#whileLoop.
    def enterWhileLoop(self, ctx:analizadorParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by analizadorParser#whileLoop.
    def exitWhileLoop(self, ctx:analizadorParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by analizadorParser#ifElse.
    def enterIfElse(self, ctx:analizadorParser.IfElseContext):
        pass

    # Exit a parse tree produced by analizadorParser#ifElse.
    def exitIfElse(self, ctx:analizadorParser.IfElseContext):
        pass


    # Enter a parse tree produced by analizadorParser#bloque.
    def enterBloque(self, ctx:analizadorParser.BloqueContext):
        pass

    # Exit a parse tree produced by analizadorParser#bloque.
    def exitBloque(self, ctx:analizadorParser.BloqueContext):
        pass


    # Enter a parse tree produced by analizadorParser#expresion.
    def enterExpresion(self, ctx:analizadorParser.ExpresionContext):
        pass

    # Exit a parse tree produced by analizadorParser#expresion.
    def exitExpresion(self, ctx:analizadorParser.ExpresionContext):
        pass



del analizadorParser