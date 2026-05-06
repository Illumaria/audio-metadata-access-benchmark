import struct
from pathlib import Path

from mutagen.ogg import OggPage
from mutagen.oggopus import (
    OggOpus as _OggOpus,
    OggOpusHeaderError,
)
from mutagen._file import StreamInfo


class OggOpusInfo(StreamInfo):
    length = 0.0
    channels = 0
    sample_rate = 0.0

    def __init__(self, fileobj) -> None:
        page = OggPage(fileobj)
        while not page.packets[0].startswith(b"OpusHead"):
            page = OggPage(fileobj)

        self.serial = page.serial

        if not page.first:
            raise OggOpusHeaderError("page has ID header, but doesn't start a stream")

        (
            version,
            self.channels,
            pre_skip,
            self.sample_rate,
            _,
            _,
        ) = struct.unpack("<BBHIhB", page.packets[0][8:19])

        self.__pre_skip = pre_skip

        # only the higher 4 bits change on incombatible changes
        major = version >> 4
        if major != 0:
            raise OggOpusHeaderError("version %r unsupported" % major)

    def _post_tags(self, fileobj):
        page = OggPage.find_last(fileobj, self.serial, finishing=True)
        if page is None:
            raise OggOpusHeaderError
        self.length = (page.position - self.__pre_skip) / float(48000)

    def pprint(self):
        return "Ogg Opus, %.2f seconds" % (self.length)


class OggOpus(_OggOpus):
    _Info = OggOpusInfo


def get_info(path: Path) -> tuple[float, float]:
    info = OggOpus(path).info
    duration = info.length or 0.0
    sample_rate = info.sample_rate or 0.0
    return duration, sample_rate
