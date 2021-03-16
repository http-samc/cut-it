#!/usr/bin/env python
from __future__ import print_function

import datetime
import glob
import os
import shutil
import sys
from optparse import OptionParser
from subprocess import PIPE, Popen

from xhtml2pdf import pisa

do_bytes = 'b'
if sys.version[0] != '2':
    do_bytes = ''

def render_pdf(filename, output_dir, options):
    if options.debug:
        print('Rendering %s' % filename)
    basename = os.path.basename(filename)
    outname = '%s.pdf' % os.path.splitext(basename)[0]
    output_path = os.path.join(output_dir, outname)

    with open(filename, 'rb') as input_file, open(output_path, 'wb') as output_file:
        result = pisa.pisaDocument(input_file, output_file, path=filename)

    if result.err:
        print('Error rendering %s: %s' % (filename, result.err))
        sys.exit(1)
    return output_path


def convert_to_png(infile, output_dir, options):
    if options.debug:
        print('Converting %s to PNG' % infile)
    basename = os.path.basename(infile)
    filename = os.path.splitext(basename)[0]
    outname = '%s.page%%0d.png' % filename
    globname = '%s.page*.png' % filename
    outfile = os.path.join(output_dir, outname)
    exec_cmd(options, options.convert_cmd, '-density', '150', infile, outfile)

    outfiles = glob.glob(os.path.join(output_dir, globname))
    outfiles.sort()
    if options.remove_transparencies:
        for outfile in outfiles:
            # convert transparencies to white background
            # Done after PDF to PNG conversion, as during that conversion this will remove most background colors.
            exec_cmd(options, options.convert_cmd, '-background', 'white', '-alpha', 'remove', outfile, outfile)
    return outfiles


def create_diff_image(srcfile1, srcfile2, output_dir, options):
    if options.debug:
        print('Creating difference image for %s and %s' % (srcfile1, srcfile2))

    outname = '%s.diff%s' % os.path.splitext(srcfile1)
    outfile = os.path.join(output_dir, outname)
    _,result = exec_cmd(options, options.compare_cmd, '-metric', 'ae', srcfile1, srcfile2,'-lowlight-color','white',  '-colorspace', 'RGB', outfile)
    diff_value = int(float(result.strip()))
    if diff_value > 0:
        if not options.quiet:
            print('Image %s differs from reference, value is %i' % (srcfile1, diff_value))
    return outfile, diff_value


def copy_ref_image(srcname, output_dir, options):
    if options.debug:
        print('Copying reference image %s ' % srcname)
    dstname = os.path.basename(srcname)
    dstfile = os.path.join(output_dir, '%s.ref%s' % os.path.splitext(dstname))
    shutil.copyfile(srcname, dstfile)
    return dstfile


def create_thumbnail(filename, options):
    thumbfile = '%s.thumb%s' % os.path.splitext(filename)
    if options.debug:
        print('Creating thumbnail of %s' % filename)
    exec_cmd(options, options.convert_cmd, '-resize', '20%', filename, thumbfile)
    return thumbfile


def render_file(filename, output_dir, ref_dir, options):
    if not options.quiet:
        print('Rendering %s' % filename)
    pdf = render_pdf(filename, output_dir, options)
    pngs = convert_to_png(pdf, output_dir, options)
    if options.create_reference:
        return None, None, 0
    thumbs = [create_thumbnail(png, options) for png in pngs]
    pages = [{'png': p, 'png_thumb': thumbs[i]}
             for i,p in enumerate(pngs)]
    diff_count = 0
    if not options.no_compare:
        for page in pages:
            refsrc = os.path.join(ref_dir, os.path.basename(page['png']))
            if not os.path.isfile(refsrc):
                print('Reference image for %s not found!' % page['png'])
                continue
            page['ref'] = copy_ref_image(refsrc, output_dir, options)
            page['ref_thumb'] = create_thumbnail(page['ref'], options)
            page['diff'], page['diff_value'] = \
                    create_diff_image(page['png'], page['ref'],
                                      output_dir, options)
            page['diff_thumb'] = create_thumbnail(page['diff'], options)
            if page['diff_value']:
                diff_count += 1
    return pdf, pages, diff_count


def exec_cmd(options, *args):
    if options.debug:
        print('Executing %s' % ' '.join(args))
    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    result = proc.communicate()
    if options.debug:
        print(result[0], result[1])
    if proc.returncode:
        print('exec error (%i): %s' % (proc.returncode, result[1]))
        if not options.nofail:
            sys.exit(1)
    return result[0], result[1]


