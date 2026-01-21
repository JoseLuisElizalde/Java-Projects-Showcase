#!/usr/bin/env python3
"""
Script para actualizar automáticamente las tablas de proyectos en README.md
reemplazando las tablas dentro de las secciones <details> existentes.
"""

import os
import re
from pathlib import Path

def get_project_structure(base_path="proyectos"):
    """Recorre la estructura de directorios y obtiene información de proyectos."""
    projects = {
        "avanzado": [],
        "intermedio": [],
        "basico": []
    }
    
    base_dir = Path(base_path)
    
    if not base_dir.exists():
        return projects
    
    # Mapeo de niveles
    level_map = {
        "nivel-avanzado": "avanzado",
        "nivel-intermedio": "intermedio",
        "nivel-basico": "basico"
    }
    
    level_config = {
        "avanzado": {
            "emoji": "🟢",
            "name": "Nivel Avanzado",
            "default_tech": "Spring Boot, Docker, PostgreSQL",
            "has_status": True
        },
        "intermedio": {
            "emoji": "🟡",
            "name": "Nivel Intermedio",
            "default_tech": "Spring Boot, JPA, H2",
            "has_status": True
        },
        "basico": {
            "emoji": "🔵",
            "name": "Nivel Básico",
            "default_tech": "Java, JUnit",
            "has_status": False  # El nivel básico no tiene columna de estado
        }
    }
    
    for level_dir in base_dir.iterdir():
        if level_dir.is_dir():
            level_name = level_dir.name
            level_key = level_map.get(level_name)
            
            if not level_key:
                continue
            
            config = level_config[level_key]
            
            # Buscar proyectos en este nivel
            for project_dir in level_dir.iterdir():
                if project_dir.is_dir() and not project_dir.name.startswith('.'):
                    project_name = project_dir.name
                    
                    # Ignorar directorios comunes
                    if project_name in ['target', '.mvn', '.git', '.idea']:
                        continue
                    
                    # Extraer número y nombre (ej: "1.hello-world")
                    match = re.match(r'^(\d+)\.(.+)$', project_name)
                    if match:
                        number = match.group(1)
                        raw_name = match.group(2)
                        name = raw_name.replace('-', ' ').title()
                        
                        # Verificar si tiene pom.xml o archivos Java
                        is_maven = (project_dir / "pom.xml").exists()
                        java_files = list(project_dir.glob("**/*.java"))
                        has_java = len(java_files) > 0
                        
                        if is_maven or has_java:
                            # Obtener descripción del proyecto
                            description = get_project_description(project_dir, raw_name)
                            
                            # Determinar tecnologías
                            tech = determine_technologies(project_dir, config["default_tech"])
                            
                            # Determinar estado
                            if config["has_status"]:
                                estado = get_project_status(project_dir)
                                project_info = {
                                    "number": int(number),
                                    "name": name,
                                    "raw_name": raw_name,
                                    "folder": project_name,
                                    "path": f"{base_path}/{level_name}/{project_name}",
                                    "description": description,
                                    "technologies": tech,
                                    "status": estado
                                }
                            else:
                                project_info = {
                                    "number": int(number),
                                    "name": name,
                                    "raw_name": raw_name,
                                    "folder": project_name,
                                    "path": f"{base_path}/{level_name}/{project_name}",
                                    "description": description,
                                    "technologies": tech
                                }
                            
                            projects[level_key].append(project_info)
    
    # Ordenar por número
    for level in projects:
        projects[level].sort(key=lambda x: x["number"])
    
    return projects, level_config

