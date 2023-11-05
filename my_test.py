"""
Trying to add some functionality to pydantic

ipython -i my_test.py
the breakpoint is right where you edited the code

look at what you get
it seems that you are applying the js_annotation_function one sceham too 'inner'

you need to see where the pydantic_js_function adn pydantic_js_annotaiton _functiona are called


can you specify return_Type on the PlainValidator to fix this?
"""

from datetime import time
from typing import Annotated, Any

from pydantic import AfterValidator, BaseModel, BeforeValidator, Field, PlainValidator, WithJsonSchema, WrapValidator


def _validate(value: Any) -> Any:
    return value


Time = Annotated[time, PlainValidator(_validate), WithJsonSchema({'format': 'time', 'type': 'string'})]
Time2 = Annotated[time, PlainValidator(_validate)]
Int = Annotated[int, PlainValidator(_validate)]
Int2 = Annotated[int, WrapValidator(_validate)]
Int3 = Annotated[int, AfterValidator(_validate)]
Int4 = Annotated[int, BeforeValidator(_validate)]


class Test(BaseModel):
    """Test some schema generation"""

    number: int
    how_much: Int
    x: Int2
    y: Int3
    z: Int4
    # when: time
    # when1: Time = None
    # when2: Time2 = None
