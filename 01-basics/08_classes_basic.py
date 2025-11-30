"""
08. 클래스 기본 (Classes Basic)

클래스, 인스턴스, 메서드, 상속 등 객체지향 프로그래밍의 기초를 학습합니다.
"""


def demonstrate_class_basics():
    """클래스 기본"""
    print("=" * 50)
    print("1. 클래스 기본")
    print("=" * 50)
    
    # 기본 클래스 정의
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def bark(self):
            return f"{self.name}: 멍멍!"
        
        def get_info(self):
            return f"{self.name} ({self.age}세)"
    
    # 인스턴스 생성
    dog1 = Dog("바둑이", 3)
    dog2 = Dog("뭉치", 5)
    
    print(dog1.get_info())
    print(dog1.bark())
    print(dog2.get_info())
    print(dog2.bark())
    
    print()


def demonstrate_class_attributes():
    """클래스 속성 vs 인스턴스 속성"""
    print("=" * 50)
    print("2. 클래스 속성 vs 인스턴스 속성")
    print("=" * 50)
    
    class Car:
        # 클래스 속성 (모든 인스턴스가 공유)
        wheels = 4
        count = 0
        
        def __init__(self, brand, model):
            # 인스턴스 속성
            self.brand = brand
            self.model = model
            Car.count += 1
        
        def get_info(self):
            return f"{self.brand} {self.model} (바퀴: {self.wheels}개)"
    
    car1 = Car("현대", "소나타")
    car2 = Car("기아", "K5")
    
    print(car1.get_info())
    print(car2.get_info())
    print(f"총 생성된 차량: {Car.count}대")
    
    # 클래스 속성 변경
    Car.wheels = 6  # 모든 인스턴스에 영향
    print(f"\n바퀴 개수 변경 후:")
    print(car1.get_info())
    print(car2.get_info())
    
    # 인스턴스 속성으로 덮어쓰기
    car1.wheels = 3
    print(f"\ncar1만 변경:")
    print(car1.get_info())
    print(car2.get_info())
    
    print()


def demonstrate_methods():
    """메서드 종류"""
    print("=" * 50)
    print("3. 메서드 종류")
    print("=" * 50)
    
    class Person:
        population = 0
        
        def __init__(self, name, age):
            self.name = name
            self.age = age
            Person.population += 1
        
        # 인스턴스 메서드
        def greet(self):
            return f"안녕하세요, {self.name}입니다."
        
        # 클래스 메서드
        @classmethod
        def get_population(cls):
            return f"총 인구: {cls.population}명"
        
        # 정적 메서드
        @staticmethod
        def is_adult(age):
            return age >= 18
    
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 17)
    
    # 인스턴스 메서드
    print(person1.greet())
    
    # 클래스 메서드
    print(Person.get_population())
    
    # 정적 메서드
    print(f"Alice는 성인? {Person.is_adult(person1.age)}")
    print(f"Bob은 성인? {Person.is_adult(person2.age)}")
    
    print()


def demonstrate_inheritance():
    """상속 (Inheritance)"""
    print("=" * 50)
    print("4. 상속")
    print("=" * 50)
    
    # 부모 클래스
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return "동물 소리"
        
        def info(self):
            return f"동물: {self.name}"
    
    # 자식 클래스
    class Dog(Animal):
        def speak(self):  # 메서드 오버라이딩
            return "멍멍!"
    
    class Cat(Animal):
        def speak(self):
            return "야옹~"
        
        def info(self):  # 부모 메서드 확장
            return f"{super().info()} (고양이)"
    
    dog = Dog("바둑이")
    cat = Cat("나비")
    
    print(dog.info())
    print(f"{dog.name}: {dog.speak()}")
    print()
    print(cat.info())
    print(f"{cat.name}: {cat.speak()}")
    
    print()


def demonstrate_multiple_inheritance():
    """다중 상속"""
    print("=" * 50)
    print("5. 다중 상속")
    print("=" * 50)
    
    class Flyable:
        def fly(self):
            return "날 수 있습니다"
    
    class Swimmable:
        def swim(self):
            return "수영할 수 있습니다"
    
    class Duck(Flyable, Swimmable):
        def __init__(self, name):
            self.name = name
        
        def quack(self):
            return "꽥꽥!"
    
    duck = Duck("도널드")
    print(f"{duck.name}:")
    print(f"  - {duck.fly()}")
    print(f"  - {duck.swim()}")
    print(f"  - {duck.quack()}")
    
    # MRO (Method Resolution Order)
    print(f"\nMRO: {Duck.__mro__}")
    
    print()


