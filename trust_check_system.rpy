#============================================================
# CHECK SYSTEMS
#============================================================

label check_maximo_trust:
    if maximo_trust <= 0:
        jump game_over_maximo
    elif maximo_trust == 1:
        jump maximo_glitch
    else:
        return
    return

label check_ysabel_trust:
    if ysabel_trust <= 0:
        jump game_over_ysabel
    elif ysabel_trust == 1:
        jump placeholder_glitch
    return

label check_dawani_trust:
    if dawani_trust <= 0:
        jump game_over_dawani
    elif dawani_trust == 1:
        jump placeholder_glitch
    else:
        return
    return