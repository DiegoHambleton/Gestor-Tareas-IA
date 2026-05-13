**---GESTOR DE TAREAS CON IA---**

-Gestor de tareas en terminal con IA integrada. Permite agregar, listar, completar y eliminar tareas; 
se utiliza Gemini para sugerir el orden óptimo en que deberías hacerlas.

> **Requisitos:** Python 3.10+ y una terminal como Git Bash (Windows), Terminal (Mac) o cualquier terminal de Linux.

---TECNOLOGÍAS---
- Python 3.13
- Click — comandos de terminal
- Rich — interfaz visual en terminal
- Google Gemini — generación de descripciones y priorización con IA

---INSTALACIÓN---
1. Clona el repositorio
   git clone https://github.com/DiegoHambleton/Gestor-Tareas-IA.git
   cd Gestor-Tareas-IA

2. Crea el entorno virtual
   python -m venv venv
   source venv/Scripts/activate

3. Instala las dependencias
   pip install -r requirements.txt

4. Configura tu API key de Gemini
   - Entra a https://aistudio.google.com/apikey
   - Inicia sesión con tu cuenta de Google
   - Haz clic en "Create API Key"
   - Copia la key generada
   
     *Nota: cada usuario debe generar su propia API key. No compartas tu key con nadie.
   
   -export GEMINI_API_KEY="tu-api-key"
   
     *Nota: esta variable se resetea al cerrar la terminal. Para no tener que configurarla cada vez,
       agrégala a tu .bashrc: echo 'export GEMINI_API_KEY="tu-api-key"' >> ~/.bashrc
   
---USO---
-Agregar tarea
python cli.py add "Estudiar FastAPI" -p alta-

Agregar tarea con descripción generada por IA
python cli.py add "Escribir tests" --ai-desc

-Ver tareas pendientes
python cli.py list

-Ver todas incluyendo completadas
python cli.py list --all

-Marcar como completada
python cli.py done <id>

-Eliminar tarea
python cli.py delete <id>

# Pedir sugerencia de orden a la IA
python cli.py prioritize
