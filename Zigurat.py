#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZIGURAT - SISTEMA UNIFICADO DE PATRONES PUROS
Versión: 2.0 (Unificada Final)
Incluye: Todo lo original + Vector Normal + Vector VRIL + Interpretación de Eventos
"""

import json
import os
import sys
import csv
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

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
TOTAL_EJES = 16
TOTAL_LEYES = 42
TOTAL_PUNTOS = 672
USUARIO = "SOPHIA"
NOMBRE_COMPLETO = "José Antonio Jiménez Castellanos"
FECHA_NACIMIENTO = datetime(1988, 2, 4)

# =============================================================================
# CLASES ORIGINALES (COMPLETAS)
# =============================================================================

class MatrizDoceMasUno:
    def __init__(self):
        self.partes = self._inicializar_partes()
        self.lengua = self._inicializar_lengua()

    def _inicializar_partes(self):
        partes = []
        for i in range(1, 13):
            parte = {
                "numero": i,
                "nombre": f"Parte_{i}",
                "angulo": i * 30,
                "multiplo_13": (i * 13) % 360,
                "es_primo": self._es_primo(i),
                "codigo": f"SIGMA-{i}-{sum(d for d in range(1, i) if i % d == 0)}",
                "manifestaciones": [
                    {"lugar": l, "coord": (i * l * 13) % 360,
                     "codigo": f"P{i}-L{l}-{(i*l*13)%360}"}
                    for l in range(1, 5)
                ]
            }
            partes.append(parte)
        return partes

    def _inicializar_lengua(self):
        return {
            "numero": 13,
            "nombre": "La_Lengua",
            "suma_partes": sum(range(1, 14)),
            "funcion": "Conector de las 12 partes",
            "codigo": "SIGMA-13-12"
        }

    def _es_primo(self, n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True

    def exportar(self):
        return {
            "estructura": "12_Partes_+_1_Lengua",
            "total_fragmentos": 13,
            "partes": self.partes,
            "lengua": self.lengua
        }

    def mostrar(self):
        print("\n" + "═"*70)
        print("MATRIZ 12 + 1 (Las 12 Partes + La Lengua)")
        print("═"*70)
        for p in self.partes:
            print(f"\n[Parte {p['numero']}] {p['nombre']}")
            print(f"  Ángulo: {p['angulo']}° | Múltiplo 13: {p['multiplo_13']}")
            print(f"  Código: {p['codigo']}")
        print(f"\n[Lengua] {self.lengua['nombre']}")
        print(f"  Suma partes: {self.lengua['suma_partes']} (7×13)")


class EjesVerticales:
    def __init__(self):
        nombres = [
            ("Sustancias_Quimicas", "SQ"), ("Aduana_Comercio_Exterior", "ACE"),
            ("Maquinaria_Pesada", "MP"), ("Genetica", "GEN"),
            ("INEGI_Censos", "INEGI"), ("Auditoria", "AUD"),
            ("Meteorologia", "MET"), ("Administracion_Publica", "AP"),
            ("Psicologia_Social", "PS"), ("Logistica", "LOG"),
            ("Medicina", "MED"), ("Astronomia", "AST"),
            ("Termodinamica", "TER"), ("Historiografia", "HIST"),
            ("Antropologia", "ANT"), ("Telecomunicaciones", "TEL")
        ]
        self.ejes = [{"numero": i+1, "nombre": n, "codigo": c, "frecuencia": 364/(i+1)}
                     for i, (n, c) in enumerate(nombres)]


class LeyesHorizontales:
    def __init__(self):
        self.leyes = self._inicializar_leyes()

    def _inicializar_leyes(self):
        leyes = []
        yhvh_nombres = [
            "Yod_Keter", "Yod_Chokmah", "Yod_Binah", "Yod_Chesed",
            "Yod_Gevurah", "Yod_Tiferet", "Yod_Netzach", "Yod_Hod",
            "Yod_Yesod", "Yod_Malkuth", "He1_Daat", "He1_Corona",
            "He1_Ciclo", "He1_Emocion", "He1_Propulsion", "Vav_Sello",
            "Vav_Equilibrio", "Vav_Vida", "Vav_Despertar", "Vav_Coronacion",
            "Vav_Ser", "He2_Corazon", "He2_Reflejo", "He2_Complecion",
            "He2_Eternidad", "He2_Nombre"
        ]
        for i, nombre in enumerate(yhvh_nombres, 1):
            leyes.append({"numero": i, "nombre": nombre, "tipo": "YHVH", "valor": i})

        sello_nombres = [
            "Tiferet_Verdad", "Tiferet_Justicia", "Tiferet_Misericordia",
            "Tiferet_Humildad", "Tiferet_Fe", "Tiferet_Sacrificio",
            "Malkuth_Liderazgo", "Malkuth_Estrategia", "Malkuth_Dominio",
            "Malkuth_Paciencia", "Malkuth_Fortaleza", "Malkuth_Practica",
            "Malkuth_Integridad", "Malkuth_Grandeza", "Malkuth_Majestad",
            "Malkuth_Soberania"
        ]
        for i, nombre in enumerate(sello_nombres, 27):
            leyes.append({"numero": i, "nombre": nombre, "tipo": "Sello_Rey", "valor": (i-26)*6})

        return leyes

    def get_ley(self, num):
        if 1 <= num <= 42:
            return self.leyes[num-1]
        return None


class MatrizCompleta:
    def __init__(self):
        self.ejes = EjesVerticales()
        self.leyes = LeyesHorizontales()
        self.doce_mas_uno = MatrizDoceMasUno()
        self.puntos = self._calcular_todos_puntos()

    def _calcular_punto(self, eje_num, ley_num):
        eje = self.ejes.ejes[eje_num-1]
        ley = self.leyes.get_ley(ley_num)
        if not ley: return {}
        valor = (eje_num * ley["valor"] * MODULO) % CICLO
        angulo = (valor / CICLO) * 360
        return {
            "coordenada": {
                "eje": eje_num,
                "ley": ley_num,
                "codigo": f"{eje['codigo']}-L{ley_num:02d}-{valor:03d}"
            },
            "eje_data": eje,
            "ley_data": ley,
            "valor_cruzado": valor,
            "angulo": round(angulo, 2),
            "intensidad": round((eje_num * ley["valor"]) / 42, 4),
            "resonancia_315": (valor * abs(ANCLAJE)) % 1000
        }

    def _calcular_todos_puntos(self):
        puntos = []
        for e in range(1, 17):
            for l in range(1, 43):
                puntos.append(self._calcular_punto(e, l))
        return puntos


class AnaBkoach:
    LINEAS = {
        1: {"nombre": "Elevación del mundo material", "letras": "אבגיתצ",
            "significado": "Abre los cielos, eleva la materia",
            "leyes": [1,2,3,4,5,6], "sefirah": "Chesed"},
        2: {"nombre": "Rectificación del corazón", "letras": "קרעשטן",
            "significado": "Circuncida el corazón, purifica las emociones",
            "leyes": [7,8,9,10,11,12], "sefirah": "Gevurah"},
        3: {"nombre": "Apertura de los canales", "letras": "נגדיכש",
            "significado": "Abre los conductos, fluye la energía divina",
            "leyes": [13,14,15,16,17,18], "sefirah": "Tiferet"},
        4: {"nombre": "Liberación de las ataduras", "letras": "בטרצתג",
            "significado": "Rompe las cadenas, libera las almas",
            "leyes": [19,20,21,22,23,24], "sefirah": "Netzach"},
        5: {"nombre": "Protección y guarda", "letras": "חקבטנע",
            "significado": "Protege, guarda, defiende de los daños",
            "leyes": [25,26,27,28,29,30], "sefirah": "Hod"},
        6: {"nombre": "Sanación y empleo", "letras": "יגלפזק",
            "significado": "Sana las enfermedades, emplea las fuerzas",
            "leyes": [31,32,33,34,35,36], "sefirah": "Yesod"},
        7: {"nombre": "Manifestación y soberanía", "letras": "שקוצית",
            "significado": "Desciende la shejiná, manifiesta el reino",
            "leyes": [37,38,39,40,41,42], "sefirah": "Malkuth"}
    }


class GenesisAnaBkoach:
    DIAS_CREACION = {
        1: {"accion": "Luz de la dualidad", "leyes": range(1,7)},
        2: {"accion": "Firmamento entre aguas", "leyes": range(7,13)},
        3: {"accion": "Tierra seca y vegetación", "leyes": range(13,19)},
        4: {"accion": "Luminarias para los tiempos", "leyes": range(19,25)},
        5: {"accion": "Seres vivientes en el agua y aves", "leyes": range(25,31)},
        6: {"accion": "Animales terrestres y humano", "leyes": range(31,37)},
        7: {"accion": "Shabbat, santificación", "leyes": range(37,43)}
    }


class BibliotecaEsoterica:
    SIGNIFICADOS_NUMEROS = {
        1: "Unidad, origen.", 2: "Dualidad.", 3: "Trinidad.", 4: "Cuadrado elemental.",
        5: "Quintaesencia.", 6: "Centro, equilibrio.", 7: "Ciclo completo.",
        12: "Plenitud de partes.", 13: "La Lengua, transformación.",
        26: "YHVH completo.", 42: "Nombre de 42 letras.", 91: "Suma de 1 a 13.",
        315: "Año de la caída.", 364: "Año de equilibrio."
    }

    EJES_SIGNIFICADO = {
        1: "Sustancias Químicas", 2: "Aduana", 3: "Maquinaria Pesada",
        4: "Genética", 5: "INEGI/Censos", 6: "Auditoría",
        7: "Meteorología", 8: "Administración Pública", 9: "Psicología Social",
        10: "Logística", 11: "Medicina", 12: "Astronomía",
        13: "Termodinámica", 14: "Historiografía", 15: "Antropología",
        16: "Telecomunicaciones"
    }

    INTERPRETACIONES_ESPECIALES = {
        (6, 6): "EL JUICIO DEL CENTRO.",
        (13, 26): "EL FIN DEL CALOR.",
        (1, 1): "EL ORIGEN.",
        (16, 26): "LA RED DEL NOMBRE."
    }


class MotorInterpretacion:
    def __init__(self):
        self.biblio = BibliotecaEsoterica()

    def interpretar_numero(self, n):
        return self.biblio.SIGNIFICADOS_NUMEROS.get(n, f"{n}: sin entrada")


# =============================================================================
# VECTOR NORMAL + VECTOR VRIL
# =============================================================================
def generar_vector_normal():
    vector = {}
    for eje in range(1, 17):
        for ley in range(1, 43):
            vector[(eje, ley)] = f"Eje {eje} × Ley {ley}"
    vector[(13,26)] = "EL FIN DEL CALOR - Entropía máxima"
    vector[(6,6)] = "EL JUICIO DEL CENTRO"
    vector[(1,1)] = "EL ORIGEN"
    vector[(16,26)] = "LA RED DEL NOMBRE"
    return vector


def generar_vector_vril():
    vril = {}
    for eje in range(1, 17):
        for ley in range(1, 43):
            vril[(eje, ley)] = f"VRIL::{eje}-{ley}"
    vril[(13,26)] = "VRIL:: Entropía intentando dividir el linaje solar"
    vril[(9,42)] = "VRIL:: Mente colectiva activada por fuerza de manifestación"
    return vril


VECTOR_NORMAL = generar_vector_normal()
VECTOR_VRIL = generar_vector_vril()


def calcular_vector(id_nodo: int):
    if id_nodo == 0:
        return 1, 1, 62
    eje = ((id_nodo - 1) % 16) + 1
    ley = ((id_nodo - 1) % 42) + 1
    residuo = (ANCLAJE + (eje * ley * MODULO)) % CICLO
    return eje, ley, residuo


def interpretar_evento(eje: int, ley: int, usar_vril: bool = False):
    if usar_vril:
        return VECTOR_VRIL.get((eje, ley), "VRIL sin registro")
    return VECTOR_NORMAL.get((eje, ley), "Sin interpretación")


# =============================================================================
# SISTEMA PRINCIPAL (CON TODOS LOS COMANDOS ORIGINALES)
# =============================================================================
class SistemaZigurat:
    def __init__(self):
        print("╔" + "═"*70 + "╗")
        print("║" + " "*20 + "ZIGURAT - SISTEMA UNIFICADO v2.0" + " "*25 + "║")
        print("║" + " "*15 + f"Usuario: {USUARIO} ({NOMBRE_COMPLETO})" + " "*21 + "║")
        print("║" + " "*15 + f"Anclaje: {ANCLAJE} AC | Cierre: 12/08/2026" + " "*18 + "║")
        print("╚" + "═"*70 + "╝")

        self.matriz_completa = MatrizCompleta()
        self.matriz_12 = MatrizDoceMasUno()
        self.ana_bkoach = AnaBkoach()
        self.genesis = GenesisAnaBkoach()
        self.interprete = MotorInterpretacion()
        self.datos = self._cargar_datos()

        print(f"\n[✓] Sistema cargado: {len(self.datos)} nodos")

    def _cargar_datos(self):
        archivo = "adam_con_inegi_agregado.csv"
        if os.path.exists(archivo) and PANDAS_AVAILABLE:
            try:
                df = pd.read_csv(archivo)
                return df.to_dict('records')
            except:
                pass
        return [{"ID": 0, "Grupo": "Centro_Arbol"}]

    # COMANDOS ORIGINALES
    def cmd_report(self):
        print("\n[REPORTE VECTORIAL]")
        for nodo in self.datos:
            id_nodo = int(nodo["ID"])
            eje, ley, residuo = calcular_vector(id_nodo)
            normal = VECTOR_NORMAL.get((eje, ley), "Sin interpretación")
            print(f"ID {id_nodo:3d}: Eje {eje} × Ley {ley} → {normal}")

    def cmd_interpret(self, codigo):
        print(self.interprete.interpretar_codigo(codigo))

    def interpretar_evento(self, descripcion: str, eje: int, ley: int, usar_vril=False):
        interp = interpretar_evento(eje, ley, usar_vril)
        print(f"\n[EVENTO] {descripcion}")
        print(f"  Interpretación: {interp}")

    def menu(self):
        while True:
            print("\n" + "═"*70)
            print("MENÚ PRINCIPAL - ZIGURAT v2.0")
            print("═"*70)
            print("1. Reporte de residuos")
            print("2. Interpretar código")
            print("3. Interpretar evento por vector")
            print("0. Salir")
            opc = input("\nOpción: ").strip()
            if opc == "1":
                self.cmd_report()
            elif opc == "2":
                cod = input("Código: ").strip()
                self.cmd_interpret(cod)
            elif opc == "3":
                desc = input("Descripción del evento: ")
                try:
                    eje = int(input("Eje: "))
                    ley = int(input("Ley: "))
                    vril = input("¿Usar VRIL? (s/n): ").lower() == "s"
                    self.interpretar_evento(desc, eje, ley, vril)
                except:
                    print("Datos inválidos")
            elif opc == "0":
                break


def main():
    sistema = SistemaZigurat()
    if len(sys.argv) > 1:
        if sys.argv[1] == "report":
            sistema.cmd_report()
    else:
        sistema.menu()


if __name__ == "__main__":
    main()
```
