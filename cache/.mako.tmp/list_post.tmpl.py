# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486948263.051876
_enable_loop = True
_template_filename = u'/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'archive_nav', context._clean_inheritance_tokens(), templateuri=u'archive_navigation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'archive_nav')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'archive_nav')._populate(_import_ns, [u'*'])
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'archive_nav')._populate(_import_ns, [u'*'])
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        def content():
            return render_content(context)
        archive_nav = _mako_get_namespace(context, 'archive_nav')
        __M_writer = context.writer()
        __M_writer(u'\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(unicode(title)))
        __M_writer(u'</h1>\n    </header>\n    ')
        __M_writer(unicode(archive_nav.archive_navigation()))
        __M_writer(u'\n')
        if posts:
            __M_writer(u'    <ul class="postlist">\n')
            for post in posts:
                __M_writer(u'        <li><time class="listdate" datetime="')
                __M_writer(unicode(post.formatted_date('webiso')))
                __M_writer(u'" title="')
                __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
                __M_writer(u'</time> <a href="')
                __M_writer(unicode(post.permalink()))
                __M_writer(u'" class="listtitle">')
                __M_writer(filters.html_escape(unicode(post.title())))
                __M_writer(u'</a></li>\n')
            __M_writer(u'    </ul>\n')
        else:
            __M_writer(u'    <p>')
            __M_writer(unicode(messages("No posts found.")))
            __M_writer(u'</p>\n')
        __M_writer(u'</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "43": 2, "44": 3, "49": 21, "55": 5, "68": 5, "69": 8, "70": 8, "71": 10, "72": 10, "73": 11, "74": 12, "75": 13, "76": 14, "77": 14, "78": 14, "79": 14, "80": 14, "81": 14, "82": 14, "83": 14, "84": 14, "85": 14, "86": 14, "87": 16, "88": 17, "89": 18, "90": 18, "91": 18, "92": 20, "98": 92}, "uri": "list_post.tmpl", "filename": "/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/list_post.tmpl"}
__M_END_METADATA
"""
