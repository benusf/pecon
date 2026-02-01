from types import ModuleType
from typing import Any, Literal

import numpy as np
import numpy.typing as npt

from pecon._lib.array_api_compat import (
    is_array_api_obj,
    is_lazy_array,
    is_numpy_array,
    is_cupy_array,
    is_torch_array,
    is_jax_array,
    is_dask_array,
    size as xp_size,
    numpy as np_compat,
    device as xp_device,
    is_numpy_namespace as is_numpy,
    is_cupy_namespace as is_cupy,
    is_torch_namespace as is_torch,
    is_jax_namespace as is_jax,
    is_dask_namespace as is_dask,
    is_array_api_strict_namespace as is_array_api_strict,
)
from pecon._lib.array_api_compat.common._helpers import _compat_module_name
from pecon._lib.array_api_extra.testing import lazy_xp_function
from pecon._lib._array_api_override import array_namespace
from pecon._lib import array_api_extra as xpx
