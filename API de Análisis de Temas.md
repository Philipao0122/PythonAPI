# API de Análisis de Temas

## Descripción

Esta API permite analizar diferentes temas académicos y extraer información estructurada en formato JSON. La API está diseñada para procesar temas de diversas facultades y devolver:

- **Conceptos clave**: Los conceptos más importantes del tema
- **Actores principales**: Las personas, organizaciones o entidades relevantes
- **Casos de estudio**: Ejemplos prácticos y casos reales
- **Futuro del tema**: Tendencias y desarrollos esperados

## Estructura del Proyecto

```
topic-analyzer-api/
├── src/
│   ├── main.py                    # Punto de entrada de la aplicación
│   ├── routes/
│   │   ├── topic_analyzer.py      # Blueprint principal con la lógica de análisis
│   │   └── user.py               # Blueprint de usuarios (template)
│   ├── models/                   # Modelos de base de datos
│   └── static/                   # Archivos estáticos
├── venv/                         # Entorno virtual
├── requirements.txt              # Dependencias
└── test_api.py                  # Script de pruebas
```

## Endpoints Disponibles

### 1. Health Check
**GET** `/api/topics/health`

Verifica que la API esté funcionando correctamente.

**Respuesta:**
```json
{
  "status": "OK",
  "message": "API de análisis de temas funcionando correctamente",
  "version": "1.0.0"
}
```

### 2. Analizar Tema Individual
**POST** `/api/topics/analyze`

Analiza un tema específico y devuelve información estructurada.

**Cuerpo de la solicitud:**
```json
{
  "topic": "desinformación",
  "sources": ["Journal of Strategic Studies", "NATO Strategic Communications"]
}
```

**Respuesta:**
```json
{
  "tema": "desinformación",
  "analisis": {
    "conceptos_clave": [
      "Guerra híbrida",
      "Desinformación",
      "Propaganda digital",
      "Operaciones de influencia",
      "Redes sociales como arma",
      "Narrativas falsas",
      "Manipulación de la opinión pública"
    ],
    "actores_principales": [
      "Estados-nación",
      "Agencias de inteligencia",
      "Grupos paramilitares",
      "Plataformas de redes sociales",
      "Medios de comunicación",
      "Organizaciones internacionales",
      "Sociedad civil"
    ],
    "casos_de_estudio": [
      "Interferencia electoral en Estados Unidos (2016)",
      "Brexit y campañas de desinformación",
      "Conflicto en Ucrania y guerra informativa",
      "Operaciones de influencia en África",
      "Desinformación durante COVID-19"
    ],
    "futuro_del_topic": [
      "Inteligencia artificial para generar deepfakes",
      "Automatización de campañas de desinformación",
      "Regulación internacional de la información",
      "Desarrollo de herramientas de verificación",
      "Mayor sofisticación en técnicas de manipulación"
    ],
    "fuentes": ["Journal of Strategic Studies", "NATO Strategic Communications"]
  }
}
```

### 3. Listar Temas Disponibles
**GET** `/api/topics/topics`

Obtiene la lista de todos los temas predefinidos en la base de datos.

**Respuesta:**
```json
{
  "temas_disponibles": [
    "desinformacion_guerra_hibrida",
    "regimenes_autoritarios",
    "conflictos_persistentes",
    "poder_global",
    "privacidad_digital",
    "criptoeconomia",
    "cambio_climatico",
    "inteligencia_artificial"
  ],
  "total": 8
}
```

### 4. Análisis en Lote
**POST** `/api/topics/analyze/batch`

Analiza múltiples temas de una vez.

**Cuerpo de la solicitud:**
```json
{
  "topics": [
    {
      "topic": "desinformación",
      "sources": ["Journal of Strategic Studies"]
    },
    {
      "topic": "inteligencia artificial",
      "sources": ["IEEE Standards"]
    }
  ]
}
```