def get_project_description(project_dir, raw_name):
    """Obtiene la descripción del proyecto."""
    # Mapeo de descripciones conocidas
    description_map = {
        "hello-world": "Primer programa en Java",
        "converter": "Conversor de unidades básico",
        "calculator": "Calculadora con interfaz gráfica",
        "api-rest": "API CRUD para gestión de usuarios",
        "ecommerce": "API RESTful completa con microservicios",
        "task-manager": "Gestor de tareas con WebSocket"
    }
    
    # Primero intentar con el mapeo
    if raw_name in description_map:
        return description_map[raw_name]
    
    # Intentar leer README del proyecto
    readme_path = project_dir / "README.md"
    if readme_path.exists():
        try:
            content = readme_path.read_text(encoding='utf-8', errors='ignore')
            # Buscar la primera línea después del título
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip().startswith('# '):
                    for j in range(i+1, min(i+4, len(lines))):
                        next_line = lines[j].strip()
                        if next_line and not next_line.startswith('#'):
                            # Limitar longitud
                            if len(next_line) > 100:
                                next_line = next_line[:97] + "..."
                            return next_line
        except:
            pass
    
    # Generar descripción basada en palabras clave
    keywords = {
        "hello": "Primer programa en Java",
        "hola": "Primer programa en Java",
        "converter": "Conversor de unidades",
        "conversor": "Conversor de unidades",
        "calculator": "Calculadora",
        "calculadora": "Calculadora",
        "api": "API REST",
        "rest": "API REST",
        "ecommerce": "Sistema de comercio electrónico",
        "commerce": "Sistema de comercio",
        "task": "Gestor de tareas",
        "tarea": "Gestor de tareas",
        "manager": "Sistema de gestión",
        "gestor": "Sistema de gestión"
    }
    
    for keyword, desc in keywords.items():
        if keyword in raw_name.lower():
            return desc
    
    # Descripción genérica
    return f"Proyecto {raw_name.replace('-', ' ')}"

def determine_technologies(project_dir, default_tech):
    """Determina las tecnologías usadas en un proyecto."""
    tecnologias = []
    
    # Verificar si es proyecto Maven
    pom_path = project_dir / "pom.xml"
    if pom_path.exists():
        try:
            pom_content = pom_path.read_text(encoding='utf-8', errors='ignore')
            
            # Buscar versión de Java en pom.xml
            java_version_match = re.search(r'<maven\.compiler\.(?:source|release)>(.*?)</', pom_content)
            if java_version_match:
                java_version = java_version_match.group(1)
                tecnologias.append(f"Java {java_version}")
            
            # Buscar tecnologías específicas
            tech_indicators = {
                r'<artifactId>spring-boot': 'Spring Boot',
                r'<artifactId>spring-': 'Spring',
                r'<artifactId>junit': 'JUnit',
                r'<artifactId>javafx': 'JavaFX',
                r'<artifactId>swing': 'Swing',
                r'<artifactId>postgresql': 'PostgreSQL',
                r'<artifactId>mysql': 'MySQL',
                r'<artifactId>h2': 'H2',
                r'<artifactId>jpa': 'JPA',
                r'<artifactId>websocket': 'WebSocket',
                r'<artifactId>docker': 'Docker'
            }
            
            for pattern, tech_name in tech_indicators.items():
                if re.search(pattern, pom_content, re.IGNORECASE):
                    if tech_name not in tecnologias:
                        tecnologias.append(tech_name)
                        
        except:
            pass
    
    # Si no se encontró versión de Java en pom.xml, buscar en archivos
    if not any(t.startswith("Java") for t in tecnologias):
        java_files = list(project_dir.glob("**/*.java"))
        if java_files:
            java_version = get_java_version(java_files[0])
            tecnologias.insert(0, f"Java {java_version}")
    
    # Verificar si tiene Dockerfile
    if (project_dir / "Dockerfile").exists() or list(project_dir.glob("docker-compose*")):
        if "Docker" not in tecnologias:
            tecnologias.append("Docker")
    
    # Verificar si tiene Maven pero no se detectó
    if pom_path.exists() and "Maven" not in tecnologias:
        tecnologias.append("Maven")
    
    # Si no se encontraron tecnologías específicas, usar las por defecto
    if not tecnologias:
        return default_tech
    
    # Filtrar duplicados
    unique_tech = []
    for tech in tecnologias:
        if tech not in unique_tech:
            unique_tech.append(tech)
    
    # Poner Java al principio si existe
    java_tech = [t for t in unique_tech if t.startswith("Java")]
    other_tech = [t for t in unique_tech if not t.startswith("Java")]
    
    final_tech = []
    if java_tech:
        final_tech.append(java_tech[0])
    final_tech.extend(other_tech)
    
    return ', '.join(final_tech)

