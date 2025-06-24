from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
import re
import json

topic_analyzer_bp = Blueprint('topic_analyzer', __name__)

class TopicAnalyzer:
    def __init__(self):
        # Base de datos de temas con información predefinida
        self.topics_data = {
            "desinformacion_guerra_hibrida": {
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
                ]
            },
            "regimenes_autoritarios": {
                "conceptos_clave": [
                    "Autoritarismo digital",
                    "Personalización del poder",
                    "Represión política",
                    "Control de medios",
                    "Vigilancia masiva",
                    "Erosión democrática",
                    "Populismo autoritario"
                ],
                "actores_principales": [
                    "Líderes autoritarios",
                    "Aparatos de seguridad",
                    "Oligarquías económicas",
                    "Partidos únicos",
                    "Organizaciones internacionales",
                    "Sociedad civil opositora",
                    "Comunidad internacional"
                ],
                "casos_de_estudio": [
                    "China y el sistema de crédito social",
                    "Rusia bajo Putin",
                    "Hungría y la democracia iliberal",
                    "Venezuela y el chavismo",
                    "Myanmar y el golpe militar"
                ],
                "futuro_del_topic": [
                    "Tecnologías de vigilancia más avanzadas",
                    "Cooperación entre regímenes autoritarios",
                    "Resistencia digital y ciberactivismo",
                    "Sanciones internacionales más efectivas",
                    "Nuevas formas de represión tecnológica"
                ]
            },
            "conflictos_persistentes": {
                "conceptos_clave": [
                    "Conflictos congelados",
                    "Resolución de conflictos",
                    "Mediación internacional",
                    "Territorios disputados",
                    "Refugiados y desplazados",
                    "Violaciones de derechos humanos",
                    "Seguridad regional"
                ],
                "actores_principales": [
                    "Estados en conflicto",
                    "Organizaciones internacionales",
                    "Mediadores internacionales",
                    "Grupos armados",
                    "Población civil",
                    "Países vecinos",
                    "Potencias regionales"
                ],
                "casos_de_estudio": [
                    "Conflicto israelí-palestino",
                    "Guerra en Ucrania",
                    "Sáhara Occidental",
                    "Cachemira",
                    "Chipre dividido"
                ],
                "futuro_del_topic": [
                    "Nuevos mecanismos de mediación",
                    "Impacto del cambio climático en conflictos",
                    "Tecnología en la resolución de conflictos",
                    "Justicia transicional mejorada",
                    "Prevención de conflictos basada en IA"
                ]
            },
            "poder_global": {
                "conceptos_clave": [
                    "Multipolaridad",
                    "Hegemonía declinante",
                    "Bloques geopolíticos",
                    "Guerra comercial",
                    "Competencia tecnológica",
                    "Alianzas estratégicas",
                    "Orden mundial emergente"
                ],
                "actores_principales": [
                    "Estados Unidos",
                    "China",
                    "Unión Europea",
                    "Rusia",
                    "BRICS+",
                    "Organizaciones multilaterales",
                    "Corporaciones multinacionales"
                ],
                "casos_de_estudio": [
                    "Guerra comercial EE.UU.-China",
                    "Expansión de BRICS+",
                    "Iniciativa de la Franja y la Ruta",
                    "Competencia en semiconductores",
                    "Alianzas en el Indo-Pacífico"
                ],
                "futuro_del_topic": [
                    "Desacoplamiento económico selectivo",
                    "Nuevas instituciones financieras globales",
                    "Competencia en tecnologías emergentes",
                    "Fragmentación del internet global",
                    "Reconfiguración de cadenas de suministro"
                ]
            },
            "privacidad_digital": {
                "conceptos_clave": [
                    "Vigilancia masiva",
                    "Protección de datos",
                    "Encriptación",
                    "Anonimato digital",
                    "Derechos digitales",
                    "Capitalismo de vigilancia",
                    "Soberanía digital"
                ],
                "actores_principales": [
                    "Gobiernos nacionales",
                    "Agencias de inteligencia",
                    "Grandes tecnológicas",
                    "Activistas digitales",
                    "Reguladores",
                    "Ciudadanos",
                    "Organizaciones de derechos humanos"
                ],
                "casos_de_estudio": [
                    "GDPR en Europa",
                    "Programa PRISM de NSA",
                    "Sistema de crédito social chino",
                    "Caso Snowden",
                    "Regulación de Big Tech"
                ],
                "futuro_del_topic": [
                    "Computación cuántica y criptografía",
                    "IA para análisis de comportamiento",
                    "Regulación global de datos",
                    "Tecnologías de preservación de privacidad",
                    "Identidad digital descentralizada"
                ]
            },
            "criptoeconomia": {
                "conceptos_clave": [
                    "Blockchain",
                    "Descentralización financiera",
                    "Monedas digitales de bancos centrales",
                    "DeFi",
                    "Tokenización",
                    "Smart contracts",
                    "Regulación cripto"
                ],
                "actores_principales": [
                    "Bancos centrales",
                    "Reguladores financieros",
                    "Exchanges de criptomonedas",
                    "Desarrolladores blockchain",
                    "Inversores institucionales",
                    "Usuarios retail",
                    "Gobiernos"
                ],
                "casos_de_estudio": [
                    "El Salvador y Bitcoin",
                    "Yuan digital chino",
                    "Colapso de FTX",
                    "Regulación MiCA en Europa",
                    "Adopción institucional de Bitcoin"
                ],
                "futuro_del_topic": [
                    "CBDCs globales",
                    "Interoperabilidad blockchain",
                    "Regulación armonizada internacional",
                    "Integración con finanzas tradicionales",
                    "Sostenibilidad energética"
                ]
            },
            "cambio_climatico": {
                "conceptos_clave": [
                    "Geoingeniería",
                    "Mitigación climática",
                    "Adaptación",
                    "Transición energética",
                    "Justicia climática",
                    "Tipping points",
                    "Neutralidad de carbono"
                ],
                "actores_principales": [
                    "IPCC",
                    "Gobiernos nacionales",
                    "Empresas energéticas",
                    "Activistas climáticos",
                    "Científicos",
                    "Organizaciones internacionales",
                    "Comunidades vulnerables"
                ],
                "casos_de_estudio": [
                    "Acuerdo de París",
                    "Green New Deal",
                    "Transición energética alemana",
                    "Proyectos de captura de carbono",
                    "Litigios climáticos"
                ],
                "futuro_del_topic": [
                    "Tecnologías de captura directa de CO2",
                    "Geoingeniería solar",
                    "Adaptación basada en ecosistemas",
                    "Financiamiento climático innovador",
                    "Migración climática masiva"
                ]
            },
            "inteligencia_artificial": {
                "conceptos_clave": [
                    "AGI (Inteligencia Artificial General)",
                    "Alineamiento de IA",
                    "Riesgo existencial",
                    "Superinteligencia",
                    "Gobernanza de IA",
                    "Sesgo algorítmico",
                    "Transparencia de IA"
                ],
                "actores_principales": [
                    "Laboratorios de IA",
                    "Reguladores",
                    "Investigadores de seguridad de IA",
                    "Empresas tecnológicas",
                    "Gobiernos",
                    "Organizaciones internacionales",
                    "Sociedad civil"
                ],
                "casos_de_estudio": [
                    "Desarrollo de GPT y LLMs",
                    "Regulación de IA en la UE",
                    "Competencia en IA EE.UU.-China",
                    "Casos de sesgo en algoritmos",
                    "Iniciativas de seguridad de IA"
                ],
                "futuro_del_topic": [
                    "Desarrollo de AGI",
                    "Estándares globales de IA",
                    "IA cuántica",
                    "Automatización masiva del trabajo",
                    "Sistemas de IA autónomos"
                ]
            }
        }
    
    def normalize_topic_name(self, topic_name):
        """Normaliza el nombre del tema para buscar en la base de datos"""
        # Convertir a minúsculas y reemplazar espacios y caracteres especiales
        normalized = topic_name.lower()
        normalized = re.sub(r'[^\w\s]', '', normalized)
        normalized = re.sub(r'\s+', '_', normalized)
        
        # Mapeo de términos clave a identificadores
        mappings = {
            'desinformacion': 'desinformacion_guerra_hibrida',
            'guerra_hibrida': 'desinformacion_guerra_hibrida',
            'autoritario': 'regimenes_autoritarios',
            'regimen': 'regimenes_autoritarios',
            'conflicto': 'conflictos_persistentes',
            'israel': 'conflictos_persistentes',
            'palestina': 'conflictos_persistentes',
            'ucrania': 'conflictos_persistentes',
            'sahara': 'conflictos_persistentes',
            'poder_global': 'poder_global',
            'china': 'poder_global',
            'eeuu': 'poder_global',
            'brics': 'poder_global',
            'privacidad': 'privacidad_digital',
            'vigilancia': 'privacidad_digital',
            'cripto': 'criptoeconomia',
            'bitcoin': 'criptoeconomia',
            'blockchain': 'criptoeconomia',
            'clima': 'cambio_climatico',
            'climatico': 'cambio_climatico',
            'geoingenieria': 'cambio_climatico',
            'inteligencia_artificial': 'inteligencia_artificial',
            'agi': 'inteligencia_artificial',
            'ai': 'inteligencia_artificial'
        }
        
        # Buscar coincidencias en los mapeos
        for key, value in mappings.items():
            if key in normalized:
                return value
        
        return normalized
    
    def analyze_topic(self, topic_name, sources=None):
        """Analiza un tema y devuelve la información estructurada"""
        normalized_topic = self.normalize_topic_name(topic_name)
        
        # Buscar en la base de datos predefinida
        if normalized_topic in self.topics_data:
            data = self.topics_data[normalized_topic].copy()
        else:
            # Si no se encuentra, generar análisis básico
            data = self.generate_basic_analysis(topic_name)
        
        # Agregar fuentes si se proporcionan
        if sources:
            data["fuentes"] = sources
        
        return {
            "tema": topic_name,
            "analisis": data
        }
    
    def generate_basic_analysis(self, topic_name):
        """Genera un análisis básico para temas no predefinidos"""
        return {
            "conceptos_clave": [
                f"Concepto principal de {topic_name}",
                "Aspectos teóricos",
                "Implicaciones prácticas",
                "Contexto histórico",
                "Relevancia actual"
            ],
            "actores_principales": [
                "Instituciones académicas",
                "Investigadores especializados",
                "Organizaciones relevantes",
                "Stakeholders principales",
                "Comunidad internacional"
            ],
            "casos_de_estudio": [
                f"Caso representativo de {topic_name}",
                "Ejemplo histórico relevante",
                "Situación actual destacada"
            ],
            "futuro_del_topic": [
                "Tendencias emergentes",
                "Desarrollos esperados",
                "Desafíos futuros",
                "Oportunidades de investigación",
                "Impacto a largo plazo"
            ]
        }