**Respuesta:**
```json
{
  "resultados": [
    {
      "tema": "desinformación",
      "analisis": { ... }
    },
    {
      "tema": "inteligencia artificial", 
      "analisis": { ... }
    }
  ],
  "total_analizados": 2
}
```

## Temas Predefinidos

La API incluye análisis predefinidos para los siguientes temas:

### Ciencias Políticas
- **Desinformación y guerra híbrida**
- **Ascenso de regímenes autoritarios**
- **Conflictos persistentes** (Israel-Palestina, Ucrania-Rusia, Sáhara Occidental)
- **Reconfiguración del poder global** (China vs. EE.UU., BRICS+)

### Derecho
- **Privacidad digital vs. vigilancia estatal**
- **Reconocimiento de derechos a minorías**
- **Crímenes de guerra y justicia internacional**
- **Inteligencia artificial y responsabilidad legal**

### Ciencias Económicas
- **Criptoeconomía y regulación financiera**
- **Desigualdad económica post-pandemia**
- **Economía circular vs. crecimiento tradicional**
- **Políticas fiscales expansivas y deuda pública**

### Ciencias Naturales
- **Cambio climático y geoingeniería**
- **Edición genética con CRISPR**
- **Uso de energía nuclear vs. renovables**
- **Microplásticos y contaminación sistémica**

### Ingeniería
- **Desarrollo de Inteligencia Artificial General (AGI)**

## Instalación y Ejecución

### Requisitos
- Python 3.11+
- pip

### Pasos de instalación

1. **Clonar o descargar el proyecto**
```bash
cd topic-analyzer-api
```

2. **Activar el entorno virtual**
```bash
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
python src/main.py
```

La API estará disponible en `http://localhost:5002`

### Dependencias principales
- Flask 3.1.1
- Flask-CORS 6.0.0
- SQLAlchemy (para funcionalidad de base de datos)

## Características Técnicas

### Normalización de Temas
La API incluye un sistema inteligente de normalización que permite buscar temas usando diferentes variaciones:
- "desinformación" → "desinformacion_guerra_hibrida"
- "cripto" → "criptoeconomia"
- "clima" → "cambio_climatico"
- "AI" → "inteligencia_artificial"

### Análisis Dinámico
Para temas no predefinidos, la API genera automáticamente un análisis básico con estructura similar.

### CORS Habilitado
La API permite solicitudes desde cualquier origen, facilitando la integración con aplicaciones frontend.

### Manejo de Errores
Respuestas de error estructuradas con códigos HTTP apropiados y mensajes descriptivos.

## Ejemplos de Uso

### Usando curl

```bash
# Health check
curl -X GET http://localhost:5002/api/topics/health

# Analizar tema
curl -X POST http://localhost:5002/api/topics/analyze \
  -H "Content-Type: application/json" \
  -d '{"topic": "desinformación", "sources": ["Journal of Strategic Studies"]}'

# Listar temas
curl -X GET http://localhost:5002/api/topics/topics
```

### Usando Python requests

```python
import requests
import json

# Analizar tema
response = requests.post('http://localhost:5002/api/topics/analyze', 
                        json={
                            "topic": "inteligencia artificial",
                            "sources": ["IEEE Standards"]
                        })
result = response.json()
print(json.dumps(result, indent=2, ensure_ascii=False))
```

## Notas de Desarrollo

- La aplicación está configurada para ejecutarse en modo debug
- Escucha en todas las interfaces (0.0.0.0) para permitir acceso externo
- Incluye funcionalidad de base de datos SQLite (opcional)
- Estructura modular con blueprints para facilitar el mantenimiento

## Posibles Mejoras Futuras

1. **Integración con IA**: Usar modelos de lenguaje para análisis dinámico más sofisticado
2. **Base de datos**: Almacenar análisis y fuentes en base de datos
3. **Autenticación**: Agregar sistema de usuarios y API keys
4. **Cache**: Implementar cache para mejorar rendimiento
5. **Documentación interactiva**: Integrar Swagger/OpenAPI
6. **Análisis de texto**: Procesar documentos PDF y extraer información automáticamente

