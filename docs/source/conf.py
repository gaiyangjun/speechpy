# -*- coding: utf-8 -*-
#
# SpeechPy documentation build configuration file, created by
# sphinx-quickstart on Wed Nov 22 14:40:49 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
import speechpy
import sphinx_rtd_theme


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    # 'sphinxcontrib.googleanalytics',
]

# True to use the :ivar: role for instance variables. False to use the .. attribute:: directive instead. Defaults to False.
# Refer to http://www.sphinx-doc.org/en/stable/ext/napoleon.html
napoleon_use_ivar = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'SpeechPy'
copyright = u'2017, Amirsina Torfi'
author = u'Amirsina Torfi'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
version = 'master (' + '1.3.1' + ' )'
# The full version, including alpha/beta/rc tags.
# TODO: verify this works as expected
release = 'master'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
    'sticky_navigation': False
}

html_context = {
"display_github": True, # Add 'Edit on Github' link instead of 'View page source'
"last_updated": True,
"commit": False,
}

html_logo = '_static/img/speechpy_logo.gif'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SpeechPydoc'


# -- Options for LaTeX output ---------------------------------------------

# -- Options for LaTeX output ---------------------------------------------

# latex_engine = 'pdflatex'

latex_engine = 'xelatex'
latex_elements = {

'papersize': 'a4paper',
    'releasename':" ",
    'figure_align':'htbp',
    'pointsize': '12pt',
    'fontpkg': r'''
\setmainfont{Times New Roman}
\setsansfont{Times New Roman}
\setmonofont{Times New Roman}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}

latex_logo = '_static/img/speechpy_logo.jpg'


# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     #
#     'papersize': 'a4paper',
#     'releasename':" ",
#     # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
#     # 'fncychap': '\\usepackage[Lenny]{fncychap}',
#     'fncychap': '\\usepackage{fncychap}',
#     # 'fontpkg': ' ',
#
#     'figure_align':'htbp',
#     # The font size ('10pt', '11pt' or '12pt').
#     #
#     'pointsize': '14pt',
#
#     # Additional stuff for the LaTeX preamble.
#
#     # 'preamble': r'''
#     #     %%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%
#     #     %%%add number to subsubsection 2=subsection, 3=subsubsection
#     #     %%% below subsubsection is not good idea.
#     #     \setcounter{secnumdepth}{3}
#     #     %
#     #     %%%% Table of content upto 2=subsection, 3=subsubsection
#     #     %\setcounter{tocdepth}{2}
#     #
#     #     \usepackage{amsmath,amsfonts,amssymb,amsthm}
#     #     \usepackage{graphicx}
#     #
#     #     %\usepackage{minted}
#     #     %\fvset{breaklines=true}
#     #
#     #     %%% reduce spaces for Table of contents, figures and tables
#     #     %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
#     #     \usepackage[notlot,nottoc,notlof]{}
#     #
#     #     \usepackage{color}
#     #     \usepackage{transparent}
#     #     \usepackage{eso-pic}
#     #     \usepackage{lipsum}
#     #
#     #     \usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text
#     #
#     #     %% spacing between line
#     #     \usepackage{setspace}
#     #     %%%%\onehalfspacing
#     #     %%%%\doublespacing
#     #     %\singlespacing
#     #
#     #
#     #     %%%%%%%%%%% datetime
#     #     \usepackage{datetime}
#     #
#     #     \newdateformat{MonthYearFormat}{%
#     #         \monthname[\THEMONTH], \THEYEAR}
#     #
#     #
#     #     %% RO, LE will not work for 'oneside' layout.
#     #     %% Change oneside to twoside in document class
#     #     %\usepackage{fancyhdr}
#     #     %\pagestyle{fancy}
#     #     %\fancyhf{}
#     #
#     #     %%% Alternating Header for oneside
#     #     %\fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
#     #     %\fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}
#     #
#     #     %%% Alternating Header for two side
#     #     %\fancyhead[RO]{\small \nouppercase{\rightmark}}
#     #     %\fancyhead[LE]{\small \nouppercase{\leftmark}}
#     #
#     #     %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
#     #     %\fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Amirsina Torfi} }{\href{https://github.com/astorfi/speechpy}{\tiny SpeechPy}}}
#     #
#     #     %%% Alternating Footer for two side
#     #     %\fancyfoot[RO, RE]{\scriptsize Amirsina Torfi (amirsina.torfi@gmail.com)}
#     #
#     #     %%% page number
#     #     %\fancyfoot[CO, CE]{\thepage}
#     #
#     #     %\renewcommand{\headrulewidth}{0.5pt}
#     #     %\renewcommand{\footrulewidth}{0.5pt}
#     #
#     #     %\RequirePackage{tocbibind} %%% comment this to remove page number for following
#     #     %\addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
#     #     %\addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
#     #     %\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
#     #     %\addto\captionsenglish{\renewcommand{\listtablename}{List of tables}} %%% Heading for TOC
#     #
#     #
#     #     %%reduce spacing for itemize
#     #     \usepackage{enumitem}
#     #     %\setlist{nosep}
#     #
#     #     %%%%%%%%%%% Quote Styles at the top of chapter
#     #     %\usepackage{epigraph}
#     #     %\setlength{\epigraphwidth}{0.8\columnwidth}
#     #     %\newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
#     #     %%%%%%%%%%% Quote for all places except Chapter
#     #     %\newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
#     # ''',
#     #
#     #
#     # 'maketitle': r'''
#     #     \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1
#     #
#     #     \begin{titlepage}
#     #         \centering
#     #
#     #         \vspace*{40mm} %%% * is used to give space from top
#     #         \textbf{\Huge {SpeechPy: Speech Recognition Library}}
#     #
#     #         \vspace{0mm}
#     #         \begin{figure}[!h]
#     #             \centering
#     #             \includegraphics[scale=0.8]{speechpy_logo.jpg}
#     #         \end{figure}
#     #
#     #         \vspace{0mm}
#     #         \Large \textbf{{Amirsina Torfi}}
#     #
#     #         % \small Created on : Octorber, 2017
#     #
#     #         \vspace*{0mm}
#     #         \small  Last updated : \MonthYearFormat\today
#     #
#     #
#     #         %% \vfill adds at the bottom
#     #         \vfill
#     #         \small \textit{Please refer to project repository at }{\href{https://github.com/astorfi/speechpy}{SpeechPy}}
#     #     \end{titlepage}
#     #
#     #     \clearpage
#     #     \pagenumbering{roman}
#     #     \tableofcontents
#     #     % \listoffigures
#     #     % \listoftables
#     #     \clearpage
#     #     \pagenumbering{english}
#     #
#     #     ''',
#     # Latex figure (float) alignment
#     #
#     # 'figure_align': 'htbp',
#     # 'sphinxsetup': \
#     #     #'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
#     #     'verbatimwithframe=true, \
#     #     TitleColor={rgb}{0,0,0}',
#     #     'tableofcontents':' ',
#
# }



# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'SpeechPy.tex', 'SpeechPy Documentation',
     'Amirsina Torfi', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'speechpy', u'SpeechPy Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'SpeechPy', u'SpeechPy Documentation',
     author, 'SpeechPy', 'A library for Speech Recognition and Feature Extraction.',
     'Miscellaneous'),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
}


