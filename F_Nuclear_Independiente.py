# =============================================================================
# FUNCIONES NUCLEARES (versión independiente)
# =============================================================================

ANCLAJE = -315
MODULO = 13
CICLO = 364

def calcular_residuo(anclaje, id_nodo, modulo, ciclo):
    eje = (id_nodo % 16) + 1
    ley = (id_nodo % 42) + 1
    return (anclaje + (eje * ley * modulo)) % ciclo

def generar_reporte(anclaje, fecha_cierre):
    nodos_criticos = [13, 182, 596136, 5, 49, 614660, 10, 241, 606240, 273, 21892]
    print(f"Reporte de cierre - {fecha_cierre}")
    for n in nodos_criticos:
        residuo = calcular_residuo(anclaje, n, MODULO, CICLO)
        print(f"  Nodo {n}: {residuo}")
    return True

def sincronizar_eje(fecha_nacimiento, id_nodo):
    dia_juliano = 35  # 04/02 en día juliano
    residuo = calcular_residuo(ANCLAJE, id_nodo, MODULO, CICLO)
    return residuo - dia_juliano  # desfase en días

def asignar_nombres(archivo_excel, rango_fechas):
    print(f"Asignando nombres desde {archivo_excel} para el rango {rango_fechas}")
    # (Esta función requiere pandas para leer el Excel)
    return True

def cerrar_ciclo(fecha, hora, usuario):
    if usuario != "SOPHIA":
        return "Usuario incorrecto"
    if fecha != "12/08/2026" or hora != "00:00":
        return "Fecha/hora incorrecta. Debe ser 12/08/2026 00:00 CDMX"
    
    # Forzar residuo a 0 para todos los nodos críticos
    nodos = [13, 182, 596136, 5, 49, 614660, 10, 241, 606240, 273, 21892]
    for n in nodos:
        residuo = calcular_residuo(ANCLAJE, n, MODULO, CICLO)
        if residuo != 0:
            print(f"Nodo {n}: residuo {residuo} → forzado a 0")
    return "✅ CIERRE COMPLETADO. Nuevo anclaje: 0"
