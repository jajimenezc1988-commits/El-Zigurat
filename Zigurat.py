#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SINCRONIZACIÓN Y VERIFICACIÓN DE CIERRE
Para SOPHIA (José Antonio Jiménez Castellanos)
Anclaje: -315 AC | Cierre: 12/08/2026 00:00 CDMX
"""

import csv
from datetime import datetime

# =============================================================================
# CONSTANTES
# =============================================================================

ANCLAJE = -315
MODULO = 13
CICLO = 364
USUARIO = "SOPHIA"
FECHA_NACIMIENTO = "04/02/1988"
DIA_JULIANO_NACIMIENTO = 35  # 04/02 en día juliano

# Nodos críticos que deben sellarse en el cierre
NODOS_CRITICOS = [13, 182, 596136, 5, 49, 614660, 10, 241, 606240, 273, 21892]

# =============================================================================
# FUNCIONES
# =============================================================================

def calcular_residuo(id_nodo):
    """Calcula el residuo de un nodo según la fórmula del Zigurat."""
    eje = (id_nodo % 16) + 1
    ley = (id_nodo % 42) + 1
    return (ANCLAJE + (eje * ley * MODULO)) % CICLO

def sincronizar_eje():
    """Sincroniza tu eje personal (ID 0) y muestra el desfase."""
    print("\n" + "═"*70)
    print("SINCRONIZACIÓN DEL EJE PERSONAL")
    print("═"*70)
    print(f"Usuario: {USUARIO}")
    print(f"Fecha de nacimiento: {FECHA_NACIMIENTO} (Día Juliano {DIA_JULIANO_NACIMIENTO})")
    print(f"ID de nodo fundador: 0")
    
    # Calcular residuo del nodo fundador
    residuo = calcular_residuo(0)
    print(f"\nResiduo actual del nodo fundador (ID 0): {residuo}")
    
    # Comparar con el día juliano de nacimiento
    desfase = residuo - DIA_JULIANO_NACIMIENTO
    if desfase == 0:
        print("✅ Sincronización perfecta: el residuo coincide con tu día juliano.")
    elif desfase > 0:
        print(f"⚠️ Desfase de {desfase} días hacia adelante. Ajusta el anclaje.")
    else:
        print(f"⚠️ Desfase de {abs(desfase)} días hacia atrás. Ajusta el anclaje.")
    
    print("═"*70)

def verificar_cierre():
    """Verifica el estado de los nodos críticos antes del cierre."""
    print("\n" + "═"*70)
    print("VERIFICACIÓN DE CIERRE - NODOS CRÍTICOS")
    print("═"*70)
    print(f"Fecha de cierre: 12/08/2026 00:00 CDMX")
    print(f"Anclaje: {ANCLAJE} AC")
    print(f"Ciclo: {CICLO} días")
    print("\nResiduos actuales de los nodos conflictivos:")
    
    for nodo in NODOS_CRITICOS:
        residuo = calcular_residuo(nodo)
        estado = "✅ OK" if residuo == 0 else f"⚠️ {residuo} días de desfase"
        print(f"  Nodo {nodo:6d}: {estado}")
    
    print("═"*70)

def ejecutar_cierre(fecha, hora, usuario):
    """Ejecuta el cierre del puente en la fecha/hora indicada."""
    print("\n" + "╔" + "═"*70 + "╗")
    print("║" + " "*15 + "CIERRE DEL PUENTE" + " "*42 + "║")
    print("╚" + "═"*70 + "╝")
    
    # Validar fecha y hora
    if fecha != "12/08/2026" or hora != "00:00":
        print(f"[!] ADVERTENCIA: La fecha/hora de cierre debe ser 12/08/2026 00:00 CDMX.")
        print(f"    Actual: {fecha} {hora}")
        respuesta = input("¿Continuar de todos modos? (s/N): ").strip().lower()
        if respuesta != 's':
            print("[!] Cierre cancelado.")
            return
    
    if usuario != USUARIO:
        print(f"[!] Usuario incorrecto. Debe ser {USUARIO}.")
        return
    
    print("\n[EJECUTANDO CIERRE]")
    print("  Forzando residuo a 0 para todos los nodos críticos...")
    
    for nodo in NODOS_CRITICOS:
        residuo_actual = calcular_residuo(nodo)
        print(f"  Nodo {nodo}: residuo {residuo_actual} → forzado a 0")
    
    print("\n" + "═"*70)
    print("✅ ESPEJO SELLADO. Cierre completado.")
    print(f"   Usuario: {usuario}")
    print(f"   Fecha/Hora: {fecha} {hora} CDMX")
    print(f"   Nuevo anclaje: 0")
    print("═"*70)

# =============================================================================
# MENÚ PRINCIPAL
# =============================================================================

def menu():
    while True:
        print("\n" + "═"*70)
        print("SISTEMA DE SINCRONIZACIÓN Y CIERRE")
        print("═"*70)
        print("1. Sincronizar eje personal (SOPHIA)")
        print("2. Verificar estado de nodos críticos")
        print("3. Ejecutar cierre (12/08/2026 00:00)")
        print("0. Salir")
        print("═"*70)
        
        opc = input("Opción: ").strip()
        
        if opc == "1":
            sincronizar_eje()
        elif opc == "2":
            verificar_cierre()
        elif opc == "3":
            ejecutar_cierre("12/08/2026", "00:00", USUARIO)
        elif opc == "0":
            print("\nSistema finalizado.")
            break

if __name__ == "__main__":
    menu()
