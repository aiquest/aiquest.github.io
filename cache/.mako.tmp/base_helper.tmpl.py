# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486948263.04078
_enable_loop = True
_template_filename = u'/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl'
_template_uri = u'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['late_load_js', 'html_headstart', 'html_navigation_links', 'html_stylesheets', 'html_translations', 'html_feedlinks']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'notes', context._clean_inheritance_tokens(), templateuri=u'annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        colorbox_locales = _import_ns.get('colorbox_locales', context.get('colorbox_locales', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        social_buttons_code = _import_ns.get('social_buttons_code', context.get('social_buttons_code', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n\n            <script src="/assets/js/all.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/all-nocdn.js"></script>\n')
        else:
            if use_cdn:
                __M_writer(u'            <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.3/jquery.min.js"></script>\n            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/jquery.min.js"></script>\n            <script src="/assets/js/bootstrap.min.js"></script>\n            <script src="/assets/js/moment-with-locales.min.js"></script>\n            <script src="/assets/js/fancydates.js"></script>\n')
            __M_writer(u'        <script src="/assets/js/jquery.colorbox-min.js"></script>\n')
        if colorbox_locales[lang]:
            __M_writer(u'        <script src="/assets/js/colorbox-i18n/jquery.colorbox-')
            __M_writer(unicode(colorbox_locales[lang]))
            __M_writer(u'.js"></script>\n')
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        mathjax_config = _import_ns.get('mathjax_config', context.get('mathjax_config', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        comment_system = _import_ns.get('comment_system', context.get('comment_system', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        use_open_graph = _import_ns.get('use_open_graph', context.get('use_open_graph', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        is_rtl = _import_ns.get('is_rtl', context.get('is_rtl', UNDEFINED))
        use_base_tag = _import_ns.get('use_base_tag', context.get('use_base_tag', UNDEFINED))
        comment_system_id = _import_ns.get('comment_system_id', context.get('comment_system_id', UNDEFINED))
        extra_head_data = _import_ns.get('extra_head_data', context.get('extra_head_data', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        theme_color = _import_ns.get('theme_color', context.get('theme_color', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def html_feedlinks():
            return render_html_feedlinks(context)
        url_type = _import_ns.get('url_type', context.get('url_type', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        favicons = _import_ns.get('favicons', context.get('favicons', UNDEFINED))
        def html_stylesheets():
            return render_html_stylesheets(context)
        twitter_card = _import_ns.get('twitter_card', context.get('twitter_card', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer(u"prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer(u'og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer(u'article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            __M_writer(u"'")
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer(u'    <base href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(filters.html_escape(unicode(description)))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n')
        if title == blog_title:
            __M_writer(u'        <title>')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</title>\n')
        else:
            __M_writer(u'        <title>')
            __M_writer(filters.html_escape(unicode(title)))
            __M_writer(u' | ')
            __M_writer(filters.html_escape(unicode(blog_title)))
            __M_writer(u'</title>\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    <meta name="theme-color" content="')
        __M_writer(unicode(theme_color))
        __M_writer(u'">\n    <meta name="generator" content="Nikola (getnikola.com)">\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n    <link rel="canonical" href="')
        __M_writer(unicode(abs_link(permalink)))
        __M_writer(u'">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if prevlink:
            __M_writer(u'        <link rel="prev" href="')
            __M_writer(unicode(prevlink))
            __M_writer(u'" type="text/html">\n')
        if nextlink:
            __M_writer(u'        <link rel="next" href="')
            __M_writer(unicode(nextlink))
            __M_writer(u'" type="text/html">\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(mathjax_config))
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="')
            __M_writer(unicode(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer(u'"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        tuple = _import_ns.get('tuple', context.get('tuple', UNDEFINED))
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        rel_link = _import_ns.get('rel_link', context.get('rel_link', UNDEFINED))
        isinstance = _import_ns.get('isinstance', context.get('isinstance', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for url, text in navigation_links[lang]:
            if isinstance(url, tuple):
                __M_writer(u'            <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">')
                __M_writer(unicode(text))
                __M_writer(u' <b class="caret"></b></a>\n            <ul class="dropdown-menu">\n')
                for suburl, text in url:
                    if rel_link(permalink, suburl) == "#":
                        __M_writer(u'                    <li class="active"><a href="')
                        __M_writer(unicode(permalink))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u' <span class="sr-only">')
                        __M_writer(unicode(messages("(active)", lang)))
                        __M_writer(u'</span></a>\n')
                    else:
                        __M_writer(u'                    <li><a href="')
                        __M_writer(unicode(suburl))
                        __M_writer(u'">')
                        __M_writer(unicode(text))
                        __M_writer(u'</a>\n')
                __M_writer(u'            </ul>\n')
            else:
                if rel_link(permalink, url) == "#":
                    __M_writer(u'                <li class="active"><a href="')
                    __M_writer(unicode(permalink))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u' <span class="sr-only">')
                    __M_writer(unicode(messages("(active)", lang)))
                    __M_writer(u'</span></a>\n')
                else:
                    __M_writer(u'                <li><a href="')
                    __M_writer(unicode(url))
                    __M_writer(u'">')
                    __M_writer(unicode(text))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        notes = _mako_get_namespace(context, 'notes')
        use_cdn = _import_ns.get('use_cdn', context.get('use_cdn', UNDEFINED))
        has_custom_css = _import_ns.get('has_custom_css', context.get('has_custom_css', UNDEFINED))
        needs_ipython_css = _import_ns.get('needs_ipython_css', context.get('needs_ipython_css', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        use_bundles = _import_ns.get('use_bundles', context.get('use_bundles', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer(u'            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">\n')
            else:
                __M_writer(u'            <link href="/assets/css/bootstrap.min.css" rel="stylesheet" type="text/css">\n')
            __M_writer(u'        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/colorbox.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer(u'        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(abs_link(_link("root", None, langname))))
                __M_writer(u'" rel="alternate" hreflang="')
                __M_writer(unicode(langname))
                __M_writer(u'">')
                __M_writer(unicode(messages("LANGUAGE", langname)))
                __M_writer(u'</a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'notes')._populate(_import_ns, [u'*'])
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        rss_link = _import_ns.get('rss_link', context.get('rss_link', UNDEFINED))
        generate_rss = _import_ns.get('generate_rss', context.get('generate_rss', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        generate_atom = _import_ns.get('generate_atom', context.get('generate_atom', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer(u'                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('index_atom', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(unicode(_link('index_atom', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 3, "26": 0, "33": 2, "34": 3, "35": 73, "36": 101, "37": 135, "38": 158, "39": 181, "40": 189, "46": 75, "57": 75, "58": 76, "59": 77, "60": 78, "61": 82, "62": 83, "63": 85, "64": 86, "65": 87, "66": 89, "67": 90, "68": 95, "69": 97, "70": 98, "71": 98, "72": 98, "73": 100, "74": 100, "75": 100, "81": 4, "112": 4, "113": 8, "114": 9, "115": 10, "116": 11, "117": 13, "118": 14, "119": 16, "120": 17, "121": 19, "122": 22, "123": 23, "124": 26, "125": 26, "126": 26, "127": 29, "128": 30, "129": 30, "130": 30, "131": 32, "132": 33, "133": 33, "134": 33, "135": 35, "136": 36, "137": 37, "138": 37, "139": 37, "140": 38, "141": 39, "142": 39, "143": 39, "144": 39, "145": 39, "146": 41, "147": 42, "148": 42, "149": 43, "150": 43, "151": 45, "152": 45, "153": 46, "154": 46, "155": 48, "156": 49, "157": 50, "158": 50, "159": 50, "160": 50, "161": 50, "162": 50, "163": 50, "164": 53, "165": 54, "166": 55, "167": 55, "168": 55, "169": 57, "170": 58, "171": 59, "172": 59, "173": 59, "174": 61, "175": 62, "176": 62, "177": 62, "178": 64, "179": 65, "180": 65, "181": 66, "182": 67, "183": 68, "184": 69, "185": 69, "186": 69, "187": 71, "188": 72, "189": 72, "195": 137, "208": 137, "209": 138, "210": 139, "211": 140, "212": 140, "213": 140, "214": 142, "215": 143, "216": 144, "217": 144, "218": 144, "219": 144, "220": 144, "221": 144, "222": 144, "223": 145, "224": 146, "225": 146, "226": 146, "227": 146, "228": 146, "229": 149, "230": 150, "231": 151, "232": 152, "233": 152, "234": 152, "235": 152, "236": 152, "237": 152, "238": 152, "239": 153, "240": 154, "241": 154, "242": 154, "243": 154, "244": 154, "250": 104, "263": 104, "264": 105, "265": 106, "266": 107, "267": 109, "268": 110, "269": 112, "270": 113, "271": 114, "272": 115, "273": 116, "274": 118, "275": 122, "276": 123, "277": 126, "278": 127, "279": 130, "280": 131, "281": 131, "282": 131, "283": 132, "284": 133, "285": 133, "286": 133, "292": 183, "304": 183, "305": 184, "306": 185, "307": 186, "308": 186, "309": 186, "310": 186, "311": 186, "312": 186, "313": 186, "319": 160, "332": 160, "333": 161, "334": 162, "335": 162, "336": 162, "337": 163, "338": 164, "339": 165, "340": 166, "341": 166, "342": 166, "343": 166, "344": 166, "345": 168, "346": 169, "347": 169, "348": 169, "349": 172, "350": 173, "351": 174, "352": 175, "353": 175, "354": 175, "355": 175, "356": 175, "357": 177, "358": 178, "359": 178, "360": 178, "366": 360}, "uri": "base_helper.tmpl", "filename": "/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/bootstrap3/templates/base_helper.tmpl"}
__M_END_METADATA
"""
