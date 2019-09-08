# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from feast.types.FeatureRow_pb2 import (
    FeatureRow as feast___types___FeatureRow_pb2___FeatureRow,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class Error(google___protobuf___message___Message):
    cause = ... # type: typing___Text
    transform = ... # type: typing___Text
    message = ... # type: typing___Text
    stackTrace = ... # type: typing___Text

    def __init__(self,
        cause : typing___Optional[typing___Text] = None,
        transform : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        stackTrace : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Error: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"cause",u"message",u"stackTrace",u"transform"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"cause",b"message",b"stackTrace",b"transform"]) -> None: ...

class Attempt(google___protobuf___message___Message):
    attempts = ... # type: int

    @property
    def error(self) -> Error: ...

    def __init__(self,
        attempts : typing___Optional[int] = None,
        error : typing___Optional[Error] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Attempt: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"attempts",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"error",b"error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"attempts",b"error"]) -> None: ...

class FeatureRowExtended(google___protobuf___message___Message):

    @property
    def row(self) -> feast___types___FeatureRow_pb2___FeatureRow: ...

    @property
    def lastAttempt(self) -> Attempt: ...

    @property
    def firstSeen(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    def __init__(self,
        row : typing___Optional[feast___types___FeatureRow_pb2___FeatureRow] = None,
        lastAttempt : typing___Optional[Attempt] = None,
        firstSeen : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FeatureRowExtended: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"firstSeen",u"lastAttempt",u"row"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"firstSeen",u"lastAttempt",u"row"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"firstSeen",b"firstSeen",u"lastAttempt",b"lastAttempt",u"row",b"row"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"firstSeen",b"lastAttempt",b"row"]) -> None: ...