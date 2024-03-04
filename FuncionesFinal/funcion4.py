def calcularimpuesto(CantidadSinIva, PorsentajeDeIVA):
    if PorsentajeDeIVA == 0:
        PorsentajeDeIVA = 21
    iva = CantidadSinIva * (PorsentajeDeIVA* .01)
    return iva 
impuesto = calcularimpuesto(100,.16)
print(impuesto)