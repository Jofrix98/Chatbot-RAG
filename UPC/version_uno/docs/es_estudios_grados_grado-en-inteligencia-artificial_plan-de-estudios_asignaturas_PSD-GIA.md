## Usted está aquí

[Inicio](/es) » [Estudios](/es/estudios) » [Grados](/es/estudios/grados) »
[Grado en Inteligencia Artificial](/es/estudios/grados/grado-en-inteligencia-
artificial) » [Plan de estudios](/es/estudios/grados/grado-en-inteligencia-
artificial/plan-de-estudios) » [Asignaturas](/es/estudios/grados/grado-en-
inteligencia-artificial/plan-de-estudios/asignaturas) » Paralelismo y Sistemas
Distribuidos

  * Profesorado
  * Horas semanales
  * Competencias
  * Objetivos
  * Contenidos
  * Actividades
  * Metodología docente
  * Método de evaluación
  * Bibliografía
  * Capacidades previas

**Créditos**

6

**Tipos**

Obligatoria

**Requisitos**

Esta asignatura no tiene requisitos, pero tiene capacidades previas

**Departamento**

AC

**Web**

\-

**Mail**

\-

Esta asignatura proporciona conocimientos básicos sobre: 1) los diferentes
niveles de paralelismo que podemos encontrar en las arquitecturas actuales (a
nivel de instrucciones o ILP, a nivel de datos o DLP ya nivel de flujo de
ejecución o TLP; 2) cómo la jerarquía de memoria se organiza para darles
soporte; y 3) los mecanismos que permiten explotarlos desde el punto de vista
de la programación de aplicaciones. Estos conocimientos permitirán entender
las oportunidades que ofrecen estas arquitecturas para hacer frente a las
necesidades de cálculo de la mayor parte de aplicaciones de inteligencia
artificial.

## Profesorado

### Responsable

  * **Eduard Ayguadé Parra ( )**

### Otros

  * Josep Lluís Berral García (  ) 

## Horas semanales

**Teoría**

2

**Problemas**

0

**Laboratorio**

2

**Aprendizaje dirigido**

0

**Aprendizaje autónomo**

6

## Competencias

### Competencias Transversales

#### Transversales

  * **CT3 [Avaluable]** \- Comunicación eficaz oral y escrita. Comunicarse de forma oral y escrita con otras personas sobre los resultados del aprendizaje, de la elaboración del pensamiento y de la toma de decisiones; participar en debates sobre temas de la propia especialidad. 
  * **CT6 [Avaluable]** \- Aprendizaje autónomo. Detectar deficiencias en el propio conocimiento y superarlas mediante la reflexión crítica y la elección de la mejor actuación para ampliar dicho conocimiento. 

### Competencias Técnicas

#### Específicas

  * **CE05** \- Analizar y evaluar la estructura y arquitectura de los computadores, así como los componentes básicos que los conforman. 
  * **CE07** \- Interpretar las características, funcionalidades y estructura de los Sistemas Distribuidos, las Redes de Computadores e Internet y diseñar e implementar aplicaciones basadas en ellas. 
  * **CE11** \- Identificar y aplicar los principios fundamentales y técnicas básicas de la programación paralela, concurrente, distribuida y de tiempo real. 

### Competencias Técnicas Genéricas

#### Genéricas

  * **CG2** \- Utilizar los conocimientos fundamentales y metodologías de trabajo sólidas adquiridos durante los estudios para adaptarse a los nuevos escenarios tecnológicos del futuro. 
  * **CG3** \- Definir, evaluar y seleccionar plataformas hardware y software para el desarrollo y la ejecución de sistemas, servicios y aplicaciones informáticas en el ámbito de la inteligencia artificial. 
  * **CG5** \- Trabajar en equipos y proyectos multidisciplinares relacionados con la inteligencia artificial y la robótica, interactuando fluidamente con ingenieros/as y profesionales de otras disciplinas. 
  * **CG9** \- Afrontar nuevos retos con una visión amplia de las posibilidades de la carrera profesional en el ámbito de la Inteligencia Artificial. Desarrollar la actividad aplicando criterios de calidad y mejora continua, y actuar con rigor en el desarrollo profesional. Adaptarse a los cambios organizativos o tecnológicos. Trabajar en situaciones de carencia de información y/o con restricciones temporales y/o de recursos. 

## Objetivos

  1. Conocer los modelos básicos de ejecución y las métricas rendimiento   
Competencias relacionadas: CE05,  
Subcompetences:

     * Herramientas para la caracterización de rendimiento
  2. Conocer la arquitectura de los procesadores escalares y las técnicas para explotar el ILP (paralelismo a nivel de instrucción) y el DLP (paralelismo a nivel de datos)   
Competencias relacionadas: CE05, CG3,  
Subcompetences:

     * Optimizaciónde la ejecución escalar: vectorización
  3. Conocer las arquitecturas de memoria compartida, soporte hardware a la coherencia de memoria y sincronización   
