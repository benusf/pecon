# pecon/warnings.py
import warnings

class PeConWarning(UserWarning):
    """Base class for all PeCon warnings."""
    pass


class DimensionWarning(PeConWarning):
    """Raised when input dimensions are auto-corrected."""
    pass


class SingularMatrixWarning(PeConWarning):
    """Raised when matrix is singular or ill-conditioned."""
    pass


class ConvergenceWarning(PeConWarning):
    """Raised when an iterative algorithm fails to converge."""
    pass

