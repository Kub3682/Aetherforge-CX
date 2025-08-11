

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Aetherforge'
copyright = '2025, Kub3682'
author = 'Kub3682'
release = '0.1'

# The full version, including alpha/beta/rc tags



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    # 增加目录导航功能
    'sphinx.ext.napoleon',
    # 支持Markdown格式
    'm2r2',
    # 更好的表格支持
    'sphinx_tables',
    # 代码块语法高亮增强
    'sphinx.highlighting',
]

# 支持同时处理rst和md文件
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# 语言设置为中文
language = 'zh_CN'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# 推荐使用现代美观的furo主题
html_theme = 'furo'

# 主题风格配置
html_theme_options = {
    # 导航栏颜色
    'navigation_with_keys': True,
    'top_of_page_button': 'edit',
    'light_css_variables': {
        'color-brand-primary': '#2c3e50',
        'color-brand-content': '#2980b9',
        'font-stack': 'Inter, system-ui, -apple-system, sans-serif',
    },
    'dark_css_variables': {
        'color-brand-primary': '#3498db',
        'color-brand-content': '#3498db',
    },
}

# 添加自定义CSS
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# 页面标题
html_title = f"{project} v{release}"

# 页脚信息
html_show_copyright = True
html_show_sphinx = False

# 侧边栏配置
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/footer.html",
    ]
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
