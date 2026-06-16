def load_tasks(path: str) -> list[str]:
    with open(path, encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def print_tasks(tasks: list[str]) -> None:
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
