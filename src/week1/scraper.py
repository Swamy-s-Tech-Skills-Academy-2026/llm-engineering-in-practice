"""Simple web scraper utility for LLM Engineering course.

This module provides basic website content extraction functionality.
Based on the original course implementation with improvements.
"""
from __future__ import annotations

from typing import List

import requests
from bs4 import BeautifulSoup

# Standard headers to fetch a website
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    )
}


def fetch_website_contents(url: str) -> str:
    """Return the title and main text of the page at url; truncated to 2,000 chars.

    Args:
        url: Page URL to fetch.
    Returns:
        Concatenated title and body text, up to 2,000 characters.
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title found"
    if soup.body:
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]


def fetch_website_links(url: str) -> List[str]:
    """Return the href values of all links on the page.

    Args:
        url: Page URL to fetch.
    Returns:
        List of link href strings (empty strings omitted).
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]


if __name__ == "__main__":
    # Simple test
    try:
        content = fetch_website_contents("https://httpbin.org/html")
        print(f"Successfully fetched {len(content)} characters")
        print(content[:200] + "..." if len(content) > 200 else content)
    except Exception as e:
        print(f"Test failed: {e}")