def create_html_file(results, template_file, output_dir, options):
    html = []
    for origin_html, pdf, pages, diff_count in results:
        if options.only_errors and not diff_count:
            continue
        pdfname = os.path.basename(pdf)
        htmlname = os.path.basename(origin_html)
        
        html.append('<div class="result">\n'
                    '<h2><a href="%(pdf)s" class="pdf-file">%(pdf)s</a></h2>\n'
                    '<h2>Generated from <a href="../%(src)s/%(html)s" class="">%(html)s</a></h2>\n'
                    % {'pdf': pdfname, 'html':htmlname, 'src': options.source_dir})
        for i, page in enumerate(pages):
            variables = dict(((k, os.path.basename(v)) for k, v in page.items()
                              if k != 'diff_value'))
            variables['page'] = i + 1
            if 'diff' in page:
                variables['diff_value'] = page['diff_value']
                if variables['diff_value']:
                    variables['class'] = 'result-page-diff error'
                else:
                    if options.only_errors:
                        continue
                    variables['class'] = 'result-page-diff'
                html.append('<div class="%(class)s">\n'
                            '<h3>Page %(page)i</h3>\n'

                            '<div class="result-img">\n'
                            '<div class="result-type">Difference '
                            '(Score %(diff_value)i)</div>\n'
                            '<a href="%(diff)s" class="diff-file">'
                            '<img src="%(diff_thumb)s"/></a>\n'
                            '</div>\n'

                            '<div class="result-img">\n'
                            '<div class="result-type">Rendered</div>\n'
                            '<a href="%(png)s" class="png-file">'
                            '<img src="%(png_thumb)s"/></a>\n'
                            '</div>\n'

                            '<div class="result-img">\n'
                            '<div class="result-type">Reference</div>\n'
                            '<a href="%(ref)s" class="ref-file">'
                            '<img src="%(ref_thumb)s"/></a>\n'
                            '</div>\n'

                            '</div>\n' % variables)
            else:
                html.append('<div class="result-page">\n'
                           '<h3>Page %(page)i</h3>\n'

                           '<div class="result-img">\n'
                           '<a href="%(png)s" class="png-file">'
                           '<img src="%(png_thumb)s"/></a>\n'
                           '</div>\n'

                           '</div>\n' % variables)
        html.append('</div>\n\n')

    now = datetime.datetime.now()
    title = 'xhtml2pdf Test Rendering Results, (Python %s) %s' % (sys.version,now.strftime('%c'))
    template = open(template_file, 'r'+do_bytes).read()
    template = template.replace('%%TITLE%%', title)
    template = template.replace('%%RESULTS%%', '\n'.join(html))

    htmlfile = os.path.join(output_dir, 'index.html')
    outfile = open(htmlfile, 'w'+do_bytes)
    outfile.write(template)
    outfile.close()
    return htmlfile


def main():
    options, args = parser.parse_args()

    base_dir = os.path.abspath(os.path.join(__file__, os.pardir))
    source_dir = os.path.join(base_dir, options.source_dir)
    if options.create_reference is not None:
        output_dir = os.path.join(base_dir, options.create_reference)
    else:
        output_dir = os.path.join(base_dir, options.output_dir)
    template_file = os.path.join(base_dir, options.html_template)
    ref_dir = os.path.join(base_dir, options.ref_dir)

    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

    results = []
    diff_count = 0
    if len(args) == 0:
        files = glob.glob(os.path.join(source_dir, '*.html'))
    else:
        files = [os.path.join(source_dir, arg) for arg in args]
    for filename in files:
        pdf, pages, diff = render_file(filename, output_dir, ref_dir, options)
        diff_count += diff
        results.append((filename, pdf, pages, diff))

    num = len(results)

    if options.create_reference is not None:
        print('Created reference for %i file%s' % (num, '' if num == 1 else 's'))
    else:
        htmlfile = create_html_file(results, template_file, output_dir, options)
        if not options.quiet:
            print('Rendered %i file%s' % (num, '' if num == 1 else 's'))
            print('%i file%s differ%s from reference' % \
                    (diff_count, diff_count != 1 and 's' or '',
                     diff_count == 1 and 's' or ''))
            print('Check %s for results' % htmlfile)
        if diff_count:
            if options.nofail:
                print("Differences were found but the error code is suppressed.")
                sys.exit(0)
            else:
                sys.exit(1)


parser = OptionParser(
    usage='rendertest.py [options] [source_file] [source_file] ...',
    description='Renders a single html source file or all files in the data '
    'directory, converts them to PNG format and prepares a result '
    'HTML file for comparing the output with an expected result')
parser.add_option('-s', '--source-dir', dest='source_dir', default='data/source',
                  help=('Path to directory containing the html source files'))
parser.add_option('-o', '--output-dir', dest='output_dir', default='output',
                  help='Path to directory for output files. CAREFUL: this '
                  'directory will be deleted and recreated before rendering!')
parser.add_option('-r', '--ref-dir', dest='ref_dir', default='data/reference',
                  help='Path to directory containing the reference images '
                  'to compare the result with')
parser.add_option('-t', '--template', dest='html_template',
                  default='data/template.html', help='Name of HTML template file')
parser.add_option('-e', '--only-errors', dest='only_errors', action='store_true',
                  default=False, help='Only include images in HTML file which '
                  'differ from reference')
parser.add_option('-q', '--quiet', dest='quiet', action='store_true',
                  default=False, help='Try to be quiet')
parser.add_option('-F', '--nofail', dest='nofail', action='store_true',
                  default=False, help="Doesn't return an error on failure "
                  "this useful when calling it in scripts"
                  )
parser.add_option('-X', '--remove_transparencies', dest='remove_transparencies', action='store_false',
                  default=True, help="Don't try to remove transparent backgrounds "
                  "Needed for Travis-CI"
                  )

parser.add_option('--no-compare', dest='no_compare', action='store_true',
                  default=False, help='Do not compare with reference image, '
                  'only render to png')
parser.add_option('-c', '--create-reference', dest='create_reference',
                  metavar='DIR',
                  default=None, help='Do not output anything, render source to '
                  'specified directory for reference. CAREFUL: this directory '
                 'will be deleted and recreated before rendering!')
parser.add_option('--debug', dest='debug', action='store_true',
                  default=False, help='More output for debugging')
parser.add_option('--convert-cmd', dest='convert_cmd', default='/usr/bin/convert',
                  help='Path to ImageMagick "convert" tool')
parser.add_option('--compare-cmd', dest='compare_cmd', default='/usr/bin/compare',
                  help='Path to ImageMagick "compare" tool')

if __name__ == '__main__':
    main()
