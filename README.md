# Python http.server File Upload

This repo contains a simple file upload page that works with the Python standard library http.server module, using CGI. No modules or installations required.

Just place the cgi-bin folder from this repo in a directory, then run the http.server command with the `--cgi` flag from that directory, and visit http://localhost:8000/cgi-bin/pyupload.cgi

`python3 -m http.server --cgi`

If you have the `qrcode` Python library installed it will render a QR code using your machine's .local address to make it simpler to access from other devices.

![Screenshot](/screenshot.png?raw=true "Screenshot")

### Why?!??

Who doesn't want to write cgi scripts in 2023? Kids these days have no idea how the world used to work.

But actually–the http.server module is really handy and very widely available. Sometimes you just want to drop some files to another machine.

### It doesn't work

Ensure your user has execute permissions on the cgi file.

Try: `chmod +x ./cgi-bin/pyupload.cgi`


License
---------------

The MIT License (MIT)

Copyright (c) 2023 Adrien Delessert

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
