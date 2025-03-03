# LogicaPredicadosEquipo1

# 🧠 Lógica de Predicados con SymPy

Este proyecto implementa una **evaluación de reglas lógicas** en lógica de predicados utilizando la biblioteca **SymPy** en Python.  
Se define una regla condicional y se verifica su validez en diferentes casos.

## 📌 Descripción

El código analiza la regla lógica:

> **"Si es un mamífero, entonces tiene pelo"**  
> *(P → Q, donde P = "Es un mamífero" y Q = "Tiene pelo")*

Se evalúan distintos casos para comprobar si la regla es válida en todos los escenarios posibles.

## 🚀 Instalación

Para ejecutar el código, necesitas instalar SymPy. Puedes hacerlo con:

```bash
pip install sympy
```

## 📝 Uso

Ejecuta el script con:

```bash
python ejericicio.py
```

## 📊 Funcionamiento

El código realiza los siguientes pasos:

1. **Define los predicados** `P` y `Q` (Mamífero y Pelo).
2. **Crea la regla lógica** `Implies(P, Q)`.
3. **Evalúa la regla** en distintos casos posibles.
4. **Verifica la validez general** de la regla en todos los escenarios.
5. **Detecta contraejemplos** donde la regla podría fallar.

## 📌 Ejemplo de Salida

```plaintext
Regla lógica: P → Q
Evaluación de casos: {'{P: True, Q: True}': True, '{P: True, Q: False}': False, '{P: False, Q: True}': True}
¿La regla es siempre válida? False
¿Siempre que es mamífero, tiene pelo? False
```

## 🛠️ Solución de Problemas

Si tienes errores de importación con SymPy, prueba reinstalarlo:

```bash
pip uninstall sympy -y
pip install sympy
```

Si el error persiste, verifica que estás usando la versión correcta de Python (`>=3.8`).

## 🏗️ Contribuciones

Si deseas mejorar el código o agregar nuevas funcionalidades, ¡las contribuciones son bienvenidas!  
Abre un **issue** o un **pull request** en este repositorio.

## 📜 Licencia

Este proyecto se distribuye bajo la licencia **MIT**.

---
💡 *Creado con SymPy y Python para explorar la lógica de predicados.*
```


