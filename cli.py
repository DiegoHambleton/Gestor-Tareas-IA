import click
from rich.console import Console
from rich.table import Table
from rich import box
from tasks.models import Task
from tasks.storage import load_tasks, add_task, delete_task, update_task, get_task_by_id
from tasks.ai import prioritize_tasks, suggest_description

console = Console()

@click.group()
def cli():
    """Gestor de tareas con IA integrada."""
    pass

@cli.command()
@click.argument("title")
@click.option("--priority", "-p", default="media", type=click.Choice(["baja", "media", "alta"]))
@click.option("--ai-desc", is_flag=True, help="Generar descripción con IA")
def add(title, priority, ai_desc):
    """Agregar una nueva tarea."""
    description = ""
    if ai_desc:
        with console.status("Generando descripción con IA..."):
            description = suggest_description(title)
        console.print(f"[dim]Descripción:[/dim] {description}")

    task = Task(title=title, priority=priority, description=description)
    add_task(task)
    console.print(f"[green]✓[/green] Tarea [{task.id}] '{title}' agregada.")

@cli.command(name="list")
@click.option("--all", "show_all", is_flag=True, help="Mostrar también las completadas")
def list_tasks(show_all):
    """Listar todas las tareas."""
    tasks = load_tasks()
    if not show_all:
        tasks = [t for t in tasks if not t.done]

    if not tasks:
        console.print("[dim]No hay tareas pendientes.[/dim]")
        return

    table = Table(box=box.SIMPLE, show_header=True, header_style="bold")
    table.add_column("ID", style="dim", width=8)
    table.add_column("Título", min_width=20)
    table.add_column("Prioridad", width=10)
    table.add_column("Estado", width=10)

    priority_colors = {"Alta": "red", "Media": "yellow", "Baja": "green"}

    for t in tasks:
        status = "[green]✓ Terminada[/green]" if t.done else "[yellow] Pendiente[/yellow]"
        color = priority_colors.get(t.priority, "white")
        table.add_row(t.id, t.title, f"[{color}]{t.priority}[/{color}]", status)

    console.print(table)

@cli.command()
@click.argument("task_id")
def done(task_id):
    """Marcar una tarea como completada."""
    task = get_task_by_id(task_id)
    if not task:
        console.print(f"[red]No se encontró tarea con ID {task_id}[/red]")
        return
    task.done = True
    update_task(task)
    console.print(f"[green]✓[/green] Tarea '{task.title}' marcada como completada.")

@cli.command()
@click.argument("task_id")
def delete(task_id):
    """Eliminar una tarea."""
    task = get_task_by_id(task_id)
    if not task:
        console.print(f"[red]No se encontró tarea con ID {task_id}[/red]")
        return
    delete_task(task_id)
    console.print(f"[red]✗[/red] Tarea '{task.title}' eliminada.")

@cli.command()
def prioritize():
    """Pedir a la IA que sugiera el orden de las tareas."""
    tasks = load_tasks()
    with console.status("[bold]Consultando a la IA...[/bold]"):
        suggestion = prioritize_tasks(tasks)
    console.print("\n[bold]Sugerencia de la IA:[/bold]")
    console.print(suggestion)

if __name__ == "__main__":
    cli()