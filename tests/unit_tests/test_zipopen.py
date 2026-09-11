"""Behavioural tests for pypipegzip.zipopen (gzip path)."""

import gzip
import os
import tempfile
import unittest

from pypipegzip.pypipegzip import zipopen


class ZipopenTests(unittest.TestCase):
    def test_write_then_read_binary_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            name = os.path.join(d, "data.gz")
            payload = b"hello pypipegzip\n" * 100
            with zipopen(name, mode="wb") as stream:
                stream.write(payload)
            with zipopen(name, mode="rb") as stream:
                self.assertEqual(stream.read(), payload)

    def test_write_then_read_text_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            name = os.path.join(d, "data.gz")
            with zipopen(name, mode="wt") as stream:
                stream.write("line one\nline two\n")
            with zipopen(name, mode="rt") as stream:
                self.assertEqual(stream.read(), "line one\nline two\n")

    def test_invalid_mode_raises(self):
        with tempfile.TemporaryDirectory() as d:
            name = os.path.join(d, "data.gz")
            with self.assertRaises(ValueError):
                zipopen(name, mode="x")

    def test_read_produces_real_gzip(self):
        # a file written by zipopen must be a valid gzip file on disk
        with tempfile.TemporaryDirectory() as d:
            name = os.path.join(d, "data.gz")
            with zipopen(name, mode="wb") as stream:
                stream.write(b"gzip content")
            with gzip.open(name, mode="rb") as stream:
                self.assertEqual(stream.read(), b"gzip content")
