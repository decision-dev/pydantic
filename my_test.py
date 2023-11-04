"""
Trying to add some functionality to pydantic

ipython -i my_test.py
the breakpoint is right where you edited the code

look at what oyu get
it seems that oyu are applying the js_annotation_function one sceham too 'inner'

you need to see where the pydantic_js_function adn pydantic_js_annotaiton _functiona are called 


can you specify return_Type on the PlainValidator to fix this?
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

    number: int
    how_much: Int
    when: time
    when1: Time = None
    # when2: Time2 = None
