



def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."



print(greet.__annotations__)
{'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}




class Person:
    name: str
    age: int

print(Person.__annotations__)
Output: {'name': <class 'str'>, 'age': <class 'int'>}




from typing import List, Tuple, Dict

def process_data(items: List[int], mapping: Dict[str, int]) -> Tuple[int, int]:
    return sum(items), len(mapping)



from typing import Optional

def get_user_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None


from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> float:
    return x + y


from typing import Callable

def execute(func: Callable[[int , int], int], a: int, b: int) -> int:
    return func(a, b)
