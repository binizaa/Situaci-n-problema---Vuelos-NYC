# Programa de Consulta de Vuelos - PROFE ALEX

Este proyecto está diseñado para permitir a los usuarios consultar y analizar información sobre vuelos, incluyendo detalles como la cantidad de vuelos desde aeropuertos específicos, retrasos, distancias recorridas, y mucho más. Los usuarios pueden seleccionar entre una variedad de consultas para visualizar datos específicos sobre vuelos y obtener resúmenes estadísticos para un mejor análisis.

El programa se ejecuta a través del archivo `main.py` y proporciona un menú interactivo para la entrada de datos por parte del usuario.

## Funcionalidades

- **Cantidad de vuelos por origen y destino**: Obtén el número total de vuelos entre un origen y un destino específicos.
- **Cantidad de vuelos por origen y fecha**: Recupera la cantidad de vuelos desde un aeropuerto seleccionado en una fecha específica.
- **Resumen estadístico por origen**: Genera resúmenes estadísticos (mínimo, máximo, promedio y desviación estándar) para cualquier variable, como distancia o retrasos, de vuelos que salgan desde un aeropuerto específico.
- **Resumen de retrasos por origen**: Obtén un resumen de los retrasos de vuelos desde un aeropuerto seleccionado basados en ciertos criterios.
- **Resumen acumulativo por criterio y fecha**: Consulta métricas acumulativas como el tiempo total de vuelo o la distancia recorrida en una fecha específica.
- **Consulta por número de cola (Tail Number)**: Cuenta la cantidad de vuelos realizados por un avión específico (identificado por su número de cola) desde uno o varios aeropuertos.
- **Consulta personalizada**: Identifica los aeropuertos y ciudades con mayor número de vuelos en una fecha específica.

## Tecnologías

- **Python 3.x**: Lenguaje de programación principal utilizado para construir la lógica y funcionalidad del proyecto.
- **Pandas**: Para la manipulación y el manejo eficiente de grandes conjuntos de datos.
- **Módulos personalizados**:
  - `necesidadCliente`: Contiene funciones auxiliares como convertir números de meses a nombres y calcular el estatus de retraso de vuelos.
  - `solicitudes`: Para manejar las entradas y consultas de los usuarios.
  - `autenticacion`: Para gestionar el inicio de sesión de los usuarios.

## Requisitos

Para ejecutar el proyecto, necesitas tener:

- Python 3.x instalado.
- Las siguientes bibliotecas de Python: 
  - `pandas`
  - Otras dependencias definidas en el proyecto (asegúrate de instalarlas a través de `requirements.txt` si aplica).

Puedes instalar las dependencias ejecutando:

```bash
pip install pandas

## Cómo Ejecutar

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener las dependencias requeridas instaladas.
3. Ejecuta el programa usando el siguiente comando en la terminal:

```bash
python main.py

4. Después de ejecutar el programa, se te mostrará un menú en el que podrás elegir entre diferentes opciones de consulta:
   - Opción **A**: Contar el número de vuelos según el origen y el destino.
   - Opción **B**: Contar el número de vuelos en una fecha específica.
   - Opción **C**: Generar resúmenes estadísticos (mínimo, máximo, promedio) para cualquier variable, como la distancia o el tiempo en el aire.
   - Opción **D**: Resumir los retrasos de los vuelos según el origen.
   - Opción **E**: Ver métricas acumulativas como el tiempo total de vuelo o la distancia recorrida en un día específico.
   - Opción **F**: Contar el número de vuelos realizados por un avión específico (por número de cola) desde un aeropuerto particular.
   - Opción **G**: Usar una consulta personalizada para encontrar aeropuertos y ciudades con la mayor cantidad de vuelos en un día específico.

5. Sigue las instrucciones en pantalla para ingresar datos como los códigos de aeropuerto, fechas o números de cola de los aviones.
