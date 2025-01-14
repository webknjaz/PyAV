from av.video.reformatter import ColorRange, Colorspace
import av

from .common import TestCase, fate_suite


class TestColorSpace(TestCase):
    def test_color_range(self):
        container = av.open(
            fate_suite("amv/MTV_high_res_320x240_sample_Penguin_Joke_MTV_from_WMV.amv")
        )
        stream = container.streams.video[0]

        self.assertEqual(stream.color_range, None)

        for packet in container.demux(stream):
            for frame in packet.decode():
                self.assertEqual(frame.color_range, ColorRange.JPEG)  # a.k.a "pc"
                self.assertEqual(frame.colorspace, Colorspace.ITU601)
                return
