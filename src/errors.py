class AssemblyError(Exception):
    """Custom exception for assembly errors."""
    pass

class InvalidOperationError(AssemblyError):
    """Exception raised for invalid operations."""
    pass