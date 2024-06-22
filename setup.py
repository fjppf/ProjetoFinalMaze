import sys
from cx_Freeze import setup, Executable

# Dependências do seu projeto
build_exe_options = {
    "packages": ["pygame", "pygame_widgets", "pygame_gui","os","time","threading","random","math"],
    "include_files": ["src/"],  # Inclui todos os arquivos da pasta src
    "excludes": [],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Se quiser que o executável não abra um console no Windows

# Executáveis a serem criados
executables = [
    Executable("src/main.py", base=base, target_name="Simulador de Aprendizagem de Rotas em Labirintos.exe")  # Nome do executável final
]

setup(
    name="ProjetoFinalMaze",
    version="0.1",
    description="Descrição do seu projeto",
    options={"build_exe": build_exe_options},
    executables=executables,
    packages=["src.controllers", "src.models", "src.views", "src.images", "src.utils"]
)
