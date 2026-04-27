from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import urlparse
from typing import TYPE_CHECKING
import re

if TYPE_CHECKING:
    from lxml.html import HtmlElement
    from bs4 import BeautifulSoup


@dataclass
class Metadata:
    title: str | None
    description: str | None
    thumbnail: str | None
    author: str | None
    keywords: tuple[str] | None
    twitter_handle: str | None
    robots: tuple[str] | None
    canonical: str | None


PARSER_IMPORT_SOLUTION = "Install it using 'pip install stealth-requests[parsers]'."


class StealthResponse:
    def __init__(self, resp, elapsed):
        self._response = resp
        self._elapsed = elapsed

        self._tree: HtmlElement | None = None
        self._important_meta_tags: Metadata | None = None
        self._links: tuple[str] = tuple()
        self._images: tuple[str] = tuple()
        self._tables: list[dict[str, list[str]]] | None = None

    def __getattr__(self, name):
        return getattr(self._response, name)

    def __repr__(self):
        return f'<StealthResponse [Status: {self._response.status_code} Elapsed Time: {self._elapsed:.2f} seconds]>'

    def _get_tree(self) -> HtmlElement:
        pass

    @staticmethod
    def _format_meta_list(content: str) -> tuple[str]:
        pass

    def _set_important_meta_tags(self) -> Metadata:
        pass

    def _parse_links(self, tag: str) -> tuple[str]:
        pass

    def tree(self) -> HtmlElement:
        pass

    def soup(self, parser: str = 'html.parser') -> BeautifulSoup:
        pass

    def markdown(self, content_xpath: str | None = None, ignore_links: bool = True):
        pass

    def xpath(self, xp: str):
        pass

    def iterlinks(self, *args, **kwargs):
        pass

    def itertext(self, *args, **kwargs):
        pass

    def text_content(self, *args, **kwargs):
        pass

    @property
    def meta(self):
        pass

    @property
    def images(self) -> tuple[str]:
        pass

    @property
    def links(self) -> tuple[str]:
        pass

    @staticmethod
    def _parse_table(table_element) -> dict[str, list[str]] | None:
        pass

    @property
    def tables(self) -> list[dict[str, list[str]]]:
        pass

    @property
    def emails(self) -> tuple[str]:
        pass

    @property
    def phone_numbers(self) -> tuple[str]:
        pass
