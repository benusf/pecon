from ._core import mean, corr
import types


stats = types.SimpleNamespace(mean=mean, corr=corr)

__all__ = ["mean", "corr", "stats"]
