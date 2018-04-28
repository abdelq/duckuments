import sys
from collections import OrderedDict

import yaml
from bs4 import Tag
from mcdp_docs.embed_css import embed_css_files
from mcdp_docs.mcdp_render_manual import get_extra_content
from mcdp_docs.sync_from_circle import get_artefacts, get_links2
from mcdp_report.html import get_css_filename
from mcdp_utils_misc import write_data_to_file, AugmentedResult
from mcdp_utils_xml import bs, gettext

books = """
!!omap
- base:
    title: Information about the project
    
    abstract: |
        This is general information about the project
        and how to contribute to it.
    
    books: !!omap
    
        - the_duckietown_project:
            title: The Duckietown Project
            abstract: |
                Learn about the history and current status.
                    
        - guide_for_instructors:
            title: Guide for instructors

        - duckumentation: 
            title: Contributing to the documentation
             
     
- tech:
    title: Operation manuals
    
    abstract: |
    
        These are the operation manuals.
    
    books: !!omap
            
        - opmanual_duckiebot_base:
            title: Duckiebot manual
        
        - opmanual_duckietown:
            title: Duckietown manual
             
        - software_carpentry:
            title: Reference for useful commands
             
- SW:
    title: Software development
    
    books: !!omap
        - software_architecture:
            title: Duckietown software architecture

        - software_devel:
            title: Software development in Duckietown
             
        - code_docs:
            title: Packages documentation
             
     
     
- theory:
    title: Class materials
     
    books: !!omap
            
        - learning_materials:
            title: Learning materials
             
        - exercises:
            title: Exercises     
        
        - preliminaries:
            title: Preliminaries


- fall2017:
    title: Past editions
    books: !!omap
            
        - class_fall2017:
            title: Fall 2017
             
        - class_fall2017_projects:
            title: Fall 2017 projects
            
- misc:
    title: Miscellanea
    
    abstract: |
        Other content
    
    books: !!omap
        - drafts:
            title: Drafts
            
        - deprecated:
            title: Deprecated
    
"""

groups = OrderedDict(yaml.load(books))

import os

dist = 'duckuments-dist'

html = Tag(name='html')
head = Tag(name='head')
meta = Tag(name='meta')
meta.attrs['content'] = "text/html; charset=utf-8"
meta.attrs['http-equiv'] = "Content-Type"

stylesheet = 'v_manual_split'
link = Tag(name='link')
link['rel'] = 'stylesheet'
link['type'] = 'text/css'
link['href'] = get_css_filename('compiled/%s' % stylesheet)
head.append(link)

body = Tag(name='body')

style = Tag(name='style')
# language=css
style.append("""
body {
    width: 100% !important;
    margin: 1em !important;
    padding: 0 !important;
    
}
.EWT {
    display: none;
    font-weight: bold;
    font-size: smaller;
    color: darkblue;
} 
a.EWT {
    text-decoration: none;
    font-family: arial;
} 
.show_todos .EWT {
    display: inline;
}
.toc_what {
    display: none;
}

h3 {
    font-size: 150%;
    color: black;
    text-align: left;
    border-bottom: 0;
    margin-top: 0;
    padding-top: 0;
}

div.group {
    column-count: auto;
    column-width: 22em;
    width: calc(100% - 4em);
    display: block;
    background-color: #eaeaea;
    padding: 1em;
    margin: 1em;
    min-height: 12em;
}

div.book-div span a:nth-child(2) {
    margin-right: 2em;
}
div.book-div {
    background-color: #ddd;
    margin: 1em;
    padding: 10px;
}
.div_inside {
    break-inside: avoid;
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

divgroups = Tag(name='div')
all_crossrefs = Tag(name='div')

for id_group, group in groups.items():
    divgroup = Tag(name='div')
    divgroup.attrs['class'] = 'group'

    h0 = Tag(name='h1')
    h0.append(group['title'])

    divgroup.append(h0)

    if 'abstract' in group:
        p = Tag(name='p')
        p.append(group['abstract'])
        divgroup.append(p)

    books = group['books']
    divbook = Tag(name='div')
    books = OrderedDict(books)
    for id_book, book in books.items():
        d = os.path.join(dist, id_book)
        d0 = dist
        artefacts = get_artefacts(d0, d)

        div = Tag(name='div')
        div.attrs['class'] = 'book-div'
        div_inside = Tag(name='div')
        div_inside.attrs['class'] = 'div_inside'
        links = get_links2(artefacts)

        for a in links.select('a'):
            s = gettext(a)
            if 'error' in s or 'warning' in s or 'task' in s:
                a['class'] = 'EWT'
        # p  = Tag(name='p')
        h = Tag(name='h3')
        h.append(book['title'])
        # p.append(h)
        div_inside.append(h)
        if 'abstract' in book:
            p = Tag(name='p')
            p.append(book['abstract'])
            div_inside.append(p)

        if 'abstract' in book:
            div_inside.append(book['abstract'])
        div_inside.append(links)
        div.append(div_inside)

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

embed_css_files(html)

for e in body.select('.notes-panel'):
    e.extract()
out = sys.argv[1]
write_data_to_file(str(html), out)

manifest = []
manifest.append(dict(display='summary', filename=os.path.basename(out)))
mf = os.path.join(os.path.dirname(out), 'summary.manifest.yaml')
write_data_to_file(yaml.dump(manifest), mf)

out_crossrefs = sys.argv[2]
write_data_to_file(str(all_crossrefs), out_crossrefs)

