# Generated from analizador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .analizadorParser import analizadorParser
else:
    from analizadorParser import analizadorParser

# This class defines a complete generic visitor for a parse tree produced by analizadorParser.

class analizadorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by analizadorParser#programa.
    def visitPrograma(self, ctx:analizadorParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#instruccion.
    def visitInstruccion(self, ctx:analizadorParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#declaracion.
    def visitDeclaracion(self, ctx:analizadorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#tipo.
    def visitTipo(self, ctx:analizadorParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#asignacion.
    def visitAsignacion(self, ctx:analizadorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#suma.
    def visitSuma(self, ctx:analizadorParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#accion.
    def visitAccion(self, ctx:analizadorParser.AccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#returnStmt.
    def visitReturnStmt(self, ctx:analizadorParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#funcionDecl.
    def visitFuncionDecl(self, ctx:analizadorParser.FuncionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#parametros.
    def visitParametros(self, ctx:analizadorParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#parametro.
    def visitParametro(self, ctx:analizadorParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:analizadorParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#argumentos.
    def visitArgumentos(self, ctx:analizadorParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#forLoop.
    def visitForLoop(self, ctx:analizadorParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#whileLoop.
    def visitWhileLoop(self, ctx:analizadorParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#ifElse.
    def visitIfElse(self, ctx:analizadorParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#bloque.
    def visitBloque(self, ctx:analizadorParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#expresion.
    def visitExpresion(self, ctx:analizadorParser.ExpresionContext):
        return self.visitChildren(ctx)



del analizadorParser