from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy

# Include directories
include_dirs = ["pecon/include", numpy.get_include()]

# Extensions
extensions = [
    Extension(
        "pecon._core",
        sources=[
            "pecon/_core.pyx",  # use .pyx, Cython will generate .c
            "pecon/src/pecon_ols.c",
            "pecon/src/pecon_math.c",
            "pecon/src/pecon_stats.c",
        ],
        include_dirs=include_dirs,
        language="c",
    ),
    Extension(
        "pecon.stats.basic_stats",
        sources=[
            "pecon/stats/basic_stats.pyx",  # use .pyx
            "pecon/src/pecon_ols.c",
            "pecon/src/pecon_math.c",
            "pecon/src/pecon_stats.c",
        ],
        include_dirs=include_dirs,
        language="c",
    ),
]

setup(
    name="pecon",
    version="0.1.0",
    packages=find_packages(),
    ext_modules=cythonize(
        extensions,
        compiler_directives={"language_level": "3", "boundscheck": False},
        annotate=True  # optional, generates HTML for optimization hints
    ),
)

