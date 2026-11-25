import json

def guardar_archivo(alumnos):
    with open("alumnos/alumnos.json", "w", encoding="utf-8") as file:
        json.dump(alumnos, file, indent=4, ensure_ascii=False)

def leer_archivo():
    with open("alumnos/alumnos.json", "a", encoding="utf-8") as file:
        pass
    with open("alumnos/alumnos.json", "r", encoding="utf-8") as file:
        content = file.read()
        if content == "":
            alumnos = {}
        else:
            alumnos = json.loads(content)
    return alumnos