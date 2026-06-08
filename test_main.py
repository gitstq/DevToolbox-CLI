#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DevToolbox-CLI — Unit Tests
"""

import unittest
import json
import base64
import hashlib
import uuid
import sys
import os
import io
from unittest.mock import patch

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import main


class TestJsonCommand(unittest.TestCase):
    def test_format_json(self):
        raw = '{"b":1,"a":2}'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'json', '--format']):
                with patch('sys.stdin', io.StringIO(raw)):
                    main.main()
        out = fake_out.getvalue()
        self.assertIn('"a": 2', out)
        self.assertIn('"b": 1', out)

    def test_minify_json(self):
        raw = '{"a": 1, "b": 2}'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'json', '--minify']):
                with patch('sys.stdin', io.StringIO(raw)):
                    main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, '{"a":1,"b":2}')

    def test_invalid_json(self):
        raw = '{invalid'
        with patch('sys.stdout', new=io.StringIO()):
            with patch.object(sys, 'argv', ['devtoolbox', 'json', '--format']):
                with patch('sys.stdin', io.StringIO(raw)):
                    rc = main.main()
        self.assertEqual(rc, 1)


class TestBase64Command(unittest.TestCase):
    def test_encode(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'base64', '--input', 'hello']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, base64.b64encode(b'hello').decode())

    def test_decode(self):
        encoded = base64.b64encode(b'hello').decode()
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'base64', '--decode', '--input', encoded]):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, 'hello')


class TestHashCommand(unittest.TestCase):
    def test_md5(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'hash', '--algo', 'md5', '--input', 'test']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, hashlib.md5(b'test').hexdigest())

    def test_sha256(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'hash', '--input', 'test']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, hashlib.sha256(b'test').hexdigest())


class TestUUIDCommand(unittest.TestCase):
    def test_uuid_v4(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'uuid', '--count', '1']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertTrue(len(out) == 36)
        # Verify it's a valid UUID
        uuid.UUID(out)


class TestTimeCommand(unittest.TestCase):
    def test_to_iso(self):
        ts = "1717776000"
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'time', '--to-iso', ts]):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertIn("2024-06-07", out)

    def test_now(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'time', '--now']):
                main.main()
        out = fake_out.getvalue()
        self.assertIn("UTC:", out)
        self.assertIn("Timestamp:", out)


class TestColorCommand(unittest.TestCase):
    def test_hex_to_rgb(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'color', '--hex-to-rgb', '#FF8000']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, "RGB: (255, 128, 0)")

    def test_rgb_to_hex(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'color', '--rgb-to-hex', '255,128,0']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, "HEX: #ff8000")


class TestPasswordCommand(unittest.TestCase):
    def test_length(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'password', '--length', '20']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(len(out), 20)


class TestHTMLCommand(unittest.TestCase):
    def test_escape(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'html', '--input', '<div>hello</div>']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, "&lt;div&gt;hello&lt;/div&gt;")

    def test_unescape(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            with patch.object(sys, 'argv', ['devtoolbox', 'html', '--unescape', '--input', '&lt;div&gt;hello&lt;/div&gt;']):
                main.main()
        out = fake_out.getvalue().strip()
        self.assertEqual(out, "<div>hello</div>")


if __name__ == "__main__":
    unittest.main()
