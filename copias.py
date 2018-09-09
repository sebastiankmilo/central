import sys
import os
nb_dir = os.path.split(os.getcwd())[0]
if nb_dir not in sys.path:
    sys.path.append(nb_dir)
    pass
import ipywidgets as widgets
from IPython.display import display
from random import shuffle
from Tonos import Tonos
from Abonado import Abonado
from Central import CentralTelefonica
from random import randrange

t = Tonos()
x = range(400)
ListaAbonados = []
shuffle(x)
for y in xrange(400):
    terminado = str(x[y])
    if x[y] < 10:
        telefono = "860000"
        pass
    elif x[y] < 100:
        telefono = "86000"
        pass
    else:
        telefono = "8600"
        pass
    if y < 79:
        estado = -1
        pass
    elif y < 279:
        estado = 0
        pass
    else:
        estado = 1
        pass
    telefono = int(telefono+terminado)
    persona = 'sujeto de prueba #'+terminado
    abno = Abonado(persona, telefono, estado)
    ListaAbonados.append(abno)
    pass
d={ListaAbonados[0].telefono: ListaAbonados[0]}
for x in xrange(1,400):
    d[ListaAbonados[x].telefono]=ListaAbonados[x]
    pass
Central1 = CentralTelefonica(d, '57')
global usuario
usuario=8600200
items_layout = widgets.Layout(width='100%',
                              height='100%',
                              justify_content='flex-end')
style = {'value_align': 'center'}
pantallita = widgets.Text(value='0000000', disabled=True,
                          layout=items_layout, style=style)
pantallita2 = widgets.HTML(value='<p style="text-align: center;">8600317<p>')
words = ['1', '2', '3', '4', '5', '6', '7',
         '8', '9', 'clear', '0', 'llamar', 'fact', 'histo']
items = [widgets.Button(description=w) for w in words]
c1 = widgets.VBox(children=[items[0], items[3], items[6], items[9]])
c2 = widgets.VBox(children=[items[1], items[4], items[7], items[10]])
c3 = widgets.VBox(children=[items[2], items[5], items[8], items[11]])
f4 = widgets.HBox(children=[items[12], items[13]])
b = [c1, c2, c3]
box_layout = widgets.Layout(display='flex',
                            flex_flow='column',
                            align_items='center',
                            border='solid',
                            width='50%')
box = widgets.Box(children=b)
f4 = widgets.VBox(children=[pantallita2, box, f4], layout=box_layout)


contador = 0


def remplazo(n):
    texto = pantallita2.value
    texto1 = texto[texto.find('>')+1:texto.find('<', 3, len(texto)-1)]
    pos = len(texto1)-1
    tecla = n
    textol = list(texto1)
    textol.append(tecla)
    pos = len(textol)
    if pos < 7:
        texto2 = []
        texto2 = textol
        pass
    else:
        texto2 = textol[1:pos]
        pass
    telefono = "".join(texto2)
    texto = '<p style="text-align: center;">'+telefono+'<p>'
    pantallita2.value = texto
    pass

def bo0(b):
    t.load(10)
    remplazo('0')
    global contador
    contador = contador+1
    pass

def bo1(b):
    t.load(1)
    remplazo('1')
    global contador
    contador = contador+1
    pass

def bo2(b):
    t.load(2)
    remplazo('2')
    global contador
    contador = contador+1
    pass

def bo3(b):
    t.load(3)
    remplazo('3')
    global contador
    contador = contador+1
    pass

def bo4(b):
    t.load(4)
    remplazo('4')
    global contador
    contador = contador+1
    pass

def bo5(b):
    t.load(5)
    remplazo('5')
    global contador
    contador = contador+1
    pass

def bo6(b):
    t.load(6)
    remplazo('6')
    global contador
    contador = contador+1
    pass

def bo7(b):
    t.load(7)
    remplazo('7')
    global contador
    contador = contador+1
    pass

def bo8(b):
    t.load(8)
    remplazo('8')
    global contador
    contador = contador+1
    pass

def bo9(b):
    t.load(9)
    remplazo('9')
    global contador
    contador = contador+1
    pass

def clear(b):
    global contador
    contador = 0
    telefono = '0000000'
    texto = '<p style="text-align: center;">'+telefono+'<p>'
    pantallita2.value = texto
    pass

def llamar(b):
    texto = pantallita2.value
    destino = texto[texto.find('>')+1:texto.find('<', 3, len(texto)-1)]
    destino = int(destino)
    Central1.llamar(usuario,destino)
    pass


def fact(b):
    t.load(9)
    pantallita2.value = str(0)
    pass


def hist(b):
    pass


metodos = {0: bo0, 1: bo1, 2: bo2, 3: bo3, 4: bo4,
           5: bo5, 6: bo6, 7: bo7, 8: bo8, 9: bo9,
           10: clear, 12: llamar, 13: fact, 14: hist}
for n in xrange(12):
    if n == 10:
        items[10].on_click(metodos.get((0), ""))
        pass
    else:
        items[n].on_click(metodos.get((n+1), ""))
    pass
f4
#col1 = widgets.VBox([items[0], items[3]], items[6])
#col2 = widgets.VBox([items[1], items[4]], items[7])
#col3 = widgets.VBox([items[2], items[5]], items[8])
#widgets.HBox([col1, col2, col3])
#8600267