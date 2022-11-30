"""ASE MD package."""
import importlib.metadata
import logging
import sys

from ase_md import simulator

__all__ = ["simulator"]

__version__ = importlib.metadata.version("ase_md")


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Formatter for advanced logging
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s')
formatter = logging.Formatter("%(asctime)s (%(levelname)s): %(message)s")

channel = logging.StreamHandler(sys.stdout)
channel.setLevel(logging.DEBUG)
channel.setFormatter(formatter)

logger.addHandler(channel)
