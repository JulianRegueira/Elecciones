# Proyecto: "Simulación PASO 2023 - Voto electrónico"

## Descripción del Proyecto
En el colegio donde me encuentro trabajando me solicitaron una aplicación para simular la proxima jornada de las PASO en Argentina 2023, en la cúal los requisitos eran simples, que los chicos puedan entrar, seleccionar a un candidato y que los votos se vayan almacenando para hacer el posterior conteo.

## Objetivo
Enseñar a los chicos todos los pasos a seguir en una eleccion, se simulará la fizcalizacion, la delegación de sedes para votación y demás.

## Como se creó el proyecto
Esta realizado con Django y unos retoques visuales de CSS, sacando provecho de este Framework lo unico que se hizo fue crear una clase Candidato en la cual almacena 3 atributos, el ID, la imagen a mostrar y la cantidad de votos inicializada en cero.<br>

Como segundo paso se creó una funcion para llamarla al hacer click en la imagen y que simplemente sume un contador en la cantidad de votos del candidato seleccionado, realizando esos dos simples pasos y con algunos aportes visuales, se logró desarrollar el proyecto.

![elecciones](https://github.com/JulianRegueira/Elecciones/assets/130511226/5157477c-39f2-406d-819a-822f4e155e39)

## Estructura del Repositorio
- **Elecciones**: Contiene el proyecto, dentro de el creamos una app para trabajar sobre los candidatos de manera mas ordenada.
- **README.md**: Explicacion del mismo.

## Herramientas utilizadas en el Proyecto
- Python
- Django
- Modelo MVT
- HTML & CSS
