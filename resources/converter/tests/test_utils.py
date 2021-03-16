# -*- coding: utf-8 -*-
from unittest import TestCase

from reportlab.lib.colors import Color

from xhtml2pdf.tags import int_to_roman
from xhtml2pdf.util import (copy_attrs, getBorderStyle, getBox, getColor, getCoords, getFrameDimensions, getSize,
                            pisaTempFile, set_value, transform_attrs)


class UtilsCoordTestCase(TestCase):

    def test_getCoords_simple(self):

        res = getCoords(1, 1, 10, 10, (10, 10))
        self.assertEqual(res, (1, -1, 10, 10))

        # A second time - it's memoized!
        res = getCoords(1, 1, 10, 10, (10, 10))
        self.assertEqual(res, (1, -1, 10, 10))

    def test_getCoords_x_lt_0(self):
        res = getCoords(-1, 1, 10, 10, (10, 10))
        self.assertEqual(res, (9, -1, 10, 10))

    def test_getCoords_y_lt_0(self):
        res = getCoords(1, -1, 10, 10, (10, 10))
        self.assertEqual(res, (1, -9, 10, 10))

    def test_getCoords_w_and_h_none(self):
        res = getCoords(1, 1, None, None, (10, 10))
        self.assertEqual(res, (1, 9))

    def test_getCoords_w_lt_0(self):
        res = getCoords(1, 1, -1, 10, (10, 10))
        self.assertEqual(res, (1, -1, 8, 10))

    def test_getCoords_h_lt_0(self):
        res = getCoords(1, 1, 10, -1, (10, 10))
        self.assertEqual(res, (1, 1, 10, 8))


class UtilsColorTestCase(TestCase):

    def test_get_color_simple(self):
        res = getColor('red')
        self.assertEqual(res, Color(1, 0, 0, 1))

        # Testing it being memoized properly
        res = getColor('red')
        self.assertEqual(res, Color(1, 0, 0, 1))

    def test_get_color_from_color(self):
        # Noop if argument is already a color
        res = getColor(Color(1, 0, 0, 1))
        self.assertEqual(res, Color(1, 0, 0, 1))

    def test_get_transparent_color(self):
        res = getColor('transparent', default='TOKEN')
        self.assertEqual(res, 'TOKEN')

        res = getColor('none', default='TOKEN')
        self.assertEqual(res, 'TOKEN')

    def test_get_color_for_none(self):
        res = getColor(None, default='TOKEN')
        self.assertEqual(res, 'TOKEN')

    def test_get_color_for_RGB(self):
        res = getColor('#FF0000')
        self.assertEqual(res, Color(1, 0, 0, 1))

    def test_get_color_for_RGB_with_len_4(self):
        res = getColor('#F00')
        self.assertEqual(res, Color(1, 0, 0, 1))

    def test_get_color_for_CSS_RGB_function(self):
        # It's regexp based, let's try common cases.
        res = getColor('rgb(255,0,0)')
        self.assertEqual(res, Color(1, 0, 0, 1))

        res = getColor('<css function: rgb(255,0,0)>')
        self.assertEqual(res, Color(1, 0, 0, 1))


class UtilsGetSizeTestCase(TestCase):

    def test_get_size_simple(self):
        res = getSize('12pt')
        self.assertEqual(res, 12.00)

        # Memoized...
        res = getSize('12pt')
        self.assertEqual(res, 12.00)

    def test_get_size_for_none(self):
        res = getSize(None, relative='TOKEN')
        self.assertEqual(res, 'TOKEN')

    def test_get_size_for_float(self):
        res = getSize(12.00)
        self.assertEqual(res, 12.00)

    def test_get_size_for_tuple(self):
        # TODO: This is a really strange case. Probably should not work this
        # way.
        res = getSize(("12", ".12"))
        self.assertEqual(res, 12.12)

    def test_get_size_for_cm(self):
        res = getSize("1cm")
        self.assertEqual(res, 28.346456692913385)

    def test_get_size_for_mm(self):
        res = getSize("1mm")
        self.assertEqual(res, 2.8346456692913385)

    def test_get_size_for_in(self):
        res = getSize("1in")
        self.assertEqual(res, 72.00)

    def test_get_size_for_inch(self):
        res = getSize("1in")
        self.assertEqual(res, 72.00)

    def test_get_size_for_pc(self):
        res = getSize("1pc")
        self.assertEqual(res, 12.00)

    def test_get_size_for_none_str(self):
        res = getSize("none")
        self.assertEqual(res, 0.0)
        res = getSize("0")
        self.assertEqual(res, 0.0)
        res = getSize("auto")  # Really?
        self.assertEqual(res, 0.0)


