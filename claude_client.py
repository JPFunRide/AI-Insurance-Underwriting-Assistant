import os
import anthropic

from config import ANTHROPIC_API_KEY, CLAUDE_MODEL, MAX_TOKENS


class ClaudeClient:
    """Wrapper class for calling Claude models via the Anthropic API."""

    def __init__(self, api_key: str = None, model: str = None, max_tokens: int = None):
        """
        Initialize the Claude client.

        Args:
            api_key (str, optional): Anthropic API key. If None, will default to ANTHROPIC_API_KEY from config.
            model (str, optional): Claude model name. If None, will default to CLAUDE_MODEL from config.
            max_tokens (int, optional): Maximum tokens to generate. If None, will default to MAX_TOKENS from config.
        """
        self.api_key = api_key or ANTHROPIC_API_KEY
        self.model = model or CLAUDE_MODEL
        self.max_tokens = max_tokens or MAX_TOKENS
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def call_claude(self, prompt: str) -> str:
        """
        Send a prompt to Claude and return the assistant's response content.

        Args:
            prompt (str): The prompt string to send to the model.

        Returns:
            str: Claude's response content.
        """
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content.strip()
        except Exception as e:
            # In a real application, you might want to log this exception
            raise RuntimeError(f"Error calling Claude: {e}") from e


# Singleton instance that can be imported elsewhere
claude_client = ClaudeClient()