def get_java_version(java_file):
    """Intenta determinar la versión de Java."""
    try:
        content = java_file.read_text(encoding='utf-8', errors='ignore')
        # Buscar en comentarios o líneas específicas
        lines = content.split('\n')
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in ['java 21', 'jdk 21', 'version 21']):
                return "21"
            elif any(keyword in line_lower for keyword in ['java 17', 'jdk 17', 'version 17']):
                return "17"
            elif any(keyword in line_lower for keyword in ['java 11', 'jdk 11', 'version 11']):
                return "11"
            elif any(keyword in line_lower for keyword in ['java 8', 'jdk 8', 'version 8', '1.8']):
                return "8"
    except:
        pass
    return "11"  # Versión por defecto

def get_project_status(project_dir):
    """Determina el estado del proyecto."""
    # Verificar si tiene README completo
    readme_path = project_dir / "README.md"
    if readme_path.exists():
        try:
            content = readme_path.read_text(encoding='utf-8', errors='ignore')
            # Si el README tiene contenido sustancial, considerarlo completo
            lines = [l.strip() for l in content.split('\n') 
                     if l.strip() and not l.strip().startswith('#')]
            if len(lines) > 5:  # Más de 5 líneas de contenido
                return "✅ Completo"
        except:
            pass
    
    # Verificar si tiene tests ejecutables
    test_files = list(project_dir.glob("**/test/**/*.java")) or list(project_dir.glob("**/*Test.java"))
    if test_files:
        # Verificar si hay pom.xml con dependencias de test
        pom_path = project_dir / "pom.xml"
        if pom_path.exists():
            try:
                pom_content = pom_path.read_text(encoding='utf-8', errors='ignore')
                if "junit" in pom_content.lower() or "test" in pom_content.lower():
                    return "🔧 Con pruebas"
            except:
                pass
        return "🔧 Con pruebas"
    
    # Verificar si tiene código fuente
    main_files = list(project_dir.glob("**/main/**/*.java")) or list(project_dir.glob("**/*.java"))
    if main_files:
        return "🔄 En progreso"
    
    return "📅 Planeado"

def generate_table_for_level(projects, level_key, config):
    """Genera solo la tabla (sin details) para un nivel."""
    if not projects:
        if config["has_status"]:
            return "| Proyecto | Descripción | Tecnologías | Estado |\n|----------|-------------|-------------|--------|\n"
        else:
            return "| Proyecto | Descripción | Tecnologías |\n|----------|-------------|-------------|\n"
    
    # Encabezado de tabla
    if config["has_status"]:
        table = "| Proyecto | Descripción | Tecnologías | Estado |\n"
        table += "|----------|-------------|-------------|--------|\n"
    else:
        table = "| Proyecto | Descripción | Tecnologías |\n"
        table += "|----------|-------------|-------------|\n"
    
    # Filas de la tabla
    for project in projects:
        project_link = f"[{project['name']}]({project['path']})"
        
        if config["has_status"]:
            table += f"| {project_link} | {project['description']} | {project['technologies']} | {project['status']} |\n"
        else:
            table += f"| {project_link} | {project['description']} | {project['technologies']} |\n"
    
    return table

