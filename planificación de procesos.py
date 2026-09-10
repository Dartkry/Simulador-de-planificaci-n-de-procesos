import time
from collections import deque

class Proceso:
    def __init__(self, id_proc, racha_cpu, prioridad, tipo):
        self.id = id_proc
        self.racha_cpu = racha_cpu
        self.tiempo_restante = racha_cpu
        self.prioridad = prioridad
        self.tipo = tipo
        self.estado = "Nuevo"

def imprimir_estado(proceso, mensaje=""):
    print(f"[{proceso.estado:^12}] Proceso {proceso.id} | {proceso.tipo} | Restante: {proceso.tiempo_restante}s {mensaje}")

def planificador_prioridad(procesos):
    print("\n" + "="*50)
    print(" SIMULACIÓN: PLANIFICADOR POR PRIORIDAD ")
    print("="*50)
    
    procesos.sort(key=lambda x: x.prioridad)
    
    for p in procesos:
        p.estado = "Listo"
        
    for p in procesos:
        p.estado = "En Ejecución"
        imprimir_estado(p, "-> Entra a CPU")
        
        while p.tiempo_restante > 0:
            time.sleep(0.8) 
            p.tiempo_restante -= 1
            if p.tiempo_restante > 0:
                print(f"   ... procesando {p.id}, restan {p.tiempo_restante}s")
                
        p.estado = "Terminado"
        imprimir_estado(p, "-> Tarea completada\n")

def planificador_round_robin(procesos, quantum=2):
    print("\n" + "="*50)
    print(f" SIMULACIÓN: PLANIFICADOR ROUND-ROBIN (Quantum={quantum}) ")
    print("="*50)
    
    cola = deque(procesos)
    
    for p in cola:
        p.estado = "Listo"
        
    while cola:
        p = cola.popleft()
        p.estado = "En Ejecución"
        imprimir_estado(p, f"-> Entra a CPU (Máximo {quantum}s)")
        
        tiempo_uso = min(quantum, p.tiempo_restante)
        time.sleep(tiempo_uso * 0.5)
        p.tiempo_restante -= tiempo_uso
        
        if p.tiempo_restante > 0:
            p.estado = "Bloqueado"
            imprimir_estado(p, "-> Tiempo expirado, vuelve a la cola\n")
            p.estado = "Listo"
            cola.append(p)
        else:
            p.estado = "Terminado"
            imprimir_estado(p, "-> Tarea completada\n")

if __name__ == '__main__':
    procesos_prio = [
        Proceso("P1", 4, 2, "Datos_Trafico"),
        Proceso("P2", 2, 1, "Alerta_Accidente"),
        Proceso("P3", 3, 3, "Rutina_Fondo")
    ]
    
    procesos_rr = [
        Proceso("P1", 4, 2, "Datos_Trafico"),
        Proceso("P2", 2, 1, "Alerta_Accidente"),
        Proceso("P3", 3, 3, "Rutina_Fondo")
    ]
    planificador_prioridad(procesos_prio)
    time.sleep(1.5)
    planificador_round_robin(procesos_rr, quantum=2)
