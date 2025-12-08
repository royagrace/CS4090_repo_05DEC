import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from sub import min

def test_min ():
    assert min(6, 3) == 3

def test_min ():
    assert min (6, 5) != 3
