import os

# Load environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Claude model to use
CLAUDE_MODEL = "claude-3-sonnet-20240229"

# Maximum tokens for Claude responses
MAX_TOKENS = 500

# Additional configuration options can be added here
