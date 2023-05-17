from IPython.display import display
import pandas as pd
import random
import time
import sys
sys.setrecursionlimit(10000)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i
def quickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quickSort(lista, inicio, p-1)
        quickSort(lista, p+1, fim)
    return lista

def bubbleSort(lista): 
    n = len(lista) 
    for i in range(n):
        for j in range(0, n-i-1):
                if lista[j] > lista[j+1] : 
                        lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1
def mergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergeSort(lista, inicio, meio)
        mergeSort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
    return lista

sequencia_k1 = []
sequencia_k2 = []
sequencia_k3 = []
for i in range (100):
    sequencia_k1.append(random.randrange(100))
inicio_quickSort_1 = time.time()
k_1 = quickSort(sequencia_k1)
fim_quickSort_1 = time.time()
tempo_exe_quickSort_1 = fim_quickSort_1 - inicio_quickSort_1

inicio_bubbleSort_1 = time.time()
k_1 = bubbleSort(sequencia_k1)
fim_bubbleSort_1 = time.time()
tempo_exe_bubbleSort_1 = fim_bubbleSort_1 - inicio_bubbleSort_1

inicio_mergeSort_1 = time.time()
k_1 = mergeSort(sequencia_k1)
fim_mergeSort_1 = time.time()
tempo_exe_mergeSort_1 = fim_mergeSort_1 - inicio_mergeSort_1

for i in range (500):
    sequencia_k2.append(random.randrange(500))
inicio_bubbleSort_2 = time.time()
k_2 = bubbleSort(sequencia_k2)
fim_bubbleSort_2 = time.time()
tempo_exe_bubbleSort_2 = fim_bubbleSort_2 - inicio_bubbleSort_2

inicio_quickSort_2 = time.time()
k_2 = quickSort(sequencia_k2)
fim_quickSort_2 = time.time()
tempo_exe_quickSort_2 = fim_quickSort_2 - inicio_quickSort_2

inicio_mergeSort_2 = time.time()
k_2 = mergeSort(sequencia_k2)
fim_mergeSort_2 = time.time()
tempo_exe_mergeSort_2 = fim_mergeSort_2 - inicio_mergeSort_2

for i in range (1000):
    sequencia_k3.append(random.randrange(1000))
inicio_bubbleSort_3 = time.time()
k_3 = bubbleSort(sequencia_k3)
fim_bubbleSort_3 = time.time()
tempo_exe_bubbleSort_3 = fim_bubbleSort_3 - inicio_bubbleSort_3

inicio_quickSort_3 = time.time()
k_3 = quickSort(sequencia_k3)
fim_quickSort_3 = time.time()
tempo_exe_quickSort_3 = fim_quickSort_3 - inicio_quickSort_3

inicio_mergeSort_3 = time.time()
k_3 = mergeSort(sequencia_k3)
fim_mergeSort_3 = time.time()
tempo_exe_mergeSort_3 = fim_mergeSort_3 - inicio_mergeSort_3

dict = {'Algoritmo' : ['MergeSort', 'BubbleSort', 'QuickSort'],
        'k_1' : [100, 100, 100],
        'Tempo_exe_1' : [tempo_exe_mergeSort_1, tempo_exe_bubbleSort_1, tempo_exe_quickSort_1],
        'k_2' : [500, 500, 500],
        'Tempo_exe_2' : [tempo_exe_mergeSort_2, tempo_exe_bubbleSort_2, tempo_exe_quickSort_2],
        'k_3' : [1000, 1000, 1000],
        'Tempo_exe_3' : [tempo_exe_mergeSort_3, tempo_exe_bubbleSort_3, tempo_exe_quickSort_3]}
df = pd.DataFrame(dict)
display(df)