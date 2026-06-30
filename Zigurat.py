#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZIGURAT - SISTEMA UNIFICADO DE PATRONES PUROS
Versión: 1.1 (con generador CSV desde INEGI)
Usuario: SOPHIA (José Antonio Jiménez Castellanos)
Fecha de nacimiento: 04/02/1988
Anclaje: -315 AC
Cierre: 12/08/2026 00:00 CDMX
"""

import json
import math
import os
import sys
import csv
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Intentar importar pandas (necesario para el build)
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    pd = None

# =============================================================================
# CONSTANTES GLOBALES
# =============================================================================

ANCLAJE = -315
MODULO = 13
CICLO = 364
FECHA_CIERRE = datetime(2026, 8, 12, 0, 0, 0)
TOTAL_EJES = 16
TOTAL_LEYES = 42
TOTAL_PUNTOS = 672
USUARIO = "SOPHIA"
NOMBRE_COMPLETO = "José Antonio Jiménez Castellanos"
FECHA_NACIMIENTO = datetime(1988, 2, 4, 0, 0, 0)

# =============================================================================
# (Todas las clases anteriores: MatrizDoceMasUno, EjesVerticales, LeyesHorizontales,
#  MatrizCompleta, AnaBkoach, GenesisAnaBkoach, BibliotecaEsoterica,
#  MotorInterpretacion, CargadorDatos, SistemaZigurat)
# ... SE MANTIENEN IGUAL QUE EN LA VERSIÓN ANTERIOR ...
# =============================================================================

# =============================================================================
# NUEVA FUNCIÓN: GENERAR CSV DESDE INEGI
# =============================================================================

class SistemaZigurat:
    # ... (todo el __init__ y comandos anteriores se mantienen) ...

    def cmd_build(self):
        """Genera el archivo adam_con_inegi_agregado.csv desde los datos originales."""
        print("\n[BUILD] Generando CSV maestro desde INEGI...")
        print("═"*70)
        
        if not PANDAS_AVAILABLE:
            print("[!] Error: pandas no instalado. Ejecuta: pip install pandas openpyxl")
            return
        
        # 1. Cargar INEGI
        try:
            df_inegi = pd.read_excel('cpv2020_b_eum_01_poblacion.xlsx', sheet_name='04', skiprows=5)
            df_inegi.columns = ['Entidad', 'Poblacion_Total', 'Hombres', 'Mujeres', 
                                'Edad_Mediana_Total', 'Edad_Mediana_H', 'Edad_Mediana_M',
                                'Relacion_H_M', 'Indice_Envejecimiento_Total', 'Indice_Envejecimiento_H',
                                'Indice_Envejecimiento_M', 'Razon_Dependencia_Total', 
                                'Razon_Dependencia_Infantil', 'Razon_Dependencia_Vejez']
            df_inegi = df_inegi.dropna(subset=['Entidad'])
            df_inegi = df_inegi[df_inegi['Entidad'] != 'Entidad federativa']
            df_inegi.reset_index(drop=True, inplace=True)
            print("  ✓ INEGI cargado")
        except Exception as e:
            print(f"  ✗ Error al cargar INEGI: {e}")
            return
        
        # 2. Mapa de entidades
        mapa_ejes = {
            'Eje_Norte_Guadalajara': 'Jalisco',
            'Eje_Este_Potosi': 'San Luis Potosí',
            'Eje_Oeste_Concepcion': 'Colima',
            'Eje_Sur_Bariloche': 'Chiapas',
            'Centro_Arbol': 'Ciudad de México',
            'Ajustes_Residuo': 'Oaxaca'
        }
        
        # 3. Leer adam_con_coordenadas.csv (o adam_completo.csv)
        try:
            with open('adam_con_coordenadas.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                personas = list(reader)
            print(f"  ✓ Coordenadas cargadas ({len(personas)} registros)")
        except FileNotFoundError:
            try:
                with open('adam_completo.csv', 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    personas = list(reader)
                print(f"  ✓ adam_completo.csv cargado ({len(personas)} registros)")
            except FileNotFoundError:
                print("  ✗ No se encuentra adam_con_coordenadas.csv ni adam_completo.csv")
                return
        
        # 4. Asignar entidades y datos
        for row in personas:
            grupo = row.get('Grupo', 'Centro_Arbol')
            entidad = mapa_ejes.get(grupo, 'No especificada')
            row['Entidad_Censal'] = entidad
            
            fila_entidad = df_inegi[df_inegi['Entidad'] == entidad]
            if not fila_entidad.empty:
                for col in df_inegi.columns:
                    if col != 'Entidad':
                        row[col] = fila_entidad.iloc[0][col]
            else:
                promedio = df_inegi.mean(numeric_only=True)
                for col in promedio.index:
                    row[col] = promedio[col]
        
        # 5. Guardar CSV
        fieldnames = ['ID', 'Grupo', 'Año', 'Dia_Juliano', 'Fecha_Nacimiento', 
                      'Nombre_Arquetipo', 'Latitud', 'Longitud', 'Entidad_Censal',
                      'Poblacion_Total', 'Hombres', 'Mujeres', 'Edad_Mediana_Total',
                      'Relacion_H_M', 'Indice_Envejecimiento_Total', 'Razon_Dependencia_Total']
        with open('adam_con_inegi_agregado.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(personas)
        
        print(f"  ✅ adam_con_inegi_agregado.csv generado con {len(personas)} registros.")
        print("═"*70)

# =============================================================================
# ACTUALIZACIÓN DEL main() PARA INCLUIR EL COMANDO 'build'
# =============================================================================

def main():
    if len(sys.argv) > 1:
        sistema = SistemaZigurat()
        comando = sys.argv[1]
        
        if comando == "build":
            sistema.cmd_build()
        elif comando == "report":
            fecha = sys.argv[2] if len(sys.argv) > 2 else None
            sistema.cmd_report(fecha)
        elif comando == "sync":
            fecha = sys.argv[2] if len(sys.argv) > 2 else "04/02/1988"
            id_nodo = int(sys.argv[3]) if len(sys.argv) > 3 else 0
            sistema.cmd_sync(fecha, id_nodo)
        elif comando == "assign":
            archivo = sys.argv[2] if len(sys.argv) > 2 else None
            inicio = int(sys.argv[3]) if len(sys.argv) > 3 else None
            fin = sys.argv[4] if len(sys.argv) > 4 else None
            sistema.cmd_assign(archivo, inicio, fin)
        elif comando == "interpret":
            codigo = sys.argv[2] if len(sys.argv) > 2 else "P6-L2-156"
            sistema.cmd_interpret(codigo)
        elif comando == "matrix12":
            sistema.cmd_matrix12()
        elif comando == "matrix16x42":
            sistema.cmd_matrix16x42()
        elif comando == "kml":
            sistema.cmd_kml()
        elif comando == "close":
            fecha = sys.argv[2] if len(sys.argv) > 2 else "12/08/2026"
            hora = sys.argv[3] if len(sys.argv) > 3 else "00:00"
            usuario = sys.argv[4] if len(sys.argv) > 4 else USUARIO
            sistema.cmd_close(fecha, hora, usuario)
        else:
            print(f"Comando '{comando}' no reconocido.")
            print("Comandos disponibles: build, report, sync, assign, interpret, matrix12, matrix16x42, kml, close")
    else:
        sistema = SistemaZigurat()
        sistema.menu()

if __name__ == "__main__":
    main()
