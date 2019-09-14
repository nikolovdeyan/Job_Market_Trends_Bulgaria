import sys
from nbconvert import HTMLExporter
import nbformat
from bs4 import BeautifulSoup



notebook_file = sys.argv[1]
html_exporter = HTMLExporter()
nb = nbformat.reads(open(notebook_file, 'r').read(), as_version=4)

(body, resources) = html_exporter.from_notebook_node(nb)
html_file = notebook_file.replace(".ipynb", ".html")

#  soup = BeautifulSoup(body, 'html.parser')
#
#  cells = soup.find_all('div', class_='cell')
#  for c in cells:
#      c['class'] = c.get('class', []) + ['col-m-12']
#
#  outcells = soup.find_all('div', class_='output')
#  for o in outcells:
#      o['class'] = o.get('class', []) + ['col-m-12']

with open(html_file, 'w') as html_file_writer:
    html_file_writer.write(soup.prettify())
