# calculos.py

# calculos.py

def calcular_ms_por_hectarea_dia(pastura, pasturas_dict):
    datos = pasturas_dict[pastura]
    return datos["produccion_verde"] * (datos["ms_pct"] / 100)

def requerimiento_diario_animal(peso_vivo):
    return peso_vivo * 0.03

def oferta_total_ms(superficie_ha, produccion_ms_ha_dia, dias):
    return superficie_ha * produccion_ms_ha_dia * dias

def requerimiento_total_animales(cantidad_animales, req_diario, dias):
    return cantidad_animales * req_diario * dias

def capacidad_maxima_animales(oferta_total, req_diario, dias):
    return oferta_total / (req_diario * dias)

#Animales que se pueden mantener por hectárea por día
def animales_por_hectarea(produccion_ms_ha_dia, req_diario):
    return produccion_ms_ha_dia / req_diario

#Equivalencia de un animal en unidades ganaderas (UG)
def calcular_ug_por_animal(peso_vivo, peso_ug=450):
    return peso_vivo / peso_ug

#Carga actual en UG/ha
def carga_ug_ha(cantidad_animales, ug_animal, superficie_ha):
    return (cantidad_animales * ug_animal) / superficie_ha

#Carga máxima estimada en UG/ha según capacidad
def carga_maxima_ug_ha(capacidad_animales, ug_animal, superficie_ha):
    return (capacidad_animales * ug_animal) / superficie_ha
