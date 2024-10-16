# Funciones utilizadas en el proyecto

# Unificar las posiciones de los jugadores y simplificar la columna "Pos"

def unificar_posiciones(pos):
    pos = ','.join(sorted([p.strip() for p in pos.split(',')]))
    
    if pos == 'MF':
        return 'MF'
    elif 'FW' in pos:
        return 'MF,FW'
    elif 'DF' in pos:
        return 'MF,DF'
    return pos