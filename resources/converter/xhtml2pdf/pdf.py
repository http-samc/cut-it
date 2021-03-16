# -*- coding: utf-8 -*-

# Copyright 2010 Dirk Holtwick, holtwick.it
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

import six

from xhtml2pdf.util import PyPDF2, getFile, pisaTempFile

log = logging.getLogger("xhtml2pdf")


class pisaPDF:
    def __init__(self, capacity=-1):
        self.capacity = capacity
        self.files = []

    def addFromURI(self, url, basepath=None):
        obj = getFile(url, basepath)
        if obj and (not obj.notFound()):
            self.files.append(obj.getFileContent())

    addFromFileName = addFromURI

    def addFromFile(self, f):
        if hasattr(f, "read"):
            self.files.append(f)
        else:
            self.addFromURI(f)

    def addFromString(self, data):
        self.files.append(pisaTempFile(data, capacity=self.capacity))

    def addDocument(self, doc):
        if hasattr(doc.dest, "read"):
            self.files.append(doc.dest)

    def join(self, file=None):
        output = PyPDF2.PdfFileWriter()
        for pdffile in self.files:
            pdf = PyPDF2.PdfFileReader(pdffile)
            for pageNumber in six.moves.range(pdf.getNumPages()):
                output.addPage(pdf.getPage(pageNumber))

        if file is not None:
            output.write(file)
            return file
        out = pisaTempFile(capacity=self.capacity)
        output.write(out)
        return out.getvalue()

    getvalue = join
    __str__ = join
