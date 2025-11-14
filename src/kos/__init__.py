"""KOS Community Edition - Knowledge Operating System.

This package provides the core implementation of the WEKAOU Knowledge Operating
System, including SPOC-M knowledge representation, K-Cycle orchestration, and
ontological validation.
"""

from kos.core import KOS
from kos.config import Config
from kos.models.spocm import SPOCM
from kos.kcycle import KCycle, Stage

__version__ = "0.1.0"
__all__ = ["KOS", "Config", "SPOCM", "KCycle", "Stage"]
