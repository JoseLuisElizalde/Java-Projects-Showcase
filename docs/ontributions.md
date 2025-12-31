
## Guía de Contribuciones


# Guía de Contribución

¡Gracias por tu interés en contribuir a este repositorio de proyectos Java! 🎉

## ¿Cómo puedo contribuir?

### 1. Reportar Bugs
- Usa el template de issue para bugs
- Describe el problema claramente
- Incluye pasos para reproducirlo
- Muestra el comportamiento esperado vs actual

### 2. Sugerir Mejoras
- Usa el template de feature request
- Explica el beneficio de la mejora
- Proporciona ejemplos si es posible

### 3. Mejorar Documentación
- Corregir errores tipográficos
- Agregar ejemplos más claros
- Mejorar traducciones
- Añadir mejores prácticas

### 4. Agregar Nuevos Proyectos
- Sigue la estructura existente
- Incluye documentación completa
- Añade tests
- Mantén la calidad del código

## Flujo de Trabajo para Contribuciones

### Paso 1: Fork del Repositorio
1. Haz fork del proyecto en GitHub
2. Clona tu fork localmente:
```bash
git clone https://github.com/JoseLuisElizalde/java-projects-showcase.git
```

### Paso 2: Crear una Rama

```bash
git checkout -b tipo-descripcion
# Ejemplos:
# git checkout -b fix/calculator-division-zero
# git checkout -b feat/add-new-algorithm-project
# git checkout -b docs/improve-setup-guide
```


### Paso 3: Hacer los Cambios

* Sigue las convenciones de código

* Añade tests para nuevas funcionalidades

* Actualiza la documentación

* Verifica que todo compile correctamente


### Paso 4: Commits Claros

```bash
git add .
git commit -m "tipo(ámbito): descripción breve

Descripción más detallada si es necesario.

Fixes #123"  # Referencia issues si aplica
```

Convención de commits:

* ``feat:`` Nueva funcionalidad

* ``fix:`` Corrección de bug

* ``docs:`` Cambios en documentación

* ``style:`` Formato, puntos y coma, etc.

* ``refactor:`` Refactorización de código

* ``test:`` Añadir o corregir tests

* ``chore:`` Cambios en build, dependencias, etc.


### Paso 5: Sincronizar con Upstream

```bash
git fetch upstream
git merge upstream/main
# Resuelve conflictos si los hay
```

### Paso 6: Push y Pull Request

```bash
git push origin tu-rama
```

1. Ve a tu repositorio en GitHub

2. Haz clic en "Compare & pull request"

3. Completa el template del PR

4. Espera la revisión

## Estructura para Nuevos Proyectos

### Requisitos mínimos

```text
proyectos/
└── nivel-xxx/
    └── nombre-proyecto/
        ├── src/
        │   ├── main/java/
        │   └── test/java/
        ├── README.md          # Documentación específica
        ├── pom.xml            # o build.gradle
        ├── .gitignore
        └── LICENSE            # Si aplica
```

### Contenido del README del proyecto

```markdown
# Nombre del Proyecto

## 📖 Descripción
[Explicación clara del proyecto]

## 🎯 Objetivos de Aprendizaje
- [ ] Concepto 1
- [ ] Concepto 2
- [ ] Concepto 3

## 🛠️ Tecnologías Utilizadas
- Java X
- Librería Y
- Herramienta Z

## 🚀 Cómo Ejecutar
[Instrucciones específicas]

## 📁 Estructura del Proyecto
[Explicación de paquetes/clases]

## 🧪 Ejecutar Tests
[Comandos específicos]

## 📚 Recursos
[Enlaces útiles]
```

## Criterios de Aceptación
### Para nuevos proyectos:

* Código compila sin errores

* Tests pasan exitosamente

* Documentación completa en README.md

* Ejemplos claros y comentarios

* Seguimiento de convenciones de código

* Archivos de configuración correctos

### Para correcciones:

* Issue referenciado

* Tests actualizados/agregados

* No rompe funcionalidad existente

* Código revisado por linters


### Convenciones de Código
#### Estilo Java

* Sigue Google Java Style Guide

* Usa nombres descriptivos en inglés

* Comenta código complejo

* Mantén métodos cortos y enfocados

#### Estructura de Paquetes

```text
com.tuproyecto.
├── controller/    # Controladores
├── service/       # Lógica de negocio
├── repository/    # Acceso a datos
├── model/         # Entidades/DTOs
└── util/          # Utilidades
```

### Testing

* Usa JUnit 5

* Escribe tests significativos

* Cubre casos edge

* Mockea dependencias externas

### Revisión de Código
#### Como revisor:

* Sé constructivo y respetuoso

* Enfócate en el código, no en la persona

* Sugiere alternativas cuando critiques

* Revisa dentro de 48 horas si es posible

#### Como autor:

* Responde a todos los comentarios

* Acepta críticas constructivas

* Aprende de cada revisión

* Agradece el tiempo de los revisores

### Licencia

Al contribuir, aceptas que tu código será licenciado bajo la MIT License.

### Reconocimiento

Todos los contribuidores serán listados en el archivo CONTRIBUTORS.md del proyecto.

### Preguntas Frecuentes

**¿Necesito experiencia previa?**
¡No! Proyectos para todos los niveles son bienvenidos.

**¿Cómo empiezo si soy nuevo?**
Revisa los proyectos en nivel-basico/ y elige uno para mejorar.

**¿Puedo agregar proyectos de otras tecnologías?**
Este repositorio es específico para Java, pero se aceptan herramientas relacionadas (Spring, Hibernate, etc.).