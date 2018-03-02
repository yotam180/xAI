#
#   Serving static files for the web version
#   Author: Yotam Salmon
#   Last Edited: 02/03/18
#

import os
import re
import io
import magic

def mime_content_type(filename):
    """Get mime type
    :param filename: str
    :type filename: str
    :rtype: str
    """
    mime_types = dict(
        txt='text/plain',
        htm='text/html',
        html='text/html',
        php='text/html',
        css='text/css',
        js='application/javascript',
        json='application/json',
        xml='application/xml',
        swf='application/x-shockwave-flash',
        flv='video/x-flv',

        # images
        png='image/png',
        jpe='image/jpeg',
        jpeg='image/jpeg',
        jpg='image/jpeg',
        gif='image/gif',
        bmp='image/bmp',
        ico='image/vnd.microsoft.icon',
        tiff='image/tiff',
        tif='image/tiff',
        svg='image/svg+xml',
        svgz='image/svg+xml',

        # archives
        zip='application/zip',
        rar='application/x-rar-compressed',
        exe='application/x-msdownload',
        msi='application/x-msdownload',
        cab='application/vnd.ms-cab-compressed',

        # audio/video
        mp3='audio/mpeg',
        ogg='audio/ogg',
        qt='video/quicktime',
        mov='video/quicktime',

        # adobe
        pdf='application/pdf',
        psd='image/vnd.adobe.photoshop',
        ai='application/postscript',
        eps='application/postscript',
        ps='application/postscript',

        # ms office
        doc='application/msword',
        rtf='application/rtf',
        xls='application/vnd.ms-excel',
        ppt='application/vnd.ms-powerpoint',

        # open office
        odt='application/vnd.oasis.opendocument.text',
        ods='application/vnd.oasis.opendocument.spreadsheet',
    )

    ext = os.path.splitext(filename)[1][1:].lower()
    if ext in mime_types:
        return mime_types[ext]
    else:
        return 'application/octet-stream'

def sub(x):
    """
    For substituting the <?php?> require tags with the inner content of the required pages.
    We are actually simulating here the behaviour of an Apache server, since the webpages already
    use PHP, and we don't want to change the infrastructure.
    So we give them what they need in the same framework they work on.
    """
    with open("web/" + x.group(1), "r") as f:
        return f.read()

def get(path):
    """
    Returns the contents and the mime type of a static file requetsed by /path
    """

    if path == "/":
        return get("/index.php")

    p = os.path.abspath("web" + path.split("?")[0].split("#")[0])
    print(os.path.exists(p))
    if os.path.exists(p):
        if ".php" in p:
            with io.open(p, mode="r", encoding="utf-8") as f:
                page = f.read() 
            while re.findall("<\?php.+?require\(\"(.+?)\"\);.+?\?>", page):
                page = re.sub("<\?php.+?require\(\"(.+?)\"\);.+?\?>", sub, page)
        else:
            with open(p, "rb") as f:
                page = f.read()

        print("Mime")
        mime = mime_content_type(p)
        print("Returning")
        return page, mime
        
    return None, None