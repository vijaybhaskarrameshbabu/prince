# PRINCE cipher in Python

This project started out as an assembly project for Cortex-M3 but we never got past the Python reference stage. It is now abandoned.

The code has `encrypt()` and `decrypt()` functions that take arbitrary keys and block contents. It was written for Python2.7 and will not work in Python3 since it uses strings as character arrays to represent data.

## Status

The Python reference implementation is functional. No efforts have been made to achieve speed or to defend against side-channel analysis or any other kind of attack.