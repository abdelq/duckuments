import sys

from bs4 import Tag
from mcdp_docs.mcdp_render_manual import get_extra_content
from mcdp_docs.sync_from_circle import get_artefacts, get_links2
from mcdp_report.html import get_css_filename
from mcdp_utils_misc import write_data_to_file, AugmentedResult
from mcdp_utils_xml import bs

books = """
duckumentation 
the_duckietown_project 
opmanual_duckiebot_base 
opmanual_duckiebot_fancy 
opmanual_duckietown 
software_carpentry 
software_devel 
software_architecture 
class_fall2017 
class_fall2017_projects 
learning_materials 
exercises 
code_docs 
drafts 
guide_for_instructors 
deprecated 
preliminaries
"""

books = [_ for _ in books.split() if _.strip()]

import os

dist = 'duckuments-dist'

html = Tag(name='html')
head = Tag(name='head')
meta = Tag(name='meta')
meta.attrs['content'] = "text/html; charset=utf-8"
meta.attrs['http-equiv'] = "Content-Type"
body = Tag(name='body')

style = Tag(name='style')
style.append("""
body {
    /* column-count: 3; */
    width: 100% !important;
    margin: 1em !important;
    padding: 0 !important;
    column-count: 3;
}

div.book-div {
    width: 26em;
    background-color: #ddd;
    margin: 1em;
    break-inside: avoid;
    padding: 10px;
}
ul,li {
list-style: none;
}
#extra .notes-panel {
display: none; 
}
.toc_ul-depth-3 {
display: none;
}
""")
head.append(style)
head.append(meta)

html.append(head)
html.append(body)


all_crossrefs = Tag(name='div')
divbook = Tag(name='div')
for book in books:
    d = os.path.join(dist, book)
    d0 = dist
    artefacts = get_artefacts(d0, d)

    div = Tag(name='div')
    div.attrs['class'] = 'book-div'
    links = get_links2(artefacts)
    # p  = Tag(name='p')
    h = Tag(name='h2')
    h.append(book)
    # p.append(h)
    div.append(h)
    div.append(links)

    toc = os.path.join(d, 'out/toc.html')
    if os.path.exists(toc):
        data = open(toc).read()
        x = bs(data)
        for a in x.select('a[href]'):
            href = a.attrs['href']
            a.attrs['href'] = book + '/out/link.html' + href
        div.append(x)
    crossrefs = os.path.join(d, 'crossref.html')
    if os.path.exists(crossrefs):
        x = bs(open(crossrefs).read())
        all_crossrefs.append(x.__copy__())
    else:
        print('File does not exist %s' % crossrefs)

    divbook.append(div)

extra = get_extra_content(AugmentedResult())
extra.attrs['id'] = 'extra'
body.append(extra)
body.append(divbook)



stylesheet = 'v_manual_split'
link = Tag(name='link')
link['rel'] = 'stylesheet'
link['type'] = 'text/css'
link['href'] = get_css_filename('compiled/%s' % stylesheet)
head.append(link)

for e in body.select('.notes-panel'):
    e.extract()
out = sys.argv[1]
write_data_to_file(str(html), out)

out_crossrefs = sys.argv[2]
write_data_to_file(str(all_crossrefs), out_crossrefs)
