#!/usr/bin/env python3
"""Validate .compile-state.json against contracts/compile-state.schema.json.

Stdlib only, so the workflow needs no pip install for it. Implements exactly the
subset of JSON Schema the contract uses: required, additionalProperties: false,
const, enum, type, pattern, minimum/maximum, uniqueItems. Anything the schema
grows beyond that must be added here — silently ignoring a keyword would turn
this into a no-op validator, which is worse than none.
"""
import json
import pathlib
import re
import sys

TYPES = {"object": dict, "array": list, "string": str, "integer": int}


def check(instance, schema, path="$"):
    errors = []
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} not in {schema['enum']}")
    if "type" in schema:
        py = TYPES[schema["type"]]
        if not isinstance(instance, py) or (py is int and isinstance(instance, bool)):
            errors.append(f"{path}: expected {schema['type']}")
            return errors
    if isinstance(instance, str) and "pattern" in schema and not re.search(schema["pattern"], instance):
        errors.append(f"{path}: {instance!r} does not match {schema['pattern']}")
    if isinstance(instance, int):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: {instance} > maximum {schema['maximum']}")
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}: missing required {key!r}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in props:
                    errors.append(f"{path}: unexpected field {key!r}")
        for key, sub in props.items():
            if key in instance:
                errors.extend(check(instance[key], sub, f"{path}.{key}"))
    if isinstance(instance, list):
        if schema.get("uniqueItems") and len(set(map(json.dumps, instance))) != len(instance):
            errors.append(f"{path}: items are not unique")
        for i, item in enumerate(instance):
            errors.extend(check(item, schema.get("items", {}), f"{path}[{i}]"))
    return errors


def main(path):
    here = pathlib.Path(__file__).resolve().parent.parent
    schema = json.loads((here / "contracts" / "compile-state.schema.json").read_text())
    instance = json.loads(pathlib.Path(path).read_text())
    errors = check(instance, schema)
    # `claims` is required by the schema but deliberately omitted for status=failed
    # (C4: zero would be a false statement about a run that never happened).
    if instance.get("status") == "failed":
        errors = [e for e in errors if e != "$: missing required 'claims'"]
    else:
        c = instance.get("claims", {})
        if c and c.get("added", 0) + c.get("carried", 0) != c.get("total", -1):
            errors.append("$.claims: added + carried != total")
    for e in errors:
        print(f"compile-state invalid: {e}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else ".compile-state.json"))
