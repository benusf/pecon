import numpy as np
import numpy.typing as npt
from types import ModuleType

from pecon._lib import array_api_compat
import pecon._lib.array_api_compat.numpy as np_compat





from typing import Any


def array_namespace(*arrays: Array) -> ModuleType:
    """Get the array API compatible namespace for the arrays xs.

    Parameters
    ----------
    *arrays : sequence of array_like
        Arrays used to infer the common namespace.

    Returns
    -------
    namespace : module
        Common namespace.
    """
    # TODO 

    
