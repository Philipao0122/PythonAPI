#!/usr/bin/env python3

import requests
import json
import sys

def test_api():
    base_url = "http://localhost:5002/api/topics"
    
    print("=== Probando API de Análisis de Temas ===\n")
    
    # Probar endpoint de salud
    try:
        print("1. Probando endpoint de salud...")
        response = requests.get(f"{base_url}/health", timeout=5)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")
    except Exception as e:
        print(f"Error en health check: {e}\n")
        return False
    
    # Probar análisis de un tema
    try:
        print("2. Probando análisis de tema 'desinformación'...")
        data = {
            "topic": "desinformación",
            "sources": ["Journal of Strategic Studies", "NATO Strategic Communications"]
        }
        response = requests.post(f"{base_url}/analyze", json=data, timeout=10)
        print(f"Status: {response.status_code}")
        result = response.json()
        print(f"Response: {json.dumps(result, indent=2, ensure_ascii=False)}\n")
    except Exception as e:
        print(f"Error en análisis de tema: {e}\n")
        return False
    
    # Probar lista de temas disponibles
    try:
        print("3. Probando lista de temas disponibles...")
        response = requests.get(f"{base_url}/topics", timeout=5)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")
    except Exception as e:
        print(f"Error en lista de temas: {e}\n")
        return False
    
    return True

if __name__ == "__main__":
    success = test_api()
    if success:
        print("✅ Todas las pruebas pasaron exitosamente!")
    else:
        print("❌ Algunas pruebas fallaron.")
        sys.exit(1)