# Instancia global del analizador
analyzer = TopicAnalyzer()

@topic_analyzer_bp.route('/analyze', methods=['POST'])
@cross_origin()
def analyze_topic():
    """Endpoint para analizar un tema específico"""
    try:
        data = request.get_json()
        
        if not data or 'topic' not in data:
            return jsonify({
                "error": "Se requiere el campo 'topic' en el JSON"
            }), 400
        
        topic_name = data['topic']
        sources = data.get('sources', [])
        
        result = analyzer.analyze_topic(topic_name, sources)
        
        return jsonify(result), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

@topic_analyzer_bp.route('/topics', methods=['GET'])
@cross_origin()
def get_available_topics():
    """
    Obtener todos los temas disponibles con su información detallada
    ---
    responses:
      200:
        description: Lista de todos los temas disponibles con información detallada
        examples:
          application/json: 
            {
              "topics": [{
                "id": "desinformacion_guerra_hibrida",
                "name": "Desinformación en Guerra Híbrida",
                "key_concepts": ["Guerra híbrida", "Desinformación", ...],
                "main_actors": ["Estados-nación", "Agencias de inteligencia", ...],
                "case_studies": ["Interferencia electoral en Estados Unidos (2016)", ...],
                "future_trends": ["IA para generar deepfakes", ...]
              }],
              "total": 8
            }
    """
    try:
        topics_list = []
        for topic_id, topic_data in analyzer.topics_data.items():
            topic_info = {
                "id": topic_id,
                "name": topic_id.replace("_", " ").title(),
                "key_concepts": topic_data.get("conceptos_clave", []),
                "main_actors": topic_data.get("actores_principales", []),
                "case_studies": topic_data.get("casos_de_estudio", []),
                "future_trends": topic_data.get("futuro_del_topic", [])
            }
            topics_list.append(topic_info)
        
        return jsonify({
            "topics": topics_list,
            "total": len(topics_list)
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Error al obtener la lista de temas: {str(e)}"
        }), 500

