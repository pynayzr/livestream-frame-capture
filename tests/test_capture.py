# -*- coding: utf-8 -*-

import imghdr
import tempfile
import unittest
import streamlink
import pylivecap
from pylivecap import VideoQuality as VQ


YOUTUBE_360_VIDEO = 'https://www.youtube.com/watch?v=_nfp0lLGHao'
YOUTUBE_PTS_LIVESTREAM = 'https://www.youtube.com/watch?v=zjGR32QyTkQ'


class TestCapture(unittest.TestCase):
    def test_capture_360p_with_jpeg_format_from_youtube_livestream_should_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            pylivecap.capture(YOUTUBE_PTS_LIVESTREAM, output, VQ.Q1080)
            self.assertEqual(imghdr.what(output), 'jpeg')

    def test_capture_1080p_with_jpeg_format_from_youtube_livestream_should_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            pylivecap.capture(YOUTUBE_PTS_LIVESTREAM, output, VQ.Q1080)
            self.assertEqual(imghdr.what(output), 'jpeg')

    def test_capture_1080p_with_png_format_from_youtube_livestream_should_success(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.png' % (temp_dir)
            pylivecap.capture(YOUTUBE_PTS_LIVESTREAM, output, VQ.Q1080)
            self.assertEqual(imghdr.what(output), 'png')

    def test_capture_should_return_output_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            ret = pylivecap.capture(YOUTUBE_PTS_LIVESTREAM, output, VQ.Q1080)
            self.assertEqual(ret, output)


class TestSaveCaptureException(unittest.TestCase):
    def test_video_quality_1080p_not_in_youtube_360_should_raise_value_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            with self.assertRaises(ValueError):
                pylivecap.safe_capture(YOUTUBE_360_VIDEO, output, quality=VQ.Q1080)

    def test_not_support_url_should_raise_no_plugin_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            with self.assertRaises(streamlink.exceptions.NoPluginError):
                pylivecap.safe_capture('', output)

    def test_not_exist_output_path_should_raise_permission_error(self):
        with self.assertRaises(PermissionError):
            pylivecap.safe_capture(YOUTUBE_PTS_LIVESTREAM, '/path/not/exists')
