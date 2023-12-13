class Calculo:
    def somar(self, x, y):
        resultado = x + y
        return resultado

    def subtrair(self, x, y):
        resultado = x - y
        return resultado

x = 4
y = 5

calculo = Calculo()

soma_resultado = calculo.somar(x, y)
subtracao_resultado = calculo.subtrair(x, y)

print(f"Somando: {x} + {y} = {soma_resultado}")
print(f"Subtraindo: {x} - {y} = {subtracao_resultado}")
