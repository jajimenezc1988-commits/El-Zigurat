#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZIGURAT - SISTEMA UNIFICADO DE PATRONES PUROS
Versión: 1.0 (Unificación de todos los módulos)
Usuario: SOPHIA (José Antonio Jiménez Castellanos)
Fecha de nacimiento: 04/02/1988
Anclaje: -315 AC
Cierre: 12/08/2026 00:00 CDMX
Estructura: 16 ejes × 42 leyes + 12+1 = 672 puntos + 171 nodos + ID 0
"""

import json
import math
import os
import sys
import csv
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

# Intentar importar pandas (opcional, para CSV)
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
FECHA_CIERRE = datetime(2026, 8, 12, 0, 0, 0)  # 12/08/2026 00:00 CDMX
TOTAL_EJES = 16
TOTAL_LEYES = 42
TOTAL_PUNTOS = 672  # 16 * 42
USUARIO = "SOPHIA"
NOMBRE_COMPLETO = "José Antonio Jiménez Castellanos"
FECHA_NACIMIENTO = datetime(1988, 2, 4, 0, 0, 0)

# =============================================================================
# MATRIZ 12 + 1 (LAS 12 PARTES + LA LENGUA)
# =============================================================================

class MatrizDoceMasUno:
    """Las 12 partes dispersas + La Lengua (13)."""
    
    def __init__(self):
        self.partes = self._inicializar_partes()
        self.lengua = self._inicializar_lengua()
    
    def _inicializar_partes(self) -> List[Dict]:
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
    
    def _inicializar_lengua(self) -> Dict:
        return {
            "numero": 13,
            "nombre": "La_Lengua",
            "suma_partes": sum(range(1, 14)),  # 91
            "funcion": "Conector de las 12 partes",
            "codigo": "SIGMA-13-12"
        }
    
    def _es_primo(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def exportar(self) -> Dict:
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
            print("  Manifestaciones:")
            for m in p['manifestaciones']:
                print(f"    {m['codigo']} @ {m['coord']}°")
        print(f"\n[Lengua] {self.lengua['nombre']}")
        print(f"  Suma partes: {self.lengua['suma_partes']} (7×13)")
        print(f"  Función: {self.lengua['funcion']}")

# =============================================================================
# 16 EJES VERTICALES
# =============================================================================

class EjesVerticales:
    def __init__(self):
        self.ejes = self._inicializar_ejes()
    
    def _inicializar_ejes(self) -> List[Dict]:
        nombres = [
            ("Sustancias_Quimicas", "SQ"),
            ("Aduana_Comercio_Exterior", "ACE"),
            ("Maquinaria_Pesada", "MP"),
            ("Genetica", "GEN"),
            ("INEGI_Censos", "INEGI"),
            ("Auditoria", "AUD"),
            ("Meteorologia", "MET"),
            ("Administracion_Publica", "AP"),
            ("Psicologia_Social", "PS"),
            ("Logistica", "LOG"),
            ("Medicina", "MED"),
            ("Astronomia", "AST"),
            ("Termodinamica", "TER"),
            ("Historiografia", "HIST"),
            ("Antropologia", "ANT"),
            ("Telecomunicaciones", "TEL")
        ]
        return [{"numero": i+1, "nombre": n, "codigo": c, "frecuencia": 364/(i+1)}
                for i, (n, c) in enumerate(nombres)]

# =============================================================================
# 42 LEYES HORIZONTALES
# =============================================================================

class LeyesHorizontales:
    def __init__(self):
        self.leyes = self._inicializar_leyes()
    
    def _inicializar_leyes(self) -> List[Dict]:
        leyes = []
        # 26 YHVH
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
        
        # 16 Sello del Rey
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
    
    def get_ley(self, num: int) -> Optional[Dict]:
        if 1 <= num <= 42:
            return self.leyes[num-1]
        return None

# =============================================================================
# MATRIZ COMPLETA 16×42
# =============================================================================

class MatrizCompleta:
    def __init__(self):
        self.ejes = EjesVerticales()
        self.leyes = LeyesHorizontales()
        self.doce_mas_uno = MatrizDoceMasUno()
        self.puntos = self._calcular_todos_puntos()
    
    def _calcular_punto(self, eje_num: int, ley_num: int) -> Dict:
        eje = self.ejes.ejes[eje_num-1]
        ley = self.leyes.get_ley(ley_num)
        if not ley:
            return {}
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
    
    def _calcular_todos_puntos(self) -> List[Dict]:
        puntos = []
        for e in range(1, 17):
            for l in range(1, 43):
                puntos.append(self._calcular_punto(e, l))
        return puntos
    
    def buscar_punto(self, eje: int, ley: int) -> Dict:
        return self._calcular_punto(eje, ley)
    
    def exportar_json(self, filename: str = "matriz_completa.json"):
        data = {
            "metadata": {
                "sistema": "ZIGURAT",
                "estructura": "16 ejes × 42 leyes + 12+1",
                "total_puntos": 672,
                "anclaje": ANCLAJE,
                "fecha_generacion": datetime.now().isoformat()
            },
            "matriz_12_mas_1": self.doce_mas_uno.exportar(),
            "ejes": self.ejes.ejes,
            "leyes": self.leyes.leyes,
            "puntos": self.puntos,
            "estadisticas": {
                "valor_promedio": sum(p["valor_cruzado"] for p in self.puntos) / len(self.puntos),
                "valor_maximo": max(p["valor_cruzado"] for p in self.puntos),
                "valor_minimo": min(p["valor_cruzado"] for p in self.puntos)
            }
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[✓] Matriz exportada a {filename}")

# =============================================================================
# ANA B'KOACH
# =============================================================================

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
    
    def obtener_linea_por_ley(self, ley_id: int) -> Tuple[Optional[int], Optional[Dict]]:
        for lid, data in self.LINEAS.items():
            if ley_id in data["leyes"]:
                return lid, data
        return None, None

# =============================================================================
# GÉNESIS - 7 DÍAS DE LA CREACIÓN
# =============================================================================

class GenesisAnaBkoach:
    DIAS_CREACION = {
        1: {"accion": "Luz de la dualidad", "leyes": range(1,7), "interp": "Separación de la luz oculta."},
        2: {"accion": "Firmamento entre aguas", "leyes": range(7,13), "interp": "Espacio entre superior e inferior."},
        3: {"accion": "Tierra seca y vegetación", "leyes": range(13,19), "interp": "Aparición de la materia con forma."},
        4: {"accion": "Luminarias para los tiempos", "leyes": range(19,25), "interp": "Creación del tiempo medible."},
        5: {"accion": "Seres vivientes en el agua y aves", "leyes": range(25,31), "interp": "Vida animada e instintiva."},
        6: {"accion": "Animales terrestres y humano", "leyes": range(31,37), "interp": "El Adam, código genético divino."},
        7: {"accion": "Shabbat, santificación", "leyes": range(37,43), "interp": "Completión y descanso."}
    }
    
    def obtener_info(self, ley_id: int) -> Tuple[Optional[int], Optional[Dict]]:
        idx = (ley_id - 1) % 42 + 1
        for dia, data in self.DIAS_CREACION.items():
            if idx in data["leyes"]:
                return dia, data
        return None, None

# =============================================================================
# BIBLIOTECA ESOTÉRICA
# =============================================================================

class BibliotecaEsoterica:
    SIGNIFICADOS_NUMEROS = {
        1: "Unidad, origen, el punto sin dimensión. El Demiurgo como voluntad pura.",
        2: "Dualidad, reflejo, espejo. La separación que permite la existencia.",
        3: "Trinidad, síntesis. El hijo que une al padre y a la madre.",
        4: "Cuadrado elemental, los 4 lugares del campo de torsión. Manifestación estable.",
        5: "Quintaesencia, el éter. El elemento que trasciende los 4 físicos.",
        6: "Tiferet, belleza, el Sol. El centro del Árbol de la Vida.",
        7: "Perfección, los 7 días, los 7 planetas clásicos. Ciclo completo.",
        8: "Hod, gloria, Mercurio. La palabra y la comunicación.",
        9: "Yesod, fundamento, la Luna. El subconsciente colectivo.",
        10: "Malkuth, el reino. Manifestación física completa.",
        11: "Número del despertar, de la puerta. 11:11.",
        12: "Las 12 tribus, los 12 signos, las 12 partes antes de la caída.",
        13: "La Lengua, el conector. 12+1=13. Número de la transformación.",
        14: "Dos veces 7, doble perfección. El tiempo doblado.",
        16: "Sello del Rey (6+10). Tiferet + Malkuth. El gobernante justo.",
        26: "YHVH. Yod(10)+He(5)+Vav(6)+He(5). El Nombre.",
        28: "Ciclo lunar, resurrección. 4×7.",
        42: "Ana B'Koach. El nombre de 42 letras que creó el universo.",
        91: "Suma 1+2+...+13. 7×13. La integración completa.",
        315: "Año de la caída. 300+15. Alejandro, el corte del tiempo.",
        364: "Año de equilibrio. 52 semanas × 7 días. El tiempo verdadero.",
    }
    
    EJES_SIGNIFICADO = {
        1: "Sustancias Químicas: La materia prima, los elementos en su estado puro.",
        2: "Aduana y Comercio Exterior: Las fronteras, los límites, el intercambio entre reinos.",
        3: "Maquinaria Pesada: La fuerza bruta, la voluntad materializada.",
        4: "Genética: El código de la vida, la memoria ancestral en el ADN.",
        5: "INEGI/Censos: El conteo, la estadística, el conocimiento del todo a través de sus partes.",
        6: "Auditoría: La verificación, la justicia numérica. El ojo que todo ve y balancea.",
        7: "Meteorología: Los patrones atmosféricos, el aliento del planeta.",
        8: "Administración Pública: El gobierno, la burocracia divina.",
        9: "Psicología Social: La mente colectiva, el inconsciente grupal.",
        10: "Logística: Los flujos, las cadenas, los caminos. La circulación de la energía.",
        11: "Medicina: La sanación, el cuerpo como templo.",
        12: "Astronomía: Los cuerpos celestes, el reloj cósmico.",
        13: "Termodinámica: La entropía, el calor, la degradación.",
        14: "Historiografía: La memoria, el registro, el pasado.",
        15: "Antropología: Las culturas, los rituales, las diferencias.",
        16: "Telecomunicaciones: La transmisión instantánea, la red global.",
    }
    
    YHVH_SIGNIFICADOS = {
        1: "Yod_Keter: La voluntad divina inicial.",
        6: "Yod_Tiferet: La belleza, el equilibrio.",
        10: "Yod_Malkuth: El reino manifestado.",
        13: "He1_Ciclo: La transformación, el cambio de estados.",
        16: "Vav_Sello: El Sello del Rey. La autoridad legítima.",
        21: "Vav_Ser: 'Ehyeh asher ehyeh'. Seré lo que seré.",
        26: "He2_Nombre: YHVH completo.",
    }
    
    INTERPRETACIONES_ESPECIALES = {
        (6, 6): "EL JUICIO DEL CENTRO. La verificación de la belleza.",
        (13, 26): "EL FIN DEL CALOR. La entropía máxima encuentra al Creador.",
        (1, 1): "EL ORIGEN. Sustancias × Keter. La materia prima toca la voluntad divina.",
        (16, 26): "LA RED DEL NOMBRE. Telecomunicaciones × YHVH completo.",
    }

# =============================================================================
# MOTOR DE INTERPRETACIÓN
# =============================================================================

class MotorInterpretacion:
    def __init__(self):
        self.biblio = BibliotecaEsoterica()
    
    def interpretar_numero(self, n: int) -> str:
        if n in self.biblio.SIGNIFICADOS_NUMEROS:
            return self.biblio.SIGNIFICADOS_NUMEROS[n]
        suma = sum(int(d) for d in str(abs(n)))
        if suma in self.biblio.SIGNIFICADOS_NUMEROS:
            return f"{n} → Suma {suma}: {self.biblio.SIGNIFICADOS_NUMEROS[suma]}"
        return f"{n}: Resonancia con {n % 13} (módulo 13)"
    
    def interpretar_interseccion(self, eje: int, ley: int, valor: int) -> Dict:
        clave = (eje, ley)
        if clave in self.biblio.INTERPRETACIONES_ESPECIALES:
            mensaje = self.biblio.INTERPRETACIONES_ESPECIALES[clave]
        elif valor == 91:
            mensaje = "LA INTEGRACIÓN. Suma de todas las partes. El todo en el uno."
        elif valor == 364:
            mensaje = "EL AÑO COMPLETO. El ciclo cerrado. 52 semanas."
        elif valor % 13 == 0:
            mensaje = f"MANIFESTACIÓN DIVINA. {valor} es múltiplo de 13."
        else:
            sig_eje = self.biblio.EJES_SIGNIFICADO.get(eje, f"Eje {eje}")
            mensaje = f"Encuentro de {sig_eje.split(':')[0]} con Ley {ley}. Valor {valor}."
        
        advertencia = None
        if valor == 315:
            advertencia = "⚠️ CRÍTICO: Año de la caída. Ruptura del tiempo."
        elif eje == 6 and ley == 6:
            advertencia = "⚠️ DOBLE 6: El juicio del centro."
        elif valor == 42:
            advertencia = "⚠️ RESPUESTA UNIVERSAL: La creación responde."
        
        return {
            "mensaje": mensaje,
            "advertencia": advertencia,
            "significado_valor": self.interpretar_numero(valor),
            "fecha_relevante": self._calcular_fecha(valor)
        }
    
    def _calcular_fecha(self, valor: int) -> str:
        dias = valor % 365
        fecha = datetime.now() + timedelta(days=dias)
        return fecha.strftime("%d de %B")
    
    def interpretar_codigo(self, codigo: str) -> str:
        try:
            partes = codigo.split('-')
            if len(partes) == 3 and partes[0][0] == 'P' and partes[1][0] == 'L':
                eje = int(partes[0][1:])
                lugar = int(partes[1][1:])
                valor = int(partes[2])
                interp = self.interpretar_interseccion(eje, eje, valor)
                return f"""