Competencias relacionadas: CE05, CG3,  
Subcompetences:

     * Programación paralela de memoria compartida: OpenMP
  4. Conocer las arquitecturas de memoria distribuida y el soporte hardware para el intercambio de datos   
Competencias relacionadas: CE05, CE07, CG3,  
Subcompetences:

     * Programación paralela con paso de mensajes: MPI
  5. Conocer las arquitecturas basadas en aceleradores y el acceso a la jerarquía de memoria del procesador escalar   
Competencias relacionadas: CE05, CG3,

  6. Conocer y aplicar las técnicas básicas de la programación paralela, para sistemas multiprocesador de memoria compartida y distribuida   
Competencias relacionadas: CT6, CE11,

  7. Capacidades para discutir y contrastar la resolución de problemas y ejercicios prácticos, tanto en trabajo de grupo como de forma autónoma   
Competencias relacionadas: CT6, CT3,

  8. Entender la relación de la asignatura con el campo de la IA   
Competencias relacionadas: CG2, CG5, CG9,

## Contenidos

  1. Modelos de ejecución y métricas de rendimiento   
Presentación de los modelos de ejecución serie, multiprogramado, concurrente y
paralelo, junto a las métricas básicas que caracterizan su rendimiento.

  2. Arquitectura del procesador escalar y optimización de código   
En este tema se presenta la arquitectura básica del procesador escalar y las
técnicas para incrementar el paralelismo a nivel de instrucciones (ILP: diseño
segmentado y superescalar) y a nivel de datos (DLP: unidades vectoriales).
Optimización del acceso a la jerarquía de memoria y vectorización.

  3. Arquitectura y programación de multiprocesadores de memoria compartida   
En este tema se presentan las arquitecturas multiprocesador de memoria
compartida UMA (uniform memory access time) y NUMA (non-uniform memory access
time), incluyendo los mecanismos de coherencia basados en bus y directorio y
el soporte a la sincronización mediante instrucciones atómicas. También se
presenta la arquitectura de un nodo dentro de una arquitectura cluster y los
componentes que lo forman (procesadores con múltiples núcleos de ejecución,
memoria y buses). Paralelización de aplicaciones usando el modelo de tareas en
OpenMP.

  4. Arquitectura y programación de multiprocesadores de memoria distribuida   
En este tema se presentan las arquitecturas multiprocesador de memoria
distribuida basadas en paso de mensajes a través de una red de interconexión
escalable. Paralelización de aplicaciones con el modelo de programación MPI.

  5. Aceleración para aplicaciones de inteligencia artificial   
En este tema se presentan las arquitecturas destinadas a acelerar los núcleos
de cómputo más característicos en aplicaciones de inteligencia artificial: GPU
(Graphics Processing Units), TPU (Tensor Processing Units),... y su
integración en los nodos de memoria compartida de una arquitectura de clúster.
Caso de uso: aceleradores para entornos de Deep Learning.

## Actividades

Actividad Acto evaluativo

  

### Modelos de ejecución, métricas y herramientas para el análisis de
rendimiento

\-  
**Objetivos:** 1 7  
**Contenidos:**

  * 1 . Modelos de ejecución y métricas de rendimiento

**Teoría**

4h

**Problemas**

0h

**Laboratorio**

4h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

6h

  

### Arquitectura del procesador escalar y optimización de aplicaciones

\-  
**Objetivos:** 2 7  
**Contenidos:**

  * 2 . Arquitectura del procesador escalar y optimización de código

**Teoría**

6h

**Problemas**

0h

**Laboratorio**

4h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

10h

  

### Arquitectura multiprocesador de memoria compartida y programación OpenMP

\-  
**Objetivos:** 3 7 8 6  
**Contenidos:**

  * 3 . Arquitectura y programación de multiprocesadores de memoria compartida

**Teoría**

8h

**Problemas**

0h

**Laboratorio**

8h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

14h

  

### OpenMP tutorial

\-  
**Objetivos:** 3  
**Contenidos:**

  * 3 . Arquitectura y programación de multiprocesadores de memoria compartida

**Teoría**

0h

**Problemas**

0h

**Laboratorio**

2h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

2h

  

### Control teoria

  
**Objetivos:** 1 2  
**Semana:** 6  

**Teoría**

2h

**Problemas**

0h

**Laboratorio**

0h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

10h

  

### Arquitectura multiprocesador de memoria distribuida y programación MPI

\-  
**Objetivos:** 4 7 8 6  
**Contenidos:**

  * 4 . Arquitectura y programación de multiprocesadores de memoria distribuida

**Teoría**

4h

**Problemas**

0h

**Laboratorio**

8h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

12h

  

### MPI tutorial

\-  
**Objetivos:** 4  
**Contenidos:**

  * 4 . Arquitectura y programación de multiprocesadores de memoria distribuida

**Teoría**

0h

**Problemas**

0h

**Laboratorio**

2h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

