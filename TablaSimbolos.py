# tabla_simbolos.py
class TablaSimbolos:
    def __init__(self):
        self.scopes = [{}]  # Lista de diccionarios por nivel de ámbito

    def abrir_scope(self):
        self.scopes.append({})

    def cerrar_scope(self):
        self.scopes.pop()

    def declarar(self, nombre, tipo, valor=None):
        if nombre in self.scopes[-1]:
            return False  # ya existe en el scope actual
        self.scopes[-1][nombre] = {
            'tipo': tipo,
            'valor': valor,
            'scope': len(self.scopes) - 1
        }
        return True

    def asignar(self, nombre, valor):
        for scope in reversed(self.scopes):
            if nombre in scope:
                scope[nombre]['valor'] = valor
                return True
        return False

    def buscar(self, nombre):
        for scope in reversed(self.scopes):
            if nombre in scope:
                return scope[nombre]
        return None

    def imprimir(self):
        print("🔎 Tabla de Símbolos:")
        for nivel, scope in enumerate(self.scopes):
            print(f"\nÁmbito {nivel}:")
            for nombre, datos in scope.items():
                print(f"  {nombre} → {datos}")
