import importlib
import pkgutil
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class LoaderSpec:
    name: str
    extensions: frozenset[str]
    get_info: Callable[[Path], tuple[float, float]]


def _discover() -> dict[str, LoaderSpec]:
    out: dict[str, LoaderSpec] = {}
    for mod_info in pkgutil.iter_modules(__path__):
        if mod_info.name.startswith("_"):
            continue
        mod = importlib.import_module(f"{__name__}.{mod_info.name}")
        name = getattr(mod, "NAME", mod_info.name)
        out[name] = LoaderSpec(
            name=name,
            extensions=frozenset(getattr(mod, "SUPPORTED_EXTENSIONS", frozenset())),
            get_info=mod.get_info,
        )
    return out


LOADERS: dict[str, LoaderSpec] = _discover()
