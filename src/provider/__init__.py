from .provider import Provider

# Export the Provider creator function
provider = Provider.create

# Export these explicitly for usage in rxconfig.py
__all__ = ["Provider", "provider"]
