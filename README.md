Undermath

Este paquete contiene módulos para realizar cálculos aritméticos y estadísticos sencillos.

Uso como script

    python3 main.py <operación> <operandos separados por espacios>

    Operaciones aritméticas soportadas:
        -sum, --sumar :         Suma dos o más operandos de tipo int o float separados por espacios.

        -dif, --restar:         Resta al primer operando el segundo.

        -mult, --multiplicar:   Multiplica dos o más operandos de tipo int o float.

        -div, --dividir:        Divide el primer operando entre el segundo.

    Funciones estadísticas soportadas:
        -med, --media:
            Obtiene la media de una lista de elementos enteros o flotantes separados por espacios.

        -mdn, --mediana:
            Obtiene la mediana de una lista de elementos enteros o flotantes separados por espacios.

        -mod, --moda:
            Obtiene la moda de una lista de elementos enteros o flotantes separados por espacios.

        -dsm,--desviacion-estandar-muestral:
            Obtiene la desviación estándar muestral de una lista de elementos enteros o flotantes separados por espacios.

        -dsp, --desviacion-estandar-poblacional
            Obtiene la desviación estándar poblacional de una lista de elementos enteros o flotantes separados por espacios.

Uso como módulo

    Operaciones aritméticas

        from undermath.modulos_aritmeticos.operaciones_basicas import *
    
    Funciones estadísticas

        from undermath.modulos_estadisticos.funciones_estadisticas import *
