from google import genai
import os
from tasks.models import Task

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def prioritize_tasks(tasks: list[Task]) -> str:
    if not tasks:
        return "No hay tareas pendientes."

    task_list = "\n".join(
        f"- [{t.id}] {t.title} (prioridad actual: {t.priority})"
        for t in tasks if not t.done
    )

    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=(
            f"Tengo estas tareas pendientes:\n{task_list}\n\n"
            "Sugiere en qué orden debería hacerlas y por qué. "
            "Sé breve y directo, máximo 5 líneas."
        )
    )
    return response.text

def suggest_description(title: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=(
            f"Para una tarea llamada '{title}', escribe una descripción "
            "breve y accionable de máximo 2 oraciones. Solo la descripción, sin más texto."
        )
    )
    return response.text