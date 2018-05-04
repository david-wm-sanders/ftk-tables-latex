import subprocess
from pathlib import Path

p = Path(__file__).parent
print(f"Running make.py on {str(p)}")
tex_files = p.glob("*.tex")
for tex_file in tex_files:
    print(f"Found {str(tex_file)} - compiling it!")
    command = ["pdflatex.exe", str(tex_file)]
    subprocess.run(command)
