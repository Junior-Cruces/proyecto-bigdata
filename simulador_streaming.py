
import json
import random
import time
from datetime import datetime

# Tipos de eventos y dispositivos para simular el comportamiento del usuario
EVENT_TYPES = ['click', 'view_product', 'add_to_cart', 'purchase', 'error_500']
DEVICES = ['mobile', 'desktop', 'tablet']

def generar_evento_artificial():
    # Estructura del dataset sugerido por el ejercicio
    event_type = random.choice(EVENT_TYPES)
    
    # Simular que si hay un error 500, la latencia es más alta de lo normal
    if event_type == 'error_500':
        latency = random.randint(1500, 4000)
        status = 500
    else:
        latency = random.randint(50, 300)
        status = 200

    evento = {
        "event_id": f"evt-{random.randint(100000, 999999)}",
        "event_time": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        "user_id": f"usr-{random.randint(1000, 5000)}",
        "event_type": event_type,
        "product_id": f"prod-{random.randint(100, 999)}",
        "device": random.choice(DEVICES),
        "status": status,
        "latency_ms": latency
    }
    return evento

if __name__ == '__main__':
    print("🚀 Iniciando simulador de eventos local (Presiona Ctrl+C para detener)...")
    try:
        # Simulación local inicial para verificar la salida de datos
        for _ in range(10):
            nuevo_evento = generar_evento_artificial()
            print(json.dumps(nuevo_evento, indent=2))
            time.sleep(1) # Esperar un segundo entre eventos
    except KeyboardInterrupt:
        print("\n🛑 Simulador detenido.")