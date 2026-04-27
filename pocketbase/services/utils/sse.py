from __future__ import annotations

import dataclasses
import threading
from collections.abc import Callable
from typing import Any

import httpx


@dataclasses.dataclass
class Event:
    """Representation of an event"""

    id: str = ""
    event: str = "message"
    data: str = ""
    retry: int | None = None


class EventLoop(threading.Thread):
    FIELD_SEPARATOR = ":"

    def __init__(
        self,
        url: str,
        method: str = "GET",
        headers: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        encoding: str = "utf-8",
        listeners: dict[str, Callable[[Event], Any]] | None = None,
        **kwargs: Any,
    ):
        threading.Thread.__init__(self, **kwargs)
        self.kill = False
        self.client = httpx.Client()
        self.url = url
        self.method = method
        self.headers = headers
        self.payload = payload
        self.encoding = encoding
        self.listeners = listeners or {}

    def _read(self):
        """Read the incoming event source stream and yield event chunks"""
        pass

    def _events(self):
        pass

    def run(self):
        pass


class SSEClient:
    """Implementation of a server side event client"""

    _listeners: dict[str, Callable[[Event], Any]]
    _loop_thread: EventLoop

    def __init__(
        self,
        url: str,
        method: str = "GET",
        headers: dict[str, Any] | None = None,
        payload: dict[str, Any] | None = None,
        encoding: str = "utf-8",
    ) -> None:
        self._listeners = {}
        self._loop_thread = EventLoop(
            url=url,
            method=method,
            headers=headers,
            payload=payload,
            encoding=encoding,
            listeners=self._listeners,
            name="loop",
        )
        self._loop_thread.daemon = True
        self._loop_thread.start()

    def add_event_listener(
        self, event: str, callback: Callable[[Any], None]
    ) -> None:
        pass

    def remove_event_listener(
        self, event: str, callback: Callable[[Any], None]
    ) -> None:
        pass

    def close(self) -> None:
        # TODO: does not work like this
        pass