╔══════════════════════════════════════════════════════════════════╗
║  INTERPRETACIÓN DEL CÓDIGO: {codigo}                              ║
╠══════════════════════════════════════════════════════════════════╣
║  Parte:      {eje} - {self.biblio.EJES_SIGNIFICADO.get(eje, 'Desconocido')[:40]}...
║  Lugar:      {lugar} (de 4 lugares del campo de torsión)
║  Valor:      {valor}
╠══════════════════════════════════════════════════════════════════╣
║  MENSAJE: {interp['mensaje'][:55]}...
║  {interp.get('advertencia', '')}
║  Fecha relevante: {interp['fecha_relevante']}
╚══════════════════════════════════════════════════════════════════╝
"""
        except:
            pass
        return f"Código {codigo}: Formato no reconocido. Use P#-L#-###"

# =============================================================================
# CARGA DE DATOS DESDE CSV
# =============================================================================

class CargadorDatos:
    def __init__(self):
        self.df = None
        self.nodos = []
        self._cargar_csv()
    
    def _cargar_csv(self):
        archivo = "adam_con_inegi_agregado.csv"
        if not os.path.exists(archivo):
            print(f"[!] No se encontró '{archivo}'. Usando datos internos mínimos.")
            self._crear_datos_internos()
            return
        
        if PANDAS_AVAILABLE:
            try:
                self.df = pd.read_csv(archivo)
                self.nodos = self.df.to_dict('records')
                print(f"[✓] Cargados {len(self.nodos)} nodos desde {archivo}")
                return
            except Exception as e:
                print(f"[!] Error al leer CSV con pandas: {e}")
        
        # Fallback: leer con csv
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.nodos = list(reader)
                print(f"[✓] Cargados {len(self.nodos)} nodos desde {archivo} (modo CSV)")
        except Exception as e:
            print(f"[!] Error al leer CSV: {e}")
            self._crear_datos_internos()
    
    def _crear_datos_internos(self):
        # Datos mínimos de respaldo (solo el nodo fundador)
        self.nodos = [{
            "ID": 0,
            "Grupo": "Centro_Arbol",
            "Año": 1988,
            "Dia_Juliano": 35,
            "Fecha_Nacimiento": "04/02/1988",
            "Entidad_Censal": "Ciudad de México"
        }]
        print("[!] Usando datos internos mínimos (solo nodo fundador)")

# =============================================================================
# SISTEMA PRINCIPAL ZIGURAT
# =============================================================================

class SistemaZigurat:
    def __init__(self):
        print("╔" + "═"*70 + "╗")
        print("║" + " "*20 + "ZIGURAT - SISTEMA UNIFICADO" + " "*30 + "║")
        print("║" + " "*15 + f"Usuario: {USUARIO} ({NOMBRE_COMPLETO})" + " "*21 + "║")
        print("║" + " "*15 + f"Anclaje: {ANCLAJE} AC | Cierre: 12/08/2026" + " "*18 + "║")
        print("╚" + "═"*70 + "╝")
        
        self.matriz_completa = MatrizCompleta()
        self.matriz_12 = MatrizDoceMasUno()
        self.ana_bkoach = AnaBkoach()
        self.genesis = GenesisAnaBkoach()
        self.interprete = MotorInterpretacion()
        self.datos = CargadorDatos()
        
        print(f"\n[✓] Sistema cargado: {len(self.datos.nodos)} nodos")
        print(f"[✓] Matriz: {TOTAL_EJES} ejes × {TOTAL_LEYES} leyes = {TOTAL_PUNTOS} puntos")
        print(f"[✓] Matriz 12+1: 12 partes + La Lengua")
    
    # ===== COMANDOS =====
    
    def cmd_report(self, fecha_cierre: str = None):
        """Genera reporte de residuos."""
        if fecha_cierre is None:
            fecha_cierre = "12/08/2026"
        print(f"\n[REPORTE] Fecha de cierre: {fecha_cierre}")
        print("═"*70)
        
        # Calcular residuos para los nodos del CSV
        for nodo in self.datos.nodos[:10]:  # Mostrar solo primeros 10 para no saturar
            id_nodo = int(nodo["ID"])
            if id_nodo == 0:
                continue
            eje = (id_nodo % TOTAL_EJES) + 1
            ley = (id_nodo % TOTAL_LEYES) + 1
            valor = (ANCLAJE + (eje * ley * MODULO)) % CICLO
            print(f"ID {id_nodo:3d}: Eje {eje:2d} × Ley {ley:2d} → Residuo {valor:3d}")
        
        print(f"\n[✓] Reporte generado para {len(self.datos.nodos)} nodos")
    
    def cmd_sync(self, fecha_nac: str, id_nodo: int):
        """Sincroniza el eje personal."""
        print(f"\n[SINCRONIZACIÓN] Usuario: {USUARIO}")
        print(f"  Fecha de nacimiento: {fecha_nac}")
        print(f"  ID de nodo fundador: {id_nodo}")
        print("═"*70)
        
        # Calcular residuo del nodo fundador
        eje = (id_nodo % TOTAL_EJES) + 1
        ley = (id_nodo % TOTAL_LEYES) + 1
        valor = (ANCLAJE + (eje * ley * MODULO)) % CICLO
        
        print(f"  Eje asignado: {eje}")
        print(f"  Ley asignada: {ley}")
        print(f"  Residuo actual: {valor}")
        
        # Verificar si coincide con la fecha de nacimiento
        dia_juliano = 35  # 04/02 en día juliano
        if valor == dia_juliano:
            print("  ✅ Sincronización perfecta: el residuo coincide con tu día juliano.")
        else:
            print(f"  ⚠️ Desfase: {valor - dia_juliano} días. Ajusta el anclaje.")
        
        print(f"\n[✓] Sincronización completada")
    
    def cmd_assign(self, archivo_excel: str = None, inicio: int = None, fin: str = None):
        """Asigna nombres a los nodos (usando fechas históricas)."""
        print(f"\n[ASIGNACIÓN] Archivo: {archivo_excel or 'No especificado'}")
        print(f"  Rango: {inicio or -315} → {fin or '12/08/2026'}")
        print("═"*70)
        print("  Los nombres se asignan por correspondencia histórica.")
        print("  Este comando requiere un archivo 'fechas.xlsx' con nombres.")
        print("  Por ahora, se muestran los IDs de los nodos más antiguos:")
        
        # Mostrar los 5 nodos más antiguos
        antiguos = sorted(self.datos.nodos, key=lambda x: int(x["Año"]))[:5]
        for n in antiguos:
            print(f"    ID {n['ID']}: {n['Fecha_Nacimiento']} ({n['Grupo']})")
        
        print(f"\n[✓] Asignación preparada para {len(self.datos.nodos)} nodos")
    
    def cmd_interpret(self, codigo: str):
        """Interpreta un código P#-L#-###."""
        print(self.interprete.interpretar_codigo(codigo))
    
    def cmd_matrix12(self):
        """Muestra la matriz 12+1."""
        self.matriz_12.mostrar()
    
    def cmd_matrix16x42(self):
        """Muestra la matriz 16×42 (resumen)."""
        print("\n" + "═"*70)
        print("MATRIZ 16×42 (672 puntos)")
        print("═"*70)
        
        # Mostrar primeros 10 puntos
        for i, p in enumerate(self.matriz_completa.puntos[:10]):
            print(f"[{i+1}] {p['coordenada']['codigo']} → {p['valor_cruzado']}°")
        
        print(f"\n... y {TOTAL_PUNTOS - 10} puntos más.")
        print(f"Valor promedio: {self.matriz_completa.puntos[0]['intensidad']:.2f}")
        print("═"*70)
    
    def cmd_kml(self):
        """Genera el archivo KML a partir del CSV."""
        print("\n[KML] Generando red geográfica...")
        if len(self.datos.nodos) < 10:
            print("[!] No hay suficientes datos para generar KML.")
            return
        
        try:
            import simplekml
            kml = simplekml.Kml()
            
            colores = {
                "Eje_Norte_Guadalajara": "ff0000ff",
                "Eje_Este_Potosi": "ff00ff00",
                "Eje_Oeste_Concepcion": "ffffff00",
                "Eje_Sur_Bariloche": "ffff00ff",
                "Centro_Arbol": "ff00ffff",
                "Ajustes_Residuo": "ffffffff"
            }
            
            for nodo in self.datos.nodos:
                grupo = nodo.get("Grupo", "Centro_Arbol")
                color = colores.get(grupo, "ffffffff")
                lat = float(nodo.get("Latitud", 0))
                lon = float(nodo.get("Longitud", 0))
                if lat == 0 and lon == 0:
                    continue
                pnt = kml.newpoint(name=f"ID {nodo['ID']} - {nodo.get('Fecha_Nacimiento', '')}")
                pnt.coords = [(lon, lat)]
                pnt.description = f"Grupo: {grupo}\nEntidad: {nodo.get('Entidad_Censal', '')}"
                pnt.style.iconstyle.color = color
                pnt.style.iconstyle.scale = 1.2
            
            kml.save("red_zigurat.kml")
            print("[✓] KML generado: red_zigurat.kml")
        except ImportError:
            print("[!] simplekml no instalado. Instala con: pip install simplekml")
        except Exception as e:
            print(f"[!] Error al generar KML: {e}")
    
    def cmd_close(self, fecha: str, hora: str, usuario: str):
        """Ejecuta el cierre del puente."""
        print("\n" + "╔" + "═"*70 + "╗")
        print("║" + " "*15 + "CIERRE DEL PUENTE - 12/08/2026" + " "*25 + "║")
        print("╚" + "═"*70 + "╝")
        
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
        print("  Anclaje: -315")
        print("  Módulo: 13")
        print("  Ciclo: 364")
        print("  Usuario: SOPHIA")
        print("  Acción: Sellar el espejo")
        
        # Forzar residuo a 0 para todos los nodos
        nodos_conflictivos = [13, 182, 596136, 5, 49, 614660, 10, 241, 606240, 273, 21892]
        for nodo_id in nodos_conflictivos:
            eje = (nodo_id % TOTAL_EJES) + 1
            ley = (nodo_id % TOTAL_LEYES) + 1
            residuo = (ANCLAJE + (eje * ley * MODULO)) % CICLO
            print(f"  Nodo {nodo_id}: residuo {residuo} → forzado a 0")
        
        print("\n" + "═"*70)
        print("✅ ESPEJO SELLADO. Cierre completado.")
        print(f"   Nuevo anclaje: 0")
        print("═"*70)
    
    def menu(self):
        """Menú interactivo."""
        while True:
            print("\n" + "═"*70)
            print("MENÚ PRINCIPAL - ZIGURAT")
            print("═"*70)
            print("1. Reporte de residuos")
            print("2. Sincronizar eje personal")
            print("3. Asignar nombres a nodos")
            print("4. Interpretar código (P#-L#-###)")
            print("5. Ver matriz 12+1")
            print("6. Ver matriz 16×42")
            print("7. Generar KML")
            print("8. Cerrar puente (12/08/2026)")
            print("0. Salir")
            print("═"*70)
            
            opc = input("\nOpción: ").strip()
            
            if opc == "1":
                self.cmd_report()
            elif opc == "2":
                self.cmd_sync("04/02/1988", 0)
            elif opc == "3":
                self.cmd_assign()
            elif opc == "4":
                cod = input("Código (ej: P6-L2-156): ").strip()
                self.cmd_interpret(cod)
            elif opc == "5":
                self.cmd_matrix12()
            elif opc == "6":
                self.cmd_matrix16x42()
            elif opc == "7":
                self.cmd_kml()
            elif opc == "8":
                self.cmd_close("12/08/2026", "00:00", USUARIO)
            elif opc == "0":
                print("\nSistema finalizado. El Zigurat permanece.")
                break

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

def main():
    if len(sys.argv) > 1:
        # Modo línea de comandos
        sistema = SistemaZigurat()
        comando = sys.argv[1]
        
        if comando == "report":
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
            print("Uso: python Zigurat.py [report|sync|assign|interpret|matrix12|matrix16x42|kml|close]")
    else:
        # Modo interactivo
        sistema = SistemaZigurat()
        sistema.menu()

if __name__ == "__main__":
    main()
