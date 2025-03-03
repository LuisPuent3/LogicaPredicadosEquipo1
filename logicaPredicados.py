from sympy import symbols
from sympy.logic.boolalg import Implies, And, Not
from sympy.logic.inference import satisfiable  # Corrección del import

# 📌 Definir predicados (variables lógicas)
P, Q = symbols('P Q')  # P = "Es un mamífero", Q = "Tiene pelo"

# 📌 Regla lógica: "Si es un mamífero, entonces tiene pelo" → (P → Q)
regla = Implies(P, Q)

# 📌 Evaluar la regla en diferentes casos
casos = [{P: True, Q: True}, {P: True, Q: False}, {P: False, Q: True}]
resultados = [regla.subs(caso) for caso in casos]

# 📌 Comprobar validez en todos los posibles valores de P y Q
valida = all(regla.subs({P: p, Q: q}) for p in [True, False] for q in [True, False])

# 📌 Verificar si existe un caso donde P sea verdadero y Q falso (esto invalidaría la regla)
es_confiable = not satisfiable(And(P, Not(Q)))

# 📌 Imprimir resultados
print("Regla lógica:", regla)
print("Evaluación de casos:", dict(zip(map(str, casos), resultados)))
print("¿La regla es siempre válida?", valida)
print("¿Siempre que es mamífero, tiene pelo?", es_confiable)
