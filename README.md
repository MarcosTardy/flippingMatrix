# Descripción del problema
Dada una matriz cuadrada de tamaño 2n x 2n, cada celda contiene un número entero. El objetivo es maximizar la suma de los elementos en la submatriz cuadrada superior izquierda de tamaño n x n.

Para lograr esto, se permiten operaciones que consisten en intercambiar filas o columnas completas de la matriz. Es decir, puedes "voltear" (flip) filas o columnas para reorganizar los elementos y así maximizar la suma de esa submatriz.

Detalles
La matriz original tiene dimensiones 2n x 2n.

La submatriz objetivo es la esquina superior izquierda, de tamaño n x n.

Las operaciones permitidas son:

Intercambiar (flip) cualquier fila con otra fila.

Intercambiar (flip) cualquier columna con otra columna.

Estas operaciones pueden usarse cualquier cantidad de veces para colocar los números más grandes dentro de la submatriz superior izquierda y maximizar su suma.

# Ejemplo
Si tienes una matriz 4x4 (2n=4, n=2):

1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16
Puedes intercambiar filas y columnas para que la submatriz 2x2 superior izquierda tenga la suma máxima posible.

# Enfoque para resolverlo
Para maximizar la suma en la submatriz n x n:

Observa que para cada posición (i, j) en esa submatriz hay cuatro candidatos posibles en la matriz original debido a las posibles inversiones:

(i, j)

(i, 2n - 1 - j)

(2n - 1 - i, j)

(2n - 1 - i, 2n - 1 - j)

Puedes escoger el máximo valor entre esos cuatro para colocar en la posición (i, j) de la submatriz.

Sumando esos máximos para toda la submatriz n x n obtienes el valor máximo posible.

# Objetivo
Implementar una función que reciba la matriz 2n x 2n y retorne la suma máxima posible en la submatriz n x n tras aplicar las operaciones permitidas.

