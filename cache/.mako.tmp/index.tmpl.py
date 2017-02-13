# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486948262.954883
_enable_loop = True
_template_filename = u'/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head', u'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'pagination')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        prevlink = context.get('prevlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        _link = context.get('_link', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        parent = context.get('parent', UNDEFINED)
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        nextlink = context.get('nextlink', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

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
        date_format = context.get('date_format', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        prevlink = context.get('prevlink', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        def content_header():
            return render_content_header(context)
        posts = context.get('posts', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        def content():
            return render_content(context)
        pagekind = context.get('pagekind', UNDEFINED)
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        front_index_header = context.get('front_index_header', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer(u'\n')
        if 'main_index' in pagekind:
            __M_writer(u'    ')
            __M_writer(unicode(front_index_header))
            __M_writer(u'\n')
        if page_links:
            __M_writer(u'    ')
            __M_writer(unicode(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer(u'\n')
        __M_writer(u'<div class="postindex">\n')
        for post in posts:
            __M_writer(u'    <article class="h-entry post-')
            __M_writer(unicode(post.meta('type')))
            __M_writer(u'">\n    <header>\n        <h1 class="p-name entry-title"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" class="u-url">')
            __M_writer(filters.html_escape(unicode(post.title())))
            __M_writer(u'</a></h1>\n        <div class="metadata">\n            <p class="byline author vcard"><span class="byline-name fn">\n')
            if author_pages_generated:
                __M_writer(u'                <a href="')
                __M_writer(unicode(_link('author', post.author())))
                __M_writer(u'">')
                __M_writer(filters.html_escape(unicode(post.author())))
                __M_writer(u'</a>\n')
            else:
                __M_writer(u'                ')
                __M_writer(filters.html_escape(unicode(post.author())))
                __M_writer(u'\n')
            __M_writer(u'            </span></p>\n            <p class="dateline"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'" rel="bookmark"><time class="published dt-published" datetime="')
            __M_writer(unicode(post.formatted_date('webiso')))
            __M_writer(u'" title="')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'">')
            __M_writer(filters.html_escape(unicode(post.formatted_date(date_format))))
            __M_writer(u'</time></a></p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer(u'                <p class="commentline">')
                __M_writer(unicode(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer(u'\n')
            __M_writer(u'        </div>\n    </header>\n')
            if index_teasers:
                __M_writer(u'    <div class="p-summary entry-summary">\n    ')
                __M_writer(unicode(post.text(teaser_only=True)))
                __M_writer(u'\n')
            else:
                __M_writer(u'    <div class="e-content entry-content">\n    ')
                __M_writer(unicode(post.text(teaser_only=False)))
                __M_writer(u'\n')
            __M_writer(u'    </div>\n    </article>\n')
        __M_writer(u'</div>\n')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer(u'        <link rel="prefetch" href="')
            __M_writer(unicode(posts[0].permalink()))
            __M_writer(u'" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 26, "129": 26, "130": 26, "131": 29, "132": 30, "133": 30, "134": 30, "135": 30, "136": 30, "137": 31, "138": 32, "139": 32, "140": 32, "141": 34, "142": 35, "143": 35, "144": 35, "145": 35, "146": 35, "147": 35, "148": 35, "149": 35, "150": 36, "23": 4, "152": 37, "153": 37, "26": 3, "155": 41, "156": 42, "29": 2, "158": 43, "159": 44, "160": 45, "161": 46, "162": 46, "35": 0, "164": 51, "165": 52, "166": 52, "167": 53, "168": 53, "169": 54, "170": 54, "157": 43, "176": 7, "186": 7, "187": 8, "151": 37, "189": 9, "190": 10, "191": 10, "192": 10, "65": 2, "66": 3, "67": 4, "68": 5, "198": 15, "73": 12, "78": 55, "209": 198, "163": 48, "84": 14, "188": 8, "108": 14, "154": 39, "113": 15, "114": 16, "115": 17, "116": 17, "117": 17, "118": 19, "119": 20, "120": 20, "121": 20, "122": 22, "123": 23, "124": 24, "125": 24, "126": 24, "127": 26}, "uri": "index.tmpl", "filename": "/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/index.tmpl"}
__M_END_METADATA
"""