def update_readme():
    """Actualiza el README.md reemplazando las tablas dentro de los details."""
    # Obtener estructura de proyectos
    projects, level_config = get_project_structure()
    
    print(f"📁 Proyectos encontrados:")
    for level in ["avanzado", "intermedio", "basico"]:
        print(f"  {level_config[level]['emoji']} {level}: {len(projects[level])} proyectos")
    
    # Leer README existente
    with open("README.md", 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Actualizar cada sección <details> individualmente
    for level_key in ["avanzado", "intermedio", "basico"]:
        config = level_config[level_key]
        emoji = config["emoji"]
        level_name = config["name"]
        
        # Buscar la sección específica
        details_pattern = rf'<details>\s*<summary><strong>{re.escape(emoji)}\s*{re.escape(level_name)}</strong></summary>.*?</details>'
        
        match = re.search(details_pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            print(f"\n🔍 Encontrada sección: {level_name}")
            
            # Generar nueva tabla
            new_table = generate_table_for_level(projects[level_key], level_key, config)
            
            # Construir el nuevo contenido de details
            new_details = f'<details>\n<summary><strong>{emoji} {level_name}</strong></summary>\n\n{new_table}\n</details>'
            
            # Reemplazar en el contenido
            content = content[:match.start()] + new_details + content[match.end():]
            
            print(f"  ✅ Actualizada: {len(projects[level_key])} proyectos")
        else:
            print(f"\n⚠️  No se encontró la sección: {level_name}")
            
            # Intentar buscar sin el emoji
            alt_pattern = rf'<details>\s*<summary><strong>.*?{re.escape(level_name)}</strong></summary>.*?</details>'
            match = re.search(alt_pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                print(f"  🔍 Encontrada sección alternativa")
                
                # Generar nueva tabla
                new_table = generate_table_for_level(projects[level_key], level_key, config)
                
                # Construir el nuevo contenido de details
                new_details = f'<details>\n<summary><strong>{emoji} {level_name}</strong></summary>\n\n{new_table}\n</details>'
                
                # Reemplazar en el contenido
                content = content[:match.start()] + new_details + content[match.end():]
                
                print(f"  ✅ Actualizada: {len(projects[level_key])} proyectos")
            else:
                print(f"  ❌ No se pudo encontrar la sección, se creará nueva")
                
                # Buscar donde insertar (después de "###  **Proyectos**")
                projects_section = "###  **Proyectos**"
                projects_pos = content.find(projects_section)
                
                if projects_pos != -1:
                    # Buscar el final de la sección de proyectos
                    next_section = content.find("### ", projects_pos + len(projects_section))
                    if next_section == -1:
                        next_section = len(content)
                    
                    # Generar nueva sección
                    new_table = generate_table_for_level(projects[level_key], level_key, config)
                    new_details = f'\n\n<details>\n<summary><strong>{emoji} {level_name}</strong></summary>\n\n{new_table}\n</details>'
                    
                    # Insertar antes de la siguiente sección
                    content = content[:next_section] + new_details + content[next_section:]
                    
                    print(f"  ✅ Creada nueva sección con {len(projects[level_key])} proyectos")
    
    # Eliminar cualquier sección duplicada fuera de los details
    print("\n🧹 Limpiando secciones duplicadas...")
    
    # Buscar y eliminar secciones como "####  **Nivel Básico**" que están fuera de details
    pattern = r'\n####\s+\*\*Nivel\s+(?:Avanzado|Intermedio|Básico)\*\*.*?(?=\n####|\n###|\Z)'
    content = re.sub(pattern, '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Escribir README actualizado
    with open("README.md", 'w', encoding='utf-8') as file:
        file.write(content)
    
    print("\n✅ README.md actualizado exitosamente!")
    
    # Mostrar resumen final
    print("\n📊 Resumen final:")
    total = 0
    for level in ["avanzado", "intermedio", "basico"]:
        count = len(projects[level])
        total += count
        print(f"  {level_config[level]['emoji']} {level_config[level]['name']}: {count} proyectos")
    print(f"  📈 Total: {total} proyectos")

def main():
    """Función principal."""
    try:
        print("🔄 Iniciando actualización del README...")
        update_readme()
        
        print("\n📝 Instrucciones:")
        print("   Para ver los cambios: git diff README.md")
        print("   Para aceptar cambios: git add README.md")
        print('                    git commit -m "Actualizar proyectos automáticamente"')
        print("                    git push")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())