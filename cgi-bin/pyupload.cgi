#!/usr/bin/env python

import cgitb
cgitb.enable()

import cgi
import logging
import os
import socket

REQUEST_METHOD = os.environ.get('REQUEST_METHOD', 'GET')
REQUEST_PORT = os.environ.get("SERVER_PORT", '8000')


def render_form(success_filenames=None):
    print("Content-Type: text/html")
    print()
    print("""
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
        </head>
    """)

    if success_filenames:
        print("""
            <h3>Files uploaded successfully:</h3>
            <ul>
        """)
        for fname in success_filenames:
            print(f"<li>{fname}</li>")
        print("</ul><hr>")

    print(f"""
        <h2>Upload a file</h2>
        <p>Files will be uploaded to <strong>{os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))}/</strong></p>
    """)

    print(f"""
        <form action="/cgi-bin/pyupload.cgi" method="POST" enctype="multipart/form-data">
            <input type="file" name="uploadedfile" multiple>
            <input type="submit" value="Upload File">
        </form>
    """)

    try:
        import qrcode
        import qrcode.image.svg

        url = f'http://{socket.getfqdn()}.local:{REQUEST_PORT}/cgi-bin/pyupload.cgi'
        qr = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
        print(f"""
            <hr>
            <p>Scan to access on another device: <a href="{url}">{url}</a></p>
            {qr.to_string().decode('utf-8')}
        """)

    except ImportError:
        logging.warning('Skipping generating address QR code, qrcode library not installed or not in python path.')


if REQUEST_METHOD == 'POST':
    form = cgi.FieldStorage()
    files = form['uploadedfile'] if isinstance(form['uploadedfile'], list) else [form['uploadedfile']]

    filenames = []
    for file in files:
        filename = file.filename
        filenames.append(filename)
        with open(f'{os.path.dirname(__file__)}/../{filename}', 'wb+') as f:
            f.write(file.file.read())

    render_form(success_filenames=filenames)

else:
    render_form()