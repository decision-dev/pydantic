"""
Trying to add some funcitonality to pydantic
"""

from datetime import time
from typing import Annotated, Any

from pydantic import BaseModel, Field, PlainValidator, WithJsonSchema


def _validate(value: Any) -> Any:
    return value


Time = Annotated[time, PlainValidator(_validate), WithJsonSchema({'format': 'time', 'type': 'string'})]
Time2 = Annotated[time, PlainValidator(_validate)]
Int = Annotated[int, PlainValidator(_validate)]


class Test(BaseModel):
    """Test some schema generation"""

    how_much: Int
    when: time
    when1: Time = None
    # when2: Time2 = None
