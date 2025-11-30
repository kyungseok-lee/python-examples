"""
01. 데코레이터 (Decorators)

함수와 클래스를 수정하거나 확장하는 데코레이터를 학습합니다.
"""

import time
import functools


def demonstrate_function_decorator():
    """함수 데코레이터 기본"""
    print("=" * 50)
    print("1. 함수 데코레이터 기본")
    print("=" * 50)
    
    # 간단한 데코레이터
    def my_decorator(func):
        def wrapper():
            print("  함수 실행 전")
            result = func()
            print("  함수 실행 후")
            return result
        return wrapper
    
    @my_decorator
    def say_hello():
        print("  Hello!")
        return "완료"
    
    result = say_hello()
    print(f"반환값: {result}")
    
    print()


def demonstrate_decorator_with_args():
    """인자가 있는 데코레이터"""
    print("=" * 50)
    print("2. 인자가 있는 데코레이터")
    print("=" * 50)
    
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"  인자: {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"  결과: {result}")
            return result
        return wrapper
    
    @my_decorator
    def add(a, b):
        return a + b
    
    @my_decorator
    def greet(name, greeting="안녕"):
        return f"{greeting}, {name}!"
    
    add(10, 20)
    greet("Alice", greeting="Hello")
    
    print()


def demonstrate_functools_wraps():
    """functools.wraps"""
    print("=" * 50)
    print("3. functools.wraps")
    print("=" * 50)
    
    # wraps 없이
    def bad_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    # wraps 사용
    def good_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @bad_decorator
    def func1():
        """func1의 docstring"""
        pass
    
    @good_decorator
    def func2():
        """func2의 docstring"""
        pass
    
    print(f"wraps 없음: {func1.__name__}, {func1.__doc__}")
    print(f"wraps 사용: {func2.__name__}, {func2.__doc__}")
    
    print()


def demonstrate_timing_decorator():
    """실행 시간 측정 데코레이터"""
    print("=" * 50)
    print("4. 실행 시간 측정 데코레이터")
    print("=" * 50)
    
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"  {func.__name__} 실행 시간: {end - start:.4f}초")
            return result
        return wrapper
    
    @timer
    def slow_function():
        time.sleep(0.1)
        return "완료"
    
    @timer
    def calculate_sum(n):
        return sum(range(n))
    
    slow_function()
    calculate_sum(100000)
    
    print()


def demonstrate_decorator_with_params():
    """매개변수를 받는 데코레이터"""
    print("=" * 50)
    print("5. 매개변수를 받는 데코레이터")
    print("=" * 50)
    
    def repeat(times):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator
    
    @repeat(times=3)
    def greet(name):
        print(f"  안녕하세요, {name}님!")
        return "완료"
    
    greet("Alice")
    
    print()


def demonstrate_class_decorator():
    """클래스 데코레이터"""
    print("=" * 50)
    print("6. 클래스 데코레이터")
    print("=" * 50)
    
    def add_repr(cls):
        """클래스에 __repr__ 메서드 추가"""
        def __repr__(self):
            attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
            return f"{cls.__name__}({attrs})"
        cls.__repr__ = __repr__
        return cls
    
    @add_repr
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    person = Person("Alice", 25)
    print(f"  {repr(person)}")
    
    print()


def demonstrate_method_decorator():
    """메서드 데코레이터"""
    print("=" * 50)
    print("7. 메서드 데코레이터")
    print("=" * 50)
    
    def log_method(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            print(f"  메서드 호출: {func.__name__}")
            return func(self, *args, **kwargs)
        return wrapper
    
    class Calculator:
        @log_method
        def add(self, a, b):
            return a + b
        
        @log_method
        def multiply(self, a, b):
            return a * b
    
    calc = Calculator()
    print(f"결과: {calc.add(10, 20)}")
    print(f"결과: {calc.multiply(5, 6)}")
    
    print()


def demonstrate_property_decorator():
    """property 데코레이터"""
    print("=" * 50)
    print("8. property 데코레이터")
    print("=" * 50)
    
    class Temperature:
        def __init__(self, celsius):
            self._celsius = celsius
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("절대영도 이하는 불가능")
            self._celsius = value
        
        @property
        def fahrenheit(self):
            return self._celsius * 9/5 + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            self._celsius = (value - 32) * 5/9
    
    temp = Temperature(25)
    print(f"  섭씨: {temp.celsius}°C")
    print(f"  화씨: {temp.fahrenheit}°F")
    
    temp.fahrenheit = 100
    print(f"  변경 후 섭씨: {temp.celsius:.1f}°C")
    
    print()


def demonstrate_cache_decorator():
    """캐싱 데코레이터"""
    print("=" * 50)
    print("9. 캐싱 데코레이터")
    print("=" * 50)
    
    def memoize(func):
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args):
            if args not in cache:
                print(f"  계산 중: {args}")
                cache[args] = func(*args)
            else:
                print(f"  캐시 사용: {args}")
            return cache[args]
        
        return wrapper
    
    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("첫 번째 호출:")
    result = fibonacci(5)
    print(f"결과: {result}")
    
    print("\n두 번째 호출:")
    result = fibonacci(5)
    print(f"결과: {result}")
    
    # functools.lru_cache 사용
    print("\nfunctools.lru_cache:")
    
    @functools.lru_cache(maxsize=128)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
    
    print(f"fib(10) = {fib(10)}")
    print(f"캐시 정보: {fib.cache_info()}")
    
    print()


def demonstrate_stacked_decorators():
    """데코레이터 스택"""
    print("=" * 50)
    print("10. 데코레이터 스택")
    print("=" * 50)
    
    def bold(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<b>{func(*args, **kwargs)}</b>"
        return wrapper
    
    def italic(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<i>{func(*args, **kwargs)}</i>"
        return wrapper
    
    @bold
    @italic
    def greet(name):
        return f"Hello, {name}"
    
    # 적용 순서: greet -> italic -> bold
    result = greet("Alice")
    print(f"  {result}")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 중급 - 데코레이터".center(50, "="))
    print()
    
    demonstrate_function_decorator()
    demonstrate_decorator_with_args()
    demonstrate_functools_wraps()
    demonstrate_timing_decorator()
    demonstrate_decorator_with_params()
    demonstrate_class_decorator()
    demonstrate_method_decorator()
    demonstrate_property_decorator()
    demonstrate_cache_decorator()
    demonstrate_stacked_decorators()
    
    print("=" * 50)
    print("✅ 데코레이터 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

