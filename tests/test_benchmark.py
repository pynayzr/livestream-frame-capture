# -*- coding: utf-8 -*-

import timeit
import tempfile
import pylivecap

YOUTUBE_VIDEO = 'https://www.youtube.com/watch?v=HvHFV244Wxg'
YOUTUBE_PTS_LIVESTREAM = 'https://www.youtube.com/watch?v=zjGR32QyTkQ'


def bench_safe_capture_from_livestream():
    def bench_safe_capture():
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            pylivecap.safe_capture(YOUTUBE_PTS_LIVESTREAM, output)

    ret = timeit.timeit(bench_safe_capture, number=5)
    print('>>> Safe Capture 5 image from YouTube Live Streaming: %.3fs' % (ret))


def bench_capture_from_livestream():
    def bench_capture():
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            pylivecap.capture(YOUTUBE_PTS_LIVESTREAM, output)

    ret = timeit.timeit(bench_capture, number=5)
    print('>>> Capture 5 image from YouTube Live Streaming: %.3fs' % (ret))


def bench_safe_capture_from_video():
    def bench_safe_capture():
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            pylivecap.safe_capture(YOUTUBE_VIDEO, output)

    ret = timeit.timeit(bench_safe_capture, number=5)
    print('>>> Safe Capture 5 image from YouTube Video: %.3fs' % (ret))


def bench_capture_from_video():
    def bench_capture():
        with tempfile.TemporaryDirectory() as temp_dir:
            output = '%s/out.jpg' % (temp_dir)
            pylivecap.capture(YOUTUBE_VIDEO, output)

    ret = timeit.timeit(bench_capture, number=5)
    print('>>> Capture 5 image from YouTube Video: %.3fs' % (ret))


if __name__ == '__main__':
    bench_safe_capture_from_livestream()
    bench_capture_from_livestream()
    bench_safe_capture_from_video()
    bench_capture_from_video()
