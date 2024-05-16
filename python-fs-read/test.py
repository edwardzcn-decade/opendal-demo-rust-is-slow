#!/usr/bin/python3
with open("/Users/edwardzcn/Rust/opendal-demo/data_file", "rb") as fp:
    result = fp.read()
assert len(result) == 64 * 1024 * 1024