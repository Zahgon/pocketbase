from __future__ import annotations

from typing import Sequence, Union

from httpx._types import FileTypes

FileUploadTypes = Union[FileTypes, Sequence[FileTypes]]


class FileUpload:
    def __init__(self, *args: FileUploadTypes):
        self.files = args

    def get(self, key: str):
        pass
