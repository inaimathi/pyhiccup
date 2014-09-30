# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Nicolas Bessi
#    Copyright 2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License 3
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

DOC_TYPES = {
    'html4': u"<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01//EN\" "
             u"\"http://www.w3.org/TR/html4/strict.dtd\">\n",

    'xhtml-strict': u"<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 ""Strict//EN\" "
                    u"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n",

    'xhtml-transitional': u"<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\" "
                          u"\"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n",

    'html5': u"<!DOCTYPE html>\n",
}

DEFAULT_XMLNS = u'http://www.w3.org/1999/xhtml'
XMl_DECLARATION = u'<?xml version="1.0" encoding="UTF-8"?>'


def get_doc_type(doc_type):
    """Return a DOCTYPE declaration

    :param doc_type: doc type string must be in ``page.DOC_TYPES``
    :type doc_type: str
    :return: DOCTYPE declaration
    :rtype: str

    """
    if doc_type not in DOC_TYPES:
        raise ValueError(
            'Invalid DOCTYPE %s available values are %s' %
            (doc_type, DOC_TYPES.keys())
        )
    return DOC_TYPES[doc_type]


def get_html_enclosing_tag(etype, **kwargs):
    attrs = {}
    if etype in DOC_TYPES:
        attrs[u'lang'] = u'en'
        attrs[u'dir'] = u'rtl'
        attrs[u'xml:lang'] = u'en'
    if 'xhtml' in etype:
        attrs[u'xmlns'] = DEFAULT_XMLNS
    attrs.update(kwargs)
    return ['html', attrs]


def get_xml_enclosing_tag(etype, **kwargs):
    return [etype, kwargs]