class PisaDimensionTestCase(TestCase):

    def test_FrameDimensions_left_top_width_height(self):
        dims = {
            'left': '10pt',
            'top': '20pt',
            'width': '30pt',
            'height': '40pt',
        }
        expected = (10.0, 20.0, 30.0, 40.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)

    def test_FrameDimensions_left_top_bottom_right(self):
        dims = {
            'left': '10pt',
            'top': '20pt',
            'bottom': '30pt',
            'right': '40pt',
        }
        expected = (10.0, 20.0, 50.0, 150.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)

    def test_FrameDimensions_bottom_right_width_height(self):
        dims = {
            'bottom': '10pt',
            'right': '20pt',
            'width': '70pt',
            'height': '80pt',
        }
        expected = (10.0, 110.0, 70.0, 80.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)

    def test_FrameDimensions_left_top_width_height_with_margin(self):
        dims = {
            'left': '10pt',
            'top': '20pt',
            'width': '70pt',
            'height': '80pt',
            'margin-top': '10pt',
            'margin-left': '15pt',
            'margin-bottom': '20pt',
            'margin-right': '25pt',
        }
        expected = (25.0, 30.0, 30.0, 50.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)

    def test_FrameDimensions_bottom_right_width_height_with_margin(self):
        dims = {
            'bottom': '10pt',
            'right': '20pt',
            'width': '70pt',
            'height': '80pt',
            'margin-top': '10pt',
            'margin-left': '15pt',
            'margin-bottom': '20pt',
            'margin-right': '25pt',
        }
        expected = (25.0, 120.0, 30.0, 50.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)

    def test_frame_dimensions_for_box_len_eq_4(self):
        dims = {
            '-pdf-frame-box': ['12pt', '12,pt', '12pt', '12pt']
        }
        expected = [12.0, 12.0, 12.0, 12.0]
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(result, expected)

    def test_trame_dimentions_for_height_without_top_or_bottom(self):
        dims = {
            'left': '10pt',
            #'top': '20pt',
            'width': '30pt',
            'height': '40pt',
        }
        expected = (10.0, 0.0, 30.0, 200.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)

    def test_trame_dimentions_for_width_without_left_or_right(self):
        dims = {
            #'left': '10pt',
            'top': '20pt',
            'width': '30pt',
            'height': '40pt',
        }
        expected = (0.0, 20.0, 100.0, 40.0)
        result = getFrameDimensions(dims, 100, 200)
        self.assertEqual(expected, result)


class GetPosTestCase(TestCase):

    def test_get_pos_simple(self):
        res = getBox("1pt 1pt 10pt 10pt", (10, 10))
        self.assertEqual(res, (1.0, -1.0, 10, 10))

    def test_get_pos_raising(self):
        raised = False
        try:
            getBox("1pt 1pt 10pt", (10, 10))
        except Exception:
            raised = True
        self.assertTrue(raised)


class TestTagUtils(TestCase):

    def test_roman_numeral_conversion(self):
        self.assertEqual("I", int_to_roman(1))
        self.assertEqual("L", int_to_roman(50))
        self.assertEqual("XLII", int_to_roman(42))
        self.assertEqual("XXVI", int_to_roman(26))


class TempFileTestCase(TestCase):

    def test_unicode(self):
        """Asserts bytes generated by reportlab are returned"""
        src = pisaTempFile()
        value = b'%PDF-1.4\r\n%\x93\x8c\x8b\x9e ReportLab Generated PDF document http://www.reportlab.com'
        try:
            src.write(value)
        except UnicodeDecodeError as error:
            self.fail(error)


class GetBorderStyleTestCase(TestCase):

    def test_will_return_value_if_passed_value_is_not_none_or_hidden(self):
        style = getBorderStyle("foo", default="blah")
        self.assertEqual(style, "foo")

    def test_will_return_default_if_passed_value_is_non_case_sensitive_none(self):
        style = getBorderStyle("None", default="blah")
        self.assertEqual(style, "blah")

    def test_will_return_default_if_passed_value_is_non_case_sensitive_hidden(self):
        style = getBorderStyle("hidDen", default="defaultPassedArg")
        self.assertEqual(style, "defaultPassedArg")


class CopyUtils(TestCase):

    class A:
        attr = 2
        attr1 = 10

    class B:

        def __init__(self, a, b):
            self.attr = a
            self.attr1 = b

    class C:
        pass

    class D:
        param1 = 28
        param2 = 1

    def test_set_value(self):

        a = self.A()
        b = self.B(20, 30)
        c = self.C()
        set_value(a, ["attr", "attr1"], 8)
        set_value(b, ["attr", "attr1"], 8)
        set_value(c, ["attr", "attr1"], 8)

        self.assertEqual(a.attr, 8)
        self.assertEqual(a.attr1, 8)
        self.assertEqual(b.attr, 8)
        self.assertEqual(b.attr1, 8)
        self.assertEqual(c.attr, 8)
        self.assertEqual(c.attr1, 8)

    def test_copy_attrs(self):
        a = self.A()
        b = self.B(19, 22)
        copy_attrs(a, b, ["attr", "attr1"])
        self.assertEqual(a.attr, 19)
        self.assertEqual(a.attr1, 22)

    def test_transform_attrs(self):
        obj = self.D()
        container = {'attr': 19, 'attr1': 22}

        transform_attrs(obj,
                        (("param1", "attr"),
                         ("param2", "attr1"),),
                        container,
                        str)

        self.assertEqual(obj.param1, str(19))
        self.assertEqual(obj.param2, str(22))
