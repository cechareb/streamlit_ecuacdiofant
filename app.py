import streamlit as st
import random

# Función para calcular el máximo común divisor extendido
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
n    y = x1 - (a // b) * y1
    return gcd, x, y

# Función para resolver ax + by = c
def solve_diophantine(a, b, c):
    gcd, x0, y0 = extended_gcd(a, b)
    if c % gcd != 0:
        return None  # No hay solución
    factor = c // gcd
    x0 *= factor
    y0 *= factor
    # Solución general: x = x0 + (b/gcd)*t, y = y0 - (a/gcd)*t
    return x0, y0, b // gcd, a // gcd

st.title("Resolución de Ecuaciones Diofánticas (ax + by = c)")

# Inicializar valores en session_state
if 'a' not in st.session_state:
    st.session_state.a = 0
if 'b' not in st.session_state:
    st.session_state.b = 0
if 'c' not in st.session_state:
    st.session_state.c = 0

# Botón para generar datos de prueba
def generar_datos():
    st.session_state.a = random.randint(1, 20)
    st.session_state.b = random.randint(1, 20)
    # Generar c como múltiplo del gcd para asegurar soluciones
    gcd_val, _, _ = extended_gcd(st.session_state.a, st.session_state.b)
    st.session_state.c = random.randint(1, 20) * gcd_val

st.button("Generar datos de prueba", on_click=generar_datos)

# Campos de entrada para a, b y c
a = st.number_input("Coeficiente a", value=st.session_state.a, step=1)
b = st.number_input("Coeficiente b", value=st.session_state.b, step=1)
c = st.number_input("Término independiente c", value=st.session_state.c, step=1)

# Resolver la ecuación
def resolver():
    result = solve_diophantine(a, b, c)
    if result is None:
        st.error("No existe solución entera para la ecuación dado que c no es múltiplo de gcd(a, b).")
    else:
        x0, y0, t_coeff_x, t_coeff_y = result
        st.success(f"Solución particular: x = {x0}, y = {y0}")
        st.info(
            f"Solución general: x = {x0} + ({t_coeff_x})·t, y = {y0} - ({t_coeff_y})·t, con t ∈ ℤ"
        )

st.button("Resolver ecuación diofántica", on_click=resolver)
