# main.py

from calculos import (
    calcular_ms_por_hectarea_dia,
    requerimiento_diario_animal,
    oferta_total_ms,
    requerimiento_total_animales,
    capacidad_maxima_animales,
    animales_por_hectarea,
    calcular_ug_por_animal,
    carga_ug_ha,
    carga_maxima_ug_ha
)
from datos_pasturas import pasturas
from utils import (
    validar_numero,
    validar_entero,
    formato_kg,
    formato_toneladas,
    pausar
)

def main():
    print("🐄 Calculadora de Carga Ganadera 🐄\n")

    # Mostrar opciones de pasturas
    print("🌿 Tipos de pastura disponibles:")
    for key in pasturas:
        print(f"- {key}")
    
    # Elegir tipo de pastura
    pastura = input("\nIngresá el tipo de pastura: ").strip().lower()
    if pastura not in pasturas:
        print("❌ Tipo de pastura no válido.")
        return

    # Pedir datos al usuario con validación
    peso_vivo = validar_numero(input("Peso promedio del animal en kilogramos: "))
    if peso_vivo is None:
        print("❌ Entrada no válida para el peso.")
        return

    cantidad_animales = validar_entero(input("Cantidad de animales actuales: "))
    if cantidad_animales is None:
        print("❌ Entrada no válida para cantidad de animales.")
        return

    superficie_ha = validar_numero(input("Superficie disponible en hectáreas: "))
    if superficie_ha is None:
        print("❌ Entrada no válida para hectáreas.")
        return

    dias = validar_entero(input("¿Durante cuántos días desea mantener los animales?: "))
    if dias is None:
        print("❌ Entrada no válida para días.")
        return

    # Cálculos principales
    produccion_ms_ha_dia = calcular_ms_por_hectarea_dia(pastura, pasturas)
    req_diario = requerimiento_diario_animal(peso_vivo)
    oferta = oferta_total_ms(superficie_ha, produccion_ms_ha_dia, dias)
    requerido = requerimiento_total_animales(cantidad_animales, req_diario, dias)
    capacidad = capacidad_maxima_animales(oferta, req_diario, dias)

    # Cálculos adicionales de carga y unidades ganaderas
    animales_ha_dia = animales_por_hectarea(produccion_ms_ha_dia, req_diario)
    animales_ha_totales = animales_ha_dia / dias
    unidades_ganaderas_por_animal = calcular_ug_por_animal(peso_vivo)
    carga_actual_en_unidades_ganaderas_por_hectarea = carga_ug_ha(cantidad_animales, unidades_ganaderas_por_animal, superficie_ha)
    carga_maxima_en_unidades_ganaderas_por_hectarea = carga_maxima_ug_ha(capacidad, unidades_ganaderas_por_animal, superficie_ha)

    # Resultados
    print("\n📊 RESULTADOS:")
    print(f"Producción diaria de materia seca por hectárea: {formato_kg(produccion_ms_ha_dia)}")
    print(f"Requerimiento diario de materia seca por animal: {formato_kg(req_diario)}")
    print(f"Oferta total de forraje durante {dias} días: {formato_kg(oferta)} ({formato_toneladas(oferta)})")
    print(f"Requerimiento total de los animales actuales: {formato_kg(requerido)} ({formato_toneladas(requerido)})")
    print(f"Cantidad máxima de animales que el campo puede sostener durante {dias} días: {int(capacidad)}")

    print("\n📐 CARGA GANADERa:")
    print(f"Cantidad estimada de animales por hectárea durante {dias} días: {animales_ha_totales:.2f}")
    print(f"Equivalencia de cada animal en unidades ganaderas: {unidades_ganaderas_por_animal:.2f}")
    print(f"Carga ganadera actual: {carga_actual_en_unidades_ganaderas_por_hectarea:.2f} unidades ganaderas por hectárea")
    print(f"Carga ganadera máxima recomendada: {carga_maxima_en_unidades_ganaderas_por_hectarea:.2f} unidades ganaderas por hectárea")

    # Recomendación final
    print(f"\n👉 Recomendación: Podés mantener hasta {int(capacidad)} animales durante {dias} días sin sobrepastorear.\n")

    # Pausa final
    pausar()

if __name__ == "__main__":
    main()