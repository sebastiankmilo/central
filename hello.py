import sys, os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import PDFExporter
dir = os.path.split(os.getcwd())[0]
if dir not in sys.path:
    sys.path.append(dir)


notebook_filename = "C:\Users\Usuario\Desktop\Universidad\9 semestre\Conmutacionpython\Notebook\central.ipynb"

with open(notebook_filename) as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python2')

ep.preprocess(nb, {'metadata': {'path': 'C:\Users\Usuario\Desktop\Universidad\9 semestre\Conmutacionpython\Notebook/'}})

pdf_exporter = PDFExporter()

pdf_data, resources = pdf_exporter.from_notebook_node(nb)

with open("notebook.pdf", "wb") as f:
    f.write(pdf_data)
    f.close()