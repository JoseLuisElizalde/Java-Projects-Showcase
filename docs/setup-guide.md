### Guía de Configuración

# Prerequisitos

### Herramientas necesarias
- **Java JDK 11+** (Recomendado: JDK 17)
- **Maven 3.6+** o **Gradle 7+**
- **Git**
- **IDE Recomendado:**
    - IntelliJ IDEA (Community/Ultimate)
    - VS Code con extensiones Java
    - Eclipse IDE

### Verifica tu instalación
```bash
java -version
javac -version
mvn -v # o gradle -v
git --version
```


### Clonar el Repositorio

```
git clone https://github.com/tu-usuario/java-projects-showcase.git
cd java-projects-showcase
```

### Configuración del Entorno

#### 1. Configurar JDK en tu IDE

* **IntelliJ IDEA:** File -> Project Structure -> SDKs
* **VS Code:** Ctrl+Shift*P -> "Java:Configure Java Runtime"
* **Eclipse:** Window -> Preferencias -> Java -> Installed JREs

#### 2. Importar proyecto Maven/Gradle

Cada proyecto individual tiene su propio archivo de build.

### Estructura del Workspace

```text
java-projects-showcase/
├── proyectos/           # Todos los proyectos categorizados
│   ├── nivel-basico/   # Proyectos iniciales
│   ├── nivel-intermedio/
│   └── nivel-avanzado/
└── docs/               # Documentación
```

### Ejecutar un proyecto específico

```bash
# Ejemplo: Proyecto Calculator
cd proyectos/nivel-basico/calculator
mvn clean compile exec:java
# o
gradle run
```

### Test y Calida de Código

Ejecutar tests

```bash
mvn test
# o 
gradle test
```

Verificar estilo de código

```bash
mvn checkstyle:check
#o usando SpotBugs
mvn spotbugs:check
```

### Flujo de Trabajo Recomendado

1. Explora los proyectos por nivel de dificultad
2. Lee el README específico de cada proyecto
3. Configura el entorno según las necesidades del proyecto
4. Ejecuta los tests para verificar que todo funciona
5. Modifica y experimenta con el código

### Solución de Problemas Comunes

#### Error de dependencias Maven

```bash
mvn clean install -U
```

#### Problemas con Git

``` bash
# Si tienes conflictos de línea fina (CRLF vs LF)
git config --global core.autocrlf true # Windows
git config --global core.autocrlf input # Linux/Max
```

### Recursos Adicionales

* [JavaPage](https://docs.oracle.com/javase/)
* [MavenStarted](https://maven.apache.org/guides/getting-started/)
* [GradleManual](https://docs.gradle.org/current/userguide/userguide.html)

