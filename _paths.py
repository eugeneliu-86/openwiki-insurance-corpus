"""Make the vendored contracts importable as `contracts.*`.

This branch is the generator; `main` is the corpus. The two contracts the
generator needs (the path regex and the evidence anchor) are vendored under
vendor/ from the POC repo at the commit in vendor/VENDORED_FROM, exactly as
main's scripts/vendor does, so the branch is self-contained.
"""
import pathlib, sys
VENDOR = pathlib.Path(__file__).resolve().parent / "vendor"
if str(VENDOR) not in sys.path:
    sys.path.insert(0, str(VENDOR))
