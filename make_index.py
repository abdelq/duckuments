import sys

from bs4 import Tag
import yaml
from mcdp_docs.mcdp_render_manual import get_extra_content
from mcdp_docs.sync_from_circle import get_artefacts, get_links2
from mcdp_report.html import get_css_filename
from mcdp_utils_misc import write_data_to_file, AugmentedResult
from mcdp_utils_xml import bs


books = """

base:
    title: Base
    
    books:
        duckumentation: 
            title: Documentation
             
        the_duckietown_project:
            title: The Duckietown Project
                    
        guide_for_instructors:
            title: Guide instructors
     
tech:
    title: Tech
    
    books:
            
        opmanual_duckiebot_base:
            title: Duckiebot manual
        
        opmanual_duckietown:
            title: Duckietown manual
             
SW:
    title: SW
    books:
        software_carpentry:
            title: Software Carpentry
             
        software_devel:
            title: Software development
             
        software_architecture:
            title: Software arch
            
                
        code_docs:
            title: Code docs
             
     
fall2017:
    title: Fall 2017
    books:
            
        class_fall2017:
            title: Fall 2017
             
        class_fall2017_projects:
            title: Fall 2017 projects
     
theory:
    title: Theory
    books:
            
        learning_materials:
            title: Learning materials
             
        exercises:
            title: exercises     
        
        preliminaries:
            title: Preliminaries
misc:
    title: misc
    
    books:
        drafts:
            title: Drafts
             
             
        deprecated:
            title: Deprecated
    
"""

groups = yaml.load(books)

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
    
}

div.group {
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

divgroups = Tag(name='divgroups')
all_crossrefs = Tag(name='div')

for id_group, group in groups.items():
    divgroup =Tag(name='div')
    divgroup.attrs['class'] = 'group'
    title = group['title']
    divgroup.append(title)

    books = group['books']
    divbook = Tag(name='div')
    for id_book, book in books.items():
        d = os.path.join(dist, id_book)
        d0 = dist
        artefacts = get_artefacts(d0, d)

        div = Tag(name='div')
        div.attrs['class'] = 'book-div'
        links = get_links2(artefacts)
        # p  = Tag(name='p')
        h = Tag(name='h2')
        h.append(book['title'])
        # p.append(h)
        div.append(h)
        div.append(links)

        toc = os.path.join(d, 'out/toc.html')
        if os.path.exists(toc):
            data = open(toc).read()
            x = bs(data)
            for a in x.select('a[href]'):
                href = a.attrs['href']
                a.attrs['href'] = id_book + '/out/' + href
            div.append(x)
        crossrefs = os.path.join(d, 'crossref.html')
        if os.path.exists(crossrefs):
            x = bs(open(crossrefs).read())
            all_crossrefs.append(x.__copy__())
        else:
            print('File does not exist %s' % crossrefs)

        divgroup.append(div)
    divgroups.append(divgroup)

extra = get_extra_content(AugmentedResult())
extra.attrs['id'] = 'extra'
body.append(extra)
body.append(divgroups)



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
