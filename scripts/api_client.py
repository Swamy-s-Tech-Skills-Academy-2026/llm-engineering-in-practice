"""API client helpers for OpenAI and Azure OpenAI.

Loads credentials from .env and exposes get_openai_client(), get_azure_openai_client(),
and test_api_connection() for use in notebooks and scripts.
"""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# Resolve .env from repo root (parent of scripts/)
_REPO_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_REPO_ROOT / ".env")


def get_openai_client():
    """Initialize and return OpenAI client using OPENAI_API_KEY from environment."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    from openai import OpenAI
    return OpenAI(api_key=api_key)


def get_azure_openai_client():
    """Initialize and return Azure OpenAI client using env vars."""
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    if not endpoint or not api_key:
        raise ValueError("Azure OpenAI credentials not found in .env file")
    from openai import AzureOpenAI
    return AzureOpenAI(
        api_key=api_key,
        azure_endpoint=endpoint,
        api_version=api_version,
    )


def test_api_connection(provider: str = "openai") -> bool:
    """Send a minimal chat request to verify the given provider works."""
    try:
        if provider == "openai":
            client = get_openai_client()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Say hello!"}],
                max_tokens=10,
            )
        elif provider == "azure_openai":
            client = get_azure_openai_client()
            deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-35-turbo")
            response = client.chat.completions.create(
                model=deployment,
                messages=[{"role": "user", "content": "Say hello!"}],
                max_tokens=10,
            )
        else:
            raise ValueError(f"Unknown provider: {provider}")
        print(f"✅ {provider.upper()} API connection successful!")
        print(f"Response: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ {provider.upper()} API connection failed: {e}")
        return False


if __name__ == "__main__":
    print("Testing OpenAI...")
    test_api_connection("openai")
    print("\nTesting Azure OpenAI...")
    test_api_connection("azure_openai")
