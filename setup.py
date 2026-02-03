from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy

include_dirs = [
    "pecon/_libs/include",
    numpy.get_include(),
]

extensions = [
    Extension(
        "pecon.stats.basic_stats",
    sources=[
            "pecon/stats/basic_stats.pyx",
            "pecon/_libs/src/pecon_stats.c",
        ],
        include_dirs=include_dirs,
        language="c",
    ),
    Extension(
        "pecon.regression._regression",
    sources=[
            "pecon/regression/_regression.pyx",
            "pecon/_libs/src/pecon_ols.c",
            "pecon/_libs/src/pecon_stats.c",
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
        compiler_directives={
            "language_level": "3",
            "boundscheck": False,
            "wraparound": False,
            "cdivision": True,
        }, annotate=True
    ),
)

