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


    # Visit a parse tree produced by analizadorParser#cicloMientras.
    def visitCicloMientras(self, ctx:analizadorParser.CicloMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#condicional.
    def visitCondicional(self, ctx:analizadorParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#accion.
    def visitAccion(self, ctx:analizadorParser.AccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#cicloPara.
    def visitCicloPara(self, ctx:analizadorParser.CicloParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#asignacion.
    def visitAsignacion(self, ctx:analizadorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#condicion.
    def visitCondicion(self, ctx:analizadorParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#operacion.
    def visitOperacion(self, ctx:analizadorParser.OperacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#expresion.
    def visitExpresion(self, ctx:analizadorParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by analizadorParser#bloque.
    def visitBloque(self, ctx:analizadorParser.BloqueContext):
        return self.visitChildren(ctx)



del analizadorParser