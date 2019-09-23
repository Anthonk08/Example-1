#Cifrado Caesar, sistema de cifrado creado por Caesar para enviar sus 
# mensajes mas importantes a sus generales sin que espias descubrieran
# la informacion que contenian sus cartas.


def cifrado_caesar(texto):
    abc="abcdefghijklmnñopqrstuvwxyz"
    cif = ""
    for c in texto:
        if c in abc:
            if (abc.index(c) + 3 > len(abc)):
                cif += abc[((abc.index(c) + 3) - len(abc))]
            else: cif += abc[(abc.index(c) + 3)]
        else:
            cif += c
    return cif

# print(cifrado_caesar("la soledad ha sido una verdadera amiga, nunca me ha dejado, aun cuando yo trato de alejarme de ella, siempre esta conmigo"))
# print(cifrado_caesar("stay with me, no, you don't need to run"))
# print(cifrado_caesar("somebody that i used to know"))
# print(cifrado_caesar("do they know I was grown with you?"))


def descifrar(texto1):
    cof = "abcdefghijklmnñopqrstuvwxyz"
    txt = ""
    for c in texto1:
        if c in cof:
            if (cof.index(c) - 3 < 0):
                txt += cof[((cof.index(c) - 3) + len(cof))]
            else: txt += cof[(cof.index(c) - 3)]
        else:
            txt += c
    
    return txt

hola = cifrado_caesar("do they know I was grown with you?")
print(hola)
print(descifrar(hola))
# print(descifrar("\n\nñd vrñhgdg kd vlgr xpd yhugdghud doljd, pxpfd oh kd ghmdgr, dxp fxdpgr br wudwr gh dñhmduoh gh hññd, vlhosuh hvwd frpoljr"))
# print(descifrar("vrohergb wkdw l xvhg wr nprz"))
# print(descifrar("gr wkhb nprz I zdv jurzp zlwk brx?"))