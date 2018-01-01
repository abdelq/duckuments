#!/usr/bin/env python2
import os
from optparse import OptionParser

class AddSearch():
    def __init__(self):

        # jquery
        jquery = '<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>'

        # lunr loads the index
        lunr = '<script src="https://unpkg.com/lunr/lunr.js"></script>'

        # css for bootstrap
        bootstrapCSS = '<link href="/duckuments-dist/master/duckiebook/style/bootstrap/css/bootstrap.min.css" rel="stylesheet">'

        # JavaScript for bootstrap
        bootstrapJS = '<script src="/duckuments-dist/master/duckiebook/style/bootstrap/js/bootstrap.min.js"></script>'

        self.styleSingle = '<link href="duckiebook/style/duckietown.css" rel="stylesheet">'

        if options.single_page:
            self.style = self.styleSingle
        else:
            self.style = '<link href="style/duckietown.css" rel="stylesheet">>'


        self.include = [bootstrapCSS, bootstrapJS, jquery, lunr]



        ### ADD SEARCHBOX TO THE BODY ###

        # div with the searchbox
        self.d = """
            <div id="topbar">
                <nav id="navbar" class="navbar navbar-default">
                    <div class="container-fluid">
                        <div class="navbar-header">
                            <div id="searchdiv" class="navbar-header pull-right">
                                <form action="results.html">
                                   <input type="text" id="searchbox" name="searchbox" placeholder="search">
                                </form>
                            </div>
                            <button id="navbar-button" type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>
                            <a class="navbar-brand" href="#">Duckietown</a>
                        </div>
                        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul class="nav navbar-nav">
                                <li class="navitem"><a href="http://book.duckietown.org">Home</a></li>
                                <li class="navitem"><a href="../duckiebook.html">Single-page</a></li>
                                <li class="navitem"><a href="../duckiebook/index.html">Multi-page</a></li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div> 
            """

        self.dSinglePage = """
            <div id="topbar">
                <nav id="navbar" class="navbar navbar-default">
                    <div class="container-fluid">
                        <div class="navbar-header">
                            <div id="searchdiv" class="navbar-header pull-right">
                                <form action="duckiebook/results.html">
                                   <input type="text" id="searchbox" name="searchbox" placeholder="search">
                                </form>
                            </div>
                            <button id="navbar-button" type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>
                            <a class="navbar-brand" href="#">Duckietown</a>
                        </div>
                        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul class="nav navbar-nav">
                                <li class="navitem"><a href="http://book.duckietown.org">Home</a></li>
                                <li class="navitem"><a href="#">Single-page</a></li>
                                <li class="navitem"><a href="duckiebook/index.html">Multi-page</a></li>
                            </ul>
                        </div>
                    </div>
                </nav>
            </div> 
            """


    def addSearch(self, filename, single_page=False, verbose=False):
        
        with open(filename) as f:
            data = f.read()

        ### ADD SCRIPTS TO THE HEADER ###

        if single_page:
            topdiv = self.dSinglePage
        else:
            topdiv = self.d

        if topdiv in data:
            if verbose:
                print('Already present:\n\t' + topdiv)
        else:
            after = '<body>'
            data = data.replace(after, after + topdiv)
            assert topdiv in data

        for s in self.include:
            if s in data:
                if verbose:
                    print('Already present:\n\t' + s)
            else:
                after = '<head>'
                data = data.replace(after, after + s)
                assert s in data

        if self.style in data:
            pass
        else:
            before = "</head>"
            data = data.replace(before, self.style + before)
            assert self.style in data

        with open(filename, 'w') as f:
            f.write(data)

    def removeSearch(self, filename, single_page=False):
        with open(filename) as f:
            data = f.read()

        data = data.replace(self.d, '')
        data = data.replace(self.dSinglePage, '')
        data = data.replace(self.style, '')
        data = data.replace(self.styleSingle, '')
        for s in self.include:
            data = data.replace(s, '')
        with open(filename, 'w') as f:
            f.write(data)

    def addSearchMultiple(self, rootDir, remove=False):
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                name, ext = os.path.splitext(fname)
                # only indexing markdown files
                if ext != ".html":
                    continue
                file = os.path.join(dirName,fname)
                if not remove:
                    AddSearch().addSearch(file)
                else:
                    AddSearch().removeSearch(file)

    def addBootstrap(self):
        before=""


if __name__ == '__main__':
    usage = "usage: %prog [options] FILE"
    parser = OptionParser(usage)
    parser.add_option("-d", "--directory", dest="is_directory",
                      help="interpret input FILE as directory",
                      action="store_true", default=False)
    parser.add_option("-r", "--remove", dest="remove",
                      help="remove search instead of adding",
                      action="store_true", default=False)
    parser.add_option("-s", "--single-page", dest="single_page",
                      help="use single-page top div",
                      action="store_true", default=False)
    (options, args) = parser.parse_args()

    if len(args) == 0:
        print("Please specify a file.")
        exit(1)
    
    file = args[0]
    search = AddSearch()
    if options.is_directory:
        search.addSearchMultiple(file, remove=options.remove)
    else:
        if options.remove:
            search.removeSearch(file)
        else:
            search.addSearch(file, single_page=options.single_page)