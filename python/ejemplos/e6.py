def pedir_confirmacion(p, r=4, q='Si o No, por favor!'):

    while True:
        ok = raw_input()
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
           return True
        if ok in ('n','no','No','NO'):
           return False
        r = r - 1
        if r < 0:
           raise IOError('usuario duro')
        print (q)