2h

  

### Arquitectura de aceleradores por aplicaciones de inteligencia artificial

\-  
**Objetivos:** 7 8 5 6  
**Contenidos:**

  * 5 . Aceleración para aplicaciones de inteligencia artificial

**Teoría**

4h

**Problemas**

0h

**Laboratorio**

0h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

6h

  

### Examen final

  
**Objetivos:** 1 2 3 4 5  
**Semana:** 15 (Fuera de horario lectivo)  

**Teoría**

2h

**Problemas**

0h

**Laboratorio**

0h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

20h

  

### Control de laboratorio

  
**Objetivos:** 6  
**Semana:** 14  

**Teoría**

0h

**Problemas**

0h

**Laboratorio**

2h

**Aprendizaje dirigido**

0h

**Aprendizaje autónomo**

8h

  

## Metodología docente

El curso se basa en sesiones de teoría y laboratorio presenciales. Las
sesiones teóricas combinan clases magistrales con la resolución de ejercicios
siguiendo el programa expuesto en este plan de estudios y usando material
propio (transparencias, enunciados de problemas, ...). Durante las sesiones,
se promueve el diálogo y la discusión para anticipar y consolidar los
resultados de aprendizaje de la asignatura.  
  
Las sesiones de laboratorio tratan los aspectos relacionados con la
programación y siguen los mismos temas del plan de estudios. Son sesiones
prácticas utilizando una arquitectura cluster disponible en el Departamento de
Arquitectura de Computadores.

## Método de evaluación

Hay dos pruebas evaluativas de la parte de teoría y una de la parte de
laboratorio:  
\- PT: examen parcial de teoría (20%)  
\- FT: examen final de teoría (35%)  
\- FL: examen final de laboratorio (30%)  
  
Adicionalmente, se evaluarán de forma continua:  
\- SL: informes de seguimiento del laboratorio (15%) que también servirá para
evaluar las competencias transversales CT3 y CT6.  
  
La Nota Final (NF) de la asignatura se obtiene a partir de  
NF = (0.30 x FL + 0.15 x SL) + MAX(0.55 x FT; (0.20 x PT + 0.35 x FT))  
  
En caso de NF < 5.0 pero superior a 3.5 habiendo realizado las dos partes del
examen final, existirá la opción de reevaluación mediante un examen que
recogerá toda la asignatura (teoría y prácticas). La nota del examen de
reevaluación reemplazará la nota NF, cuyo valor no podrá ser mayor de 7.

## Bibliografía

### Básica:

  * **Computer organization and design: the hardware/software interface** \- Patterson, David A and Hennessy, John L, Morgan Kaufmann, 2017. ISBN: 9780128017333   
[https://discovery.upc.edu/discovery/fulldisplay?docid=alma991004094079706711&context;=L&vid;=34CSUC_UPC:VU1⟨=ca](https://discovery.upc.edu/discovery/fulldisplay?docid=alma991004094079706711&context=L&vid=34CSUC_UPC:VU1&lang=ca)

  * **Computer architecture: a quantitative approach** \- Hennessy, John L. and Patterson, David A., Morgan Kaufmann, 2019. ISBN: 9780128119051   
[https://discovery.upc.edu/discovery/fulldisplay?docid=alma991004117509706711&context;=L&vid;=34CSUC_UPC:VU1⟨=ca](https://discovery.upc.edu/discovery/fulldisplay?docid=alma991004117509706711&context=L&vid=34CSUC_UPC:VU1&lang=ca)

## Capacidades previas

Las adquiridas en la asignatura de Fundamentos de Computadores (FC) que
conceptualmente precede a esta asignatura.

## Dónde estamos

Edificio B6 del Campus Nord  
C/Jordi Girona Salgado,1-3  
08034 BARCELONA España  
Tel: (+34) 93 401 70 00

[informacio@fib.upc.edu](mailto:informacio@fib.upc.edu)

  * [__](/es/noticies/rss.rss)
  * [__](https://www.facebook.com/fib.upc)
  * [__](https://twitter.com/fib_upc)
  * [__](https://www.flickr.com/photos/fib-upc/albums)
  * [__](https://www.youtube.com/user/mediafib)
  * [__](https://www.instagram.com/fib.upc/)

[![](/sites/fib/files/images/banner-suport-
fib.jpg)](http://suport.fib.upc.edu)

## Contacta con la FIB

Su nombre *

Su dirección de correo electrónico *

Asunto *

Categoría * \- Por favor, elija -Aulas, equipos y servicios informáticosBuzon
de sugerenciasFelicitacionesInformación AcadémicaInformación de
movilidadInformación de los másteresInformación general de la FIBNoticias al
web de la FIBQuejas

Mensaje *

Leave this field blank

© Facultat d'Informàtica de Barcelona - Universitat Politècnica de Catalunya -
[Avíso legal sobre esta web](/es/aviso-legal-sobre-esta-web) \- Configuración
de privacidad