def demonstrate_encapsulation():
    """캡슐화 (Encapsulation)"""
    print("=" * 50)
    print("6. 캡슐화")
    print("=" * 50)
    
    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner  # public
            self._balance = balance  # protected (관례)
            self.__pin = "1234"  # private (name mangling)
        
        def deposit(self, amount):
            if amount > 0:
                self._balance += amount
                return f"입금: {amount:,}원, 잔액: {self._balance:,}원"
            return "올바르지 않은 금액"
        
        def withdraw(self, amount, pin):
            if pin != self.__pin:
                return "PIN이 틀렸습니다"
            if amount > self._balance:
                return "잔액이 부족합니다"
            self._balance -= amount
            return f"출금: {amount:,}원, 잔액: {self._balance:,}원"
        
        def get_balance(self):
            return f"잔액: {self._balance:,}원"
    
    account = BankAccount("Alice", 10000)
    print(account.get_balance())
    print(account.deposit(5000))
    print(account.withdraw(3000, "1234"))
    print(account.withdraw(3000, "0000"))
    
    # protected 변수는 접근 가능 (관례상 외부에서 사용하지 않음)
    print(f"\n_balance 직접 접근: {account._balance}원")
    
    # private 변수는 name mangling으로 접근 어려움
    try:
        print(account.__pin)
    except AttributeError as e:
        print(f"__pin 접근 실패: {e}")
    
    # name mangling 우회 (권장하지 않음)
    print(f"name mangling 우회: {account._BankAccount__pin}")
    
    print()


def demonstrate_property():
    """프로퍼티 (Property)"""
    print("=" * 50)
    print("7. 프로퍼티")
    print("=" * 50)
    
    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            """반지름 getter"""
            return self._radius
        
        @radius.setter
        def radius(self, value):
            """반지름 setter"""
            if value < 0:
                raise ValueError("반지름은 0 이상이어야 합니다")
            self._radius = value
        
        @property
        def diameter(self):
            """지름 (읽기 전용)"""
            return self._radius * 2
        
        @property
        def area(self):
            """넓이 (읽기 전용)"""
            return 3.14159 * self._radius ** 2
    
    circle = Circle(5)
    print(f"반지름: {circle.radius}")
    print(f"지름: {circle.diameter}")
    print(f"넓이: {circle.area:.2f}")
    
    # setter 사용
    circle.radius = 10
    print(f"\n변경 후 반지름: {circle.radius}")
    print(f"변경 후 지름: {circle.diameter}")
    
    # 검증
    try:
        circle.radius = -5
    except ValueError as e:
        print(f"\n오류: {e}")
    
    print()


def demonstrate_special_methods():
    """특수 메서드 (매직 메서드)"""
    print("=" * 50)
    print("8. 특수 메서드 (매직 메서드)")
    print("=" * 50)
    
    class Vector:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __repr__(self):
            """개발자용 문자열 표현"""
            return f"Vector({self.x}, {self.y})"
        
        def __str__(self):
            """사용자용 문자열 표현"""
            return f"({self.x}, {self.y})"
        
        def __add__(self, other):
            """+ 연산자"""
            return Vector(self.x + other.x, self.y + other.y)
        
        def __sub__(self, other):
            """- 연산자"""
            return Vector(self.x - other.x, self.y - other.y)
        
        def __mul__(self, scalar):
            """* 연산자 (스칼라)"""
            return Vector(self.x * scalar, self.y * scalar)
        
        def __eq__(self, other):
            """== 연산자"""
            return self.x == other.x and self.y == other.y
        
        def __len__(self):
            """len() 함수"""
            return int((self.x ** 2 + self.y ** 2) ** 0.5)
        
        def __getitem__(self, index):
            """인덱싱"""
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            raise IndexError("Index out of range")
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"repr(v1): {repr(v1)}")
    
    print(f"\nv1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 2: {v1 * 2}")
    
    print(f"\nv1 == v2: {v1 == v2}")
    print(f"v1 == Vector(3, 4): {v1 == Vector(3, 4)}")
    
    print(f"\nlen(v1): {len(v1)}")
    print(f"v1[0]: {v1[0]}, v1[1]: {v1[1]}")
    
    print()


def demonstrate_composition():
    """컴포지션 (Composition)"""
    print("=" * 50)
    print("9. 컴포지션 (has-a 관계)")
    print("=" * 50)
    
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower
        
        def start(self):
            return f"{self.horsepower}마력 엔진 시동"
    
    class Wheel:
        def __init__(self, size):
            self.size = size
    
    class Car:
        def __init__(self, brand, horsepower, wheel_size):
            self.brand = brand
            self.engine = Engine(horsepower)  # 컴포지션
            self.wheels = [Wheel(wheel_size) for _ in range(4)]
        
        def start(self):
            return f"{self.brand} 차량: {self.engine.start()}"
        
        def info(self):
            return f"{self.brand} (엔진: {self.engine.horsepower}마력, " \
                   f"바퀴: {self.wheels[0].size}인치)"
    
    car = Car("현대", 200, 18)
    print(car.start())
    print(car.info())
    
    print("\n컴포지션 vs 상속:")
    print("  - 상속: is-a 관계 (Car is a Vehicle)")
    print("  - 컴포지션: has-a 관계 (Car has an Engine)")
    print("  - 일반적으로 컴포지션을 선호 (더 유연함)")
    
    print()


def main():
    """메인 함수"""
    print("\n" + "🐍 Python 기본 문법 - 클래스".center(50, "="))
    print()
    
    demonstrate_class_basics()
    demonstrate_class_attributes()
    demonstrate_methods()
    demonstrate_inheritance()
    demonstrate_multiple_inheritance()
    demonstrate_encapsulation()
    demonstrate_property()
    demonstrate_special_methods()
    demonstrate_composition()
    
    print("=" * 50)
    print("✅ 클래스 기본 학습 완료!")
    print("=" * 50)


if __name__ == "__main__":
    main()

