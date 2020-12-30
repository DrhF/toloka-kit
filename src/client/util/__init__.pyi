from typing import Any, Dict, Iterator


def rename_dict_keys(data: dict, mapping: Dict[str, str]): ...

def make_camel_from_snake_dict_keys(data: dict) -> dict: ...

def make_snake_from_camel_dict_keys(data: dict) -> dict: ...

def camel_case_from_snake_case(name: str) -> str: ...

def snake_case_from_camel_case(name: str) -> str: ...

def traverse_dicts_recursively(obj: Any) -> Iterator[dict]: ...
