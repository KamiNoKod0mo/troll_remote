from cx_Freeze import setup, Executable
import sys
sys.setrecursionlimit(3000)  # Ajuste conforme necessário
build_exe_options = {
    "packages":["idna","pygame","pulsectl","alsaaudio","colorama","os","argparse","socket","subprocess"]
}
setup(
    name="MyApp",
    version="0.1",
    description="My App Description",
    executables=[Executable("troll.py")],
    include_files=[('modules.py')],
    options={"build_exe":build_exe_options}
)
