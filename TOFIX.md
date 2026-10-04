# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pypipegzip/pypipegzip.py:33-38` - the `use_process=True` path, the package's whole reason to exist ("faster read of gzip files using a pipe to zcat(1)"), is broken: the stream is returned from inside `with subprocess.Popen(...)`, so `Popen.__exit__` closes `process.stdout` and waits for zcat before the caller gets it. Verified: `zipopen(f, "rb", use_process=True).read()` raises `ValueError: read of closed file` (text mode: `I/O operation on closed file`). Do not use `with`; return a wrapper object that owns the `Popen` and on `close()`/`__exit__` closes stdout, terminates/waits the child (which also addresses the hang described in `doc/TODO.txt:1-6`).

## Medium

- `tests/unit_tests/test_zipopen.py:1` - only the `gzip.open` path is tested ("gzip path" in the docstring); there is no test with `use_process=True`, which is why the bug above went unnoticed. Add binary and text round-trip tests through the zcat path, plus an early-close test (read a few lines, close, assert the child has exited).
- `src/pypipegzip/pypipegzip.py:28-39` - with `use_process=True` and a mode containing neither `b` nor `t` (e.g. the plain `"r"` that `gzip.open` accepts), zcat is spawned first and only then `ValueError("please specify t or b in mode")` is raised. Validate the mode before starting the process (or treat `"r"` as `"rb"` like `gzip.open` does).
- `pyproject.toml:88-92` - the mypy override sets `ignore_missing_imports` for `pypipegzip.*`, i.e. for this package itself, which is not a third-party module without stubs; remove the override so import errors in the package are reported.

## Low

- `src/pypipegzip/pypipegzip.py:30` - `/bin/zcat` is hardcoded; resolve `zcat` via `shutil.which` (or call `gzip -dc` directly, since `zcat` is just a shell wrapper around gzip per `doc/TODO.txt:8`), and raise a clear error if it is missing.
- `src/pypipegzip/pypipegzip.py:26` - `zipopen` has no docstring and no return annotation, so the sphinx API page documents it with nothing; document `mode`, `use_process` and `newline`.
