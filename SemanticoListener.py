from parser.analizadorListener import analizadorListener

class SemanticoListener(analizadorListener):
    def __init__(self):
        self.scopes = [{}]  
        self.funciones = {} 
        self.errors = []
        self.funcionActual = None
        self.tipoFuncionActual = None
        self.tieneReturn = False

    def enterDeclaracion(self, ctx):
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()

        if nombre in self.scopes[-1]:
            self.errors.append(f"❌ Error: La variable '{nombre}' ya fue declarada en este bloque.")
        else:
            self.scopes[-1][nombre] = tipo

    def enterAsignacion(self, ctx):
        nombre = ctx.ID().getText()
        if not self._existe_variable(nombre):
            self.errors.append(f"❌ Error: Variable '{nombre}' no ha sido declarada antes de asignar.")

    def enterFuncionDecl(self, ctx):
        nombre = ctx.ID().getText()
        tipo = ctx.tipo().getText()

        if nombre in self.funciones:
            self.errors.append(f"❌ Error: Función '{nombre}' ya fue declarada.")
            return

        parametros = []
        nombres_param = set()

        if ctx.parametros():
            for p in ctx.parametros().parametro():
                tipo_param = p.tipo().getText()
                id_param = p.ID().getText()

                if id_param in nombres_param:
                    self.errors.append(f"❌ Error: Parámetro duplicado '{id_param}' en función '{nombre}'.")
                else:
                    nombres_param.add(id_param)
                    parametros.append((tipo_param, id_param))

        self.funciones[nombre] = {
            'tipo': tipo,
            'params': parametros
        }

        # Guardamos el tipo de la función actual para validaciones de return
        self.funcionActual = nombre
        self.tipoFuncionActual = tipo
        self.tieneReturn = False

    def exitFuncionDecl(self, ctx):
        # Verifica si faltó return en funciones no-void
        if self.tipoFuncionActual != "void" and not self.tieneReturn:
            self.errors.append(f"❌ Error: La función '{self.funcionActual}' no tiene sentencia return.")
        self.funcionActual = None
        self.tipoFuncionActual = None

    def enterReturnStmt(self, ctx):
        self.tieneReturn = True
        

    def enterLlamadaFuncion(self, ctx):
        nombre = ctx.ID().getText()
        if nombre not in self.funciones:
            self.errors.append(f"❌ Error: Llamada a función '{nombre}' no declarada.")
        else:
            esperados = len(self.funciones[nombre]['params'])
            dados = len(ctx.argumentos().expresion()) if ctx.argumentos() else 0
            if esperados != dados:
                self.errors.append(f"❌ Error: Función '{nombre}' esperaba {esperados} argumentos, pero se dieron {dados}.")

    def enterBloque(self, ctx):
        self.scopes.append({})

    def exitBloque(self, ctx):
        self.scopes.pop()

    def _existe_variable(self, nombre):
        for scope in reversed(self.scopes):
            if nombre in scope:
                return True
        return False

    @property
    def hayErrores(self):
        return len(self.errors) > 0

    def mostrarErrores(self):
        for error in self.errors:
            print(error)