@topic_analyzer_bp.route('/analyze/batch', methods=['POST'])
@cross_origin()
def analyze_multiple_topics():
    """Endpoint para analizar múltiples temas de una vez"""
    try:
        data = request.get_json()
        
        if not data or 'topics' not in data:
            return jsonify({
                "error": "Se requiere el campo 'topics' con una lista de temas"
            }), 400
        
        topics = data['topics']
        
        if not isinstance(topics, list):
            return jsonify({
                "error": "El campo 'topics' debe ser una lista"
            }), 400
        
        results = []
        for topic_data in topics:
            if isinstance(topic_data, str):
                topic_name = topic_data
                sources = []
            elif isinstance(topic_data, dict) and 'topic' in topic_data:
                topic_name = topic_data['topic']
                sources = topic_data.get('sources', [])
            else:
                continue
            
            result = analyzer.analyze_topic(topic_name, sources)
            results.append(result)
        
        return jsonify({
            "resultados": results,
            "total_analizados": len(results)
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": f"Error interno del servidor: {str(e)}"
        }), 500

@topic_analyzer_bp.route('/health', methods=['GET'])
@cross_origin()
def health_check():
    """Endpoint de verificación de salud de la API"""
    return jsonify({
        "status": "OK",
        "message": "API de análisis de temas funcionando correctamente",
        "version": "1.0.0"
    }), 200

