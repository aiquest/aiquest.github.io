# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1486948263.058509
_enable_loop = True
_template_filename = u'/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/archive_navigation_helper.tmpl'
_template_uri = u'archive_navigation_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['archive_navigation']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_archive_navigation(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        up_archive = context.get('up_archive', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        has_archive_navigation = context.get('has_archive_navigation', UNDEFINED)
        next_archive = context.get('next_archive', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        previous_archive = context.get('previous_archive', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if 'archive_page' in pagekind:
            if has_archive_navigation:
                __M_writer(u'        <nav class="archivenav">\n        <ul class="pager">\n')
                if previous_archive:
                    __M_writer(u'            <li class="previous"><a href="')
                    __M_writer(unicode(previous_archive))
                    __M_writer(u'" rel="prev">')
                    __M_writer(unicode(messages("Previous")))
                    __M_writer(u'</a></li>\n')
                else:
                    __M_writer(u'            <li class="previous disabled"><a href="#" rel="prev">')
                    __M_writer(unicode(messages("Previous")))
                    __M_writer(u'</a></li>\n')
                if up_archive:
                    __M_writer(u'            <li class="up"><a href="')
                    __M_writer(unicode(up_archive))
                    __M_writer(u'" rel="up">')
                    __M_writer(unicode(messages("Up")))
                    __M_writer(u'</a></li>\n')
                else:
                    __M_writer(u'            <li class="up disabled"><a href="#" rel="up">')
                    __M_writer(unicode(messages("Up")))
                    __M_writer(u'</a></li>\n')
                if next_archive:
                    __M_writer(u'            <li class="next"><a href="')
                    __M_writer(unicode(next_archive))
                    __M_writer(u'" rel="next">')
                    __M_writer(unicode(messages("Next")))
                    __M_writer(u'</a></li>\n')
                else:
                    __M_writer(u'            <li class="next disabled"><a href="#" rel="next">')
                    __M_writer(unicode(messages("Next")))
                    __M_writer(u'</a></li>\n')
                __M_writer(u'        </ul>\n        </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 2, "22": 27, "28": 3, "38": 3, "39": 4, "40": 5, "41": 6, "42": 8, "43": 9, "44": 9, "45": 9, "46": 9, "47": 9, "48": 10, "49": 11, "50": 11, "51": 11, "52": 13, "53": 14, "54": 14, "55": 14, "56": 14, "57": 14, "58": 15, "59": 16, "60": 16, "61": 16, "62": 18, "63": 19, "64": 19, "65": 19, "66": 19, "67": 19, "68": 20, "69": 21, "70": 21, "71": 21, "72": 23, "78": 72}, "uri": "archive_navigation_helper.tmpl", "filename": "/home/mandar/Envs/blog-nikola/local/lib/python2.7/site-packages/nikola/data/themes/base/templates/archive_navigation_helper.tmpl"}
__M_END_METADATA
"""
