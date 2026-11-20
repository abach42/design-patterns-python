# Python Design Patterns Cheat Sheet – Gang of Four (GoF) Examples

[![CI](https://github.com/abach42/design-patterns-python/actions/workflows/ci.yml/badge.svg)](https://github.com/abach42/design-patterns-python/actions/workflows/ci.yml)
![Python 3.12+](https://img.shields.io/badge/Python-3.12+-blue)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

A Python design patterns cheat sheet covering all 23 Gang of Four (GoF) patterns – creational, structural and behavioral – with short explanations, client code examples, runnable source code and pytest tests.

Use it in your daily Python work to quickly decide which design pattern fits a problem – or whether you need a pattern at all. Every pattern comes with its intent, when to use it and when to avoid it, a client code example, a link to the Python source code and a link to a pytest test that shows how the pattern works.

> Remark: The class names follow the roles of each pattern (e.g. `Creator`, `Adaptee`, `Visitor`) so you can recognize its structure. In practice, you would name classes after their function. The tests are not meant to be complete; they demonstrate how each pattern works. The focus of this cheat sheet is choosing a pattern quickly – or deliberately not choosing one – to avoid over-engineering.

## Table of Contents

| Creational Patterns | Structural Patterns | Behavioral Patterns |
| :--- | :--- | :--- |
| [Singleton](#singleton-pattern-in-python) | [Adapter](#adapter-pattern-in-python) | [Chain of Responsibility](#chain-of-responsibility-pattern-in-python) |
| [Factory Method](#factory-method-pattern-in-python) | [Bridge](#bridge-pattern-in-python) | [Command](#command-pattern-in-python) |
| [Abstract Factory](#abstract-factory-pattern-in-python) | [Composite](#composite-pattern-in-python) | [Interpreter](#interpreter-pattern-in-python) |
| [Builder](#builder-pattern-in-python) | [Decorator](#decorator-pattern-in-python) | [Iterator](#iterator-pattern-in-python) |
| [Prototype](#prototype-pattern-in-python) | [Facade](#facade-pattern-in-python) | [Mediator](#mediator-pattern-in-python) |
| | [Flyweight](#flyweight-pattern-in-python) | [Memento](#memento-pattern-in-python) |
| | [Proxy](#proxy-pattern-in-python) | [Observer](#observer-pattern-in-python) |
| | | [State](#state-pattern-in-python) |
| | | [Strategy](#strategy-pattern-in-python) |
| | | [Template Method](#template-method-pattern-in-python) |
| | | [Visitor](#visitor-pattern-in-python) |

**More:** [Run the examples](#run-the-examples) · [References](#references) · [License](#license)

## Creational Design Patterns in Python

Creational patterns abstract the instantiation process: they decide how, when and which objects are created.

### Singleton Pattern in Python

:pencil2: The Singleton pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. It's useful when exactly one object is needed to coordinate actions across the system.

**Use when:** exactly one shared instance is required, e.g. a configuration registry or a hardware access point.

**Avoid when:** you only want a convenient global variable – prefer dependency injection. In Python, a module-level object is often the simplest singleton.

```python
class Singleton:
    _instance: "Singleton | None" = None

    def __new__(cls) -> "Singleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

And here's how you would use the Singleton class:

```python
singleton = Singleton()
```

The lazy variant above is not thread-safe. In multi-threaded code, guard the creation with a `threading.Lock`:

```python
import threading

class Singleton:
    _instance: "Singleton | None" = None
    _lock = threading.Lock()

    def __new__(cls) -> "Singleton":
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
```

While the Singleton pattern can be useful in certain situations, it's also often considered an "anti-pattern" due to drawbacks like hidden dependencies, concurrency issues and testing challenges.

### Factory Method Pattern in Python

:pencil2: The Factory Method is a creational pattern that defines a method for creating an object. Which type is instantiated is decided by the concrete class that implements this method.

**Use when:** a class can't anticipate which concrete type it must create, and subclasses should decide.
**Avoid when:** there is only one product type – a constructor or a factory function is enough.

:bulb: [Factory Method Python source code](src/designpatterns/creational/factorymethod)

:pill: [Factory Method pytest test](tests/creational/factorymethod/test_factory_method.py)

#### Factory Method client code example

```python
creator = CircleCreator()
product = creator.create_product(Point(100, 100))
shape = product.get_shape()
```
```python
creator = SquareCreator()
product = creator.create_product(Point(100, 100))
shape = product.get_shape()
```

### Abstract Factory Pattern in Python

:pencil2: The Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It's useful when you need to ensure that the created objects are compatible with each other and when you want to hide the implementation details of the creation process.

**Use when:** several products must be created as a consistent family (e.g. UI widgets per theme).
**Avoid when:** you have a single product type – use a Factory Method instead.

:bulb: [Abstract Factory Python source code](src/designpatterns/creational/abstractfactory)

:pill: [Abstract Factory pytest test](tests/creational/abstractfactory/test_abstract_factory.py)

#### Abstract Factory client code example

```python
first_factory = ConcreteFactory1()
result_a = str(first_factory.create_product_a())  # "Name:ProductA1"
result_b = str(first_factory.create_product_b())  # "Id:ProductB1"
```
```python
second_factory = ConcreteFactory2()
result_a = str(second_factory.create_product_a())  # "Name:ProductA2"
result_b = str(second_factory.create_product_b())  # "Id:ProductB2"
```

### Builder Pattern in Python

:pencil2: The Builder pattern is a creational pattern that composes data in steps and separates the construction process from the representation. It allows you to produce different types and representations of an object using the same construction process. This pattern is particularly useful when dealing with objects that have numerous parameters or configurations, as it provides a clear way to separate the construction logic from the rest of the code. See variants in the [Builder pytest test](tests/creational/builder/test_builder.py).

**Use when:** an object has many (optional) parameters or must be assembled in steps.
**Avoid when:** an object has only a few required fields – a constructor or a dataclass is clearer.

:bulb: [Builder Python source code](src/designpatterns/creational/builder)

:pill: [Builder pytest test](tests/creational/builder/test_builder.py)

#### Builder client code example

```python
director = Director()

barebone_builder = BareboneConcreteBuilder()
director.construct_basic_computer(barebone_builder)
barebone_product = barebone_builder.build()

print(barebone_product)
```

### Prototype Pattern in Python

:pencil2: The Prototype Pattern is a creational design pattern used to create objects based on a template of an existing object through cloning. It is particularly useful when creating a new instance by copying an existing one is more efficient than creating it from scratch.

**Use when:** object creation is expensive and many similar objects are needed.
**Avoid when:** objects hold deep or circular references that make cloning error-prone – `copy.deepcopy` helps, but think twice.

:bulb: [Prototype Python source code](src/designpatterns/creational/prototype)

:pill: [Prototype pytest test](tests/creational/prototype/test_prototype.py)

#### Prototype client code example

```python
circle_prototype = CirclePrototype()
circle_prototype.x = 1
circle_prototype.y = 1
circle_prototype.radius = 10
circle_prototype.color = "blue"

circle = circle_prototype.clone()
```

## Structural Design Patterns in Python

Structural patterns describe how classes and objects are composed into larger structures.

### Adapter Pattern in Python

:pencil2: The Adapter pattern is a design pattern that adapts the interface of an existing object so that it can be used by a class that was originally incompatible with this object. The Adapter pattern is often used to integrate existing class libraries or external APIs without needing to change their codebase.

**Use when:** you need to use an existing class or external API whose interface doesn't match yours.
**Avoid when:** you control both sides – change the interface instead.

The Adapter pattern consists of three main components:

* A Target interface, which represents the interface that the client wants to use.
* An 'Adaptee', which is the callable to be integrated but does not match the Target interface.
* An Adapter class, which implements the Target interface and wraps the 'Adaptee'. The Adapter translates the method calls of the Target interface into calls to the 'Adaptee'.

:bulb: [Adapter Python source code](src/designpatterns/structural/adapter)

:pill: [Adapter pytest test](tests/structural/adapter/test_adapter.py)

#### Adapter client code example

```python
fake_api_adaptee: ApiAdaptee[str] = lambda: '{"id": 42, "name": "John Doe"}'
api_target: Target[Record] = ApiAdapter(fake_api_adaptee)
actual_record = api_target.fetch_data()
expected_record = Record(42, "John Doe")
```

In this example `fake_api_adaptee` represents external code or an API without code insight.

### Bridge Pattern in Python

:pencil2: The Bridge Pattern decouples an abstraction from its implementation so that the two can vary independently. Abstraction defines a high-level interface that uses an implementation object. Refined Abstraction extends the abstraction.

Implementor defines the interface for implementation classes. Concrete Implementors provide the specific implementation of the Implementor interface.

**Use when:** two dimensions (e.g. shape and renderer) would otherwise multiply into a class explosion.
**Avoid when:** there is only one implementation – the extra indirection adds nothing.

:bulb: [Bridge Python source code](src/designpatterns/structural/bridge/)

:pill: [Bridge pytest test](tests/structural/bridge/test_bridge.py)

#### Bridge client code example

```python
renderer2d = Renderer2D()
circle = Circle(renderer2d, 5.0, Point(10, 10))

result = circle.draw()  # an Ellipse
```

```python
renderer3d = Renderer3D()
circle = Circle(renderer3d, 5.0, Point(10, 10))

result = circle.draw()  # a Circle3DHelper
```

```python
renderer3d = Renderer3D()
rectangle = Rectangle(renderer3d, 10.0, 5.0, Point(0, 0))

result = rectangle.draw()  # a Rectangle3DHelper
```

### Composite Pattern in Python

:pencil2: The Composite Pattern is a structural design pattern used to represent part-whole hierarchies as tree structures. It lets clients treat individual objects (leaves) and compositions of objects (composites) uniformly.

**Use when:** you model trees such as file systems, menus or organization charts.
**Avoid when:** leaves and containers need very different interfaces.

:bulb: [Composite Python source code](src/designpatterns/structural/composite/)

:pill: [Composite pytest test](tests/structural/composite/test_composite.py)

#### Composite client code example

```python
file1 = File("file1.txt", 120)
file2 = File("file2.txt", 200)

folder1 = Folder("Folder1")
folder2 = Folder("Folder2")

folder1.add_component(file1)
folder1.add_component(file2)

folder2.add_component(folder1)
```

### Decorator Pattern in Python

:pencil2: The Decorator pattern is a structural design pattern that allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.

The Decorator pattern allows you to stack decorators on top of each other, each adding its own behavior, and provides a flexible way to modify the behavior of individual objects at runtime.

**Use when:** you need combinable extensions at runtime instead of a subclass for every combination.
**Avoid when:** the order of many small wrappers becomes hard to understand and debug.

:bulb: [Decorator Python source code](src/designpatterns/structural/decorator/)

:pill: [Decorator pytest test](tests/structural/decorator/test_decorator.py)

#### Decorator client code example

```python
order = FoamMilkDecorator(
    ChocolateDecorator(
        EspressoComponent()
    )
)

print(f"{order.calculate_price():.2f}")
```

### Facade Pattern in Python

:pencil2: The Facade pattern provides a simplified interface to a set of complex subsystems. It allows clients to interact with a single unified interface without needing to understand the inner workings of each subsystem.

**Use when:** clients need a simple entry point to a complex subsystem.
**Avoid when:** the facade grows into a "god object" that knows everything.

:bulb: [Facade Python source code](src/designpatterns/structural/facade)

:pill: [Facade pytest test](tests/structural/facade/test_facade.py)

#### Facade client code example

```python
facade = OrderFacade()
result = facade.place_order("Laptop", 2, 2000.0)
```
```python
class OrderFacade:
    def __init__(self) -> None:
        self.payment_processor = PaymentProcessor()
        self.inventory_manager = InventoryManager()
        self.shipping_service = ShippingService()

    def place_order(self, product: str, quantity: int, amount: float) -> str:
        # operations accessing attributes of subsystems
        ...
```

### Flyweight Pattern in Python

:pencil2: The Flyweight pattern is a structural design pattern that minimizes memory usage by sharing as much data as possible with similar objects. It separates **intrinsic state** (shared, immutable data) from **extrinsic state** (context-dependent, provided from outside).

The pattern is useful when a system needs to handle a large number of fine-grained objects efficiently, such as characters in a text editor, tiles in a game, or icons in a UI.

**Use when:** a huge number of similar objects causes memory pressure.
**Avoid when:** there are few objects – the added complexity doesn't pay off. (In CPython, `sys.intern` or small-int caching already do this for you in many cases.)

Components:

* **Flyweight**: declares interface for objects that can act as shared.
* **ConcreteFlyweight**: implements the Flyweight and stores intrinsic state.
* **UnsharedConcreteFlyweight**: objects that cannot be shared but may use Flyweights internally.
* **FlyweightFactory**: creates and manages Flyweight objects, ensuring they are reused.

:bulb: [Flyweight Python source code](src/designpatterns/structural/flyweight)

:pill: [Flyweight pytest test](tests/structural/flyweight/test_flyweight.py)

#### Flyweight client code example

```python
factory = FlyweightFactory()

shared_a1 = factory.get_flyweight("A")
shared_a2 = factory.get_flyweight("A")
shared_b = factory.get_flyweight("B")

first = shared_a1.operation("first")
# "Intrinsic: A, Extrinsic: first"

second = shared_a2.operation("second")
# "Intrinsic: A, Extrinsic: second"

context = shared_b.operation("context")
# "Intrinsic: B, Extrinsic: context"
```

To keep the interface for objects that are not shared:

```python
unshared = UnsharedConcreteFlyweight("CustomState")
result = unshared.operation("external context")
# "Unshared: CustomState, Extrinsic: external context"
```

### Proxy Pattern in Python

:pencil2: The Proxy pattern is a structural design pattern that provides a surrogate or placeholder for another object to control access to it. This can be useful for lazy initialization, access control, logging, or caching. The Proxy implements the same interface as the RealSubject and delegates calls to it, while possibly adding extra behavior.

**Use when:** you need lazy loading, access control, caching or logging around an object.
**Avoid when:** a decorator or a framework feature already covers it.

:bulb: [Proxy Python source code](src/designpatterns/structural/proxy)

:pill: [Proxy pytest test](tests/structural/proxy/test_proxy.py)

#### Proxy client code example

```python
real = RealSubject()
proxy = Proxy(real)

result = proxy.get_data()
```

## Behavioral Design Patterns in Python

Behavioral patterns describe how objects communicate and how responsibilities are distributed between them.

### Chain of Responsibility Pattern in Python

:pencil2: The Chain of Responsibility pattern is a design pattern where a request is passed through a chain of handlers. Each handler decides either to process the request or pass it to the next handler in the chain. It promotes loose coupling between the sender and receiver of a request and is commonly used in scenarios like event handling or middleware processing in web applications.

**Use when:** a request runs through configurable processing steps (filters, middleware, validation).
**Avoid when:** the order is fixed and short – plain function calls are easier to follow.

:bulb: [Chain of Responsibility Python source code](src/designpatterns/behavioral/chain/context/)

:pill: [Chain of Responsibility pytest test](tests/behavioral/chain/context/test_context_chain.py)

#### Chain of Responsibility client code example

```python
member_list = MemberList()
member_list.append(Member("John", 50))
member_list.append(Member("Doe", 62))
member_list.append(Member("Marilyn", 32))

AbstractHandler.initialize_chain(
    FilterHandler(member_list, 30),
    SortByAgeHandler(member_list),
).handle()
```

#### Variant 1: Simple Chain of Responsibility

This example works without a data context, and handlers do not decide whether to process or pass the request.

:bulb: [Simple Chain of Responsibility Python source code](src/designpatterns/behavioral/chain/simple/)

:pill: [Simple Chain of Responsibility pytest test](tests/functional/chain/simple/test_simple_chain.py)

##### Client code example

```python
first_handler = FirstHandler()
second_handler = SecondHandler()
first_handler.set_next(second_handler)
first_handler.handle()
```

#### Variant 2: Chain of Responsibility with delegated handling

Here the data context is passed through the process. Handlers don't care about calling the next handler or building the chain; the handling is steered from outside of the handle method.

:bulb: [Delegating Chain of Responsibility Python source code](src/designpatterns/behavioral/chain/delegation/)

:pill: [Delegating Chain of Responsibility pytest test](tests/behavioral/chain/delegation/test_delegation_chain.py)

##### Client code example

```python
member_list = MemberList()
member_list.append(Member("John", 50))
member_list.append(Member("Doe", 62))
member_list.append(Member("Marilyn", 32))

Chain()
    .add(FilterHandler(40))
    .add(SortByAgeHandler())
    .process(member_list)
```

> Handling guard can vary in complexity...

```python
if not member_list:
    return member_list
```

### Command Pattern in Python

:pencil2: The Command pattern encapsulates a request as an object, allowing other objects to be parameterized with different requests, to queue or log commands, or to support undo operations.
This behavioral pattern separates tasks into small steps, enables high reusability and can be used for asynchronous execution.

**Use when:** you need undo/redo, queues, logging or deferred execution of operations.
**Avoid when:** a simple function call or a lambda does the job.

:bulb: [Command Python source code](src/designpatterns/behavioral/command)

:pill: [Command pytest test](tests/behavioral/command/test_command.py)

In this example the receiver also acts as data storage; both could be separated. It hands out ids from a counter, so ids stay unique after updates and deletes. The invoker removes each command from its queue when it runs it.

#### Command client code example

```python
invoker = PersonInvoker()
receiver = PersonReceiver()

invoker.add_command(CreatePersonCommand(receiver, "John", 62))
invoker.add_command(CreatePersonCommand(receiver, "Peter", 43))
invoker.add_command(CreatePersonCommand(receiver, "James", 21))

invoker.add_command(UpdatePersonCommand(receiver, Person(1, "Paul", 34)))
invoker.add_command(DeletePersonCommand(receiver, 1))

invoker.run_commands()
```

### Interpreter Pattern in Python

:pencil2: The **Interpreter Pattern** defines a grammar and provides an interpreter that evaluates sentences of that grammar.
Each rule or symbol of the grammar corresponds to a class implementing a common interface.

This pattern is suitable for small domain-specific languages, rule engines, and formula evaluators.

**Use when:** you evaluate a small, stable grammar (boolean rules, simple formulas).
**Avoid when:** the grammar is large or changes often – use a parser generator instead.

* `Expression` – defines the `interpret(context)` interface.
* `VariableExpression` – represents variables (terminal symbols).
* Non-terminal expressions – represent grammar rules combining other expressions (`AND`, `OR`, `NOT`, etc.).
* `Context` – provides variable values.
* Client – builds and interprets expression trees.

:bulb: [Interpreter Python source code](src/designpatterns/behavioral/interpreter)

:pill: [Interpreter pytest test](tests/behavioral/interpreter/test_interpreter.py)

#### Interpreter client code example

```python
context = Context({
    "a": True,
    "b": False,
    "c": True,
})

# Expression: a AND NOT (b OR c)
expr = AndExpression(
    VariableExpression("a"),
    NotExpression(
        OrExpression(
            VariableExpression("b"),
            VariableExpression("c")
        )
    )
)

result = expr.interpret(context)  # False
```

### Iterator Pattern in Python

:pencil2: The Iterator Pattern simplifies traversing collections without exposing their structure. With a custom iterator, you can tailor traversal to specific needs. Python's built-in iterators (`iter()` / `for` loops) streamline iteration over standard collections, ensuring consistency and interoperability.

**Use when:** a custom data structure should be traversable without exposing its internals.
**Avoid when:** a standard Python collection or iterator already provides what you need.

#### Variant 1: Using Python's built-in iterator

:bulb: [Simple Iterator Python source code](src/designpatterns/behavioral/iterator/simple)

:pill: [Simple Iterator pytest test](tests/behavioral/iterator/simple/test_simple_iterator.py)

#### Variant 2: Custom iterator

:bulb: [Custom Iterator Python source code](src/designpatterns/behavioral/iterator/customiterator)

:pill: [Custom Iterator pytest test](tests/behavioral/iterator/customiterator/test_custom_iterator.py)

#### Iterator client code example

```python
numbers = [1, 2]
aggregate = ConcreteAggregate(numbers)
iterator = aggregate.create_iterator()

result = []
for item in iterator:
    result.append(item)
```

### Mediator Pattern in Python

:pencil2: The Mediator pattern is a behavioral design pattern that allows objects to communicate with each other without needing to know each other's implementation.

When a 'colleague' sends a message through the mediator, the mediator distributes the message to all other 'colleagues' except the sender. This bidirectional communication demonstrates the Mediator pattern's central idea: decoupling the objects communicating with each other by introducing a mediator object. Instead of directly interacting with each other, objects communicate through the mediator, which encapsulates the communication logic and facilitates indirect communication between them.

**Use when:** many objects talk to each other and the dependencies become a tangled web.
**Avoid when:** only two objects interact – the mediator just adds indirection.

:bulb: [Mediator Python source code](src/designpatterns/behavioral/mediator/)

:pill: [Mediator pytest test](tests/behavioral/mediator/test_mediator.py)

#### Mediator client code example

```python
mediator = Mediator()

german_colleague = ConcreteGermanColleague(mediator)
polish_colleague = ConcretePolishColleague(mediator)

mediator.add_colleague(german_colleague)
mediator.add_colleague(polish_colleague)

german_colleague.send("Schönes Wetter!")
polish_colleague.send("ładna pogoda!")

polish_colleague.last_received_message  # "Witaj świecie: Schönes Wetter!"
german_colleague.last_received_message  # "Hallo Welt: ładna pogoda!"
```

### Memento Pattern in Python

:pencil2: The Memento pattern captures and externalizes an object's internal state without violating encapsulation. The object creates a memento that stores its state, which can later be restored. This pattern is particularly useful when the state of an object needs to be saved and restored, such as in undo mechanisms or checkpoints in an application.

**Use when:** you need undo, snapshots or checkpoints without exposing internal state.
**Avoid when:** the state is large and snapshots become too expensive in memory.

:bulb: [Memento Python source code](src/designpatterns/behavioral/memento/)

:pill: [Memento pytest test](tests/behavioral/memento/test_memento.py)

#### Memento client code example

```python
originator = Originator("foo")
caretaker = Caretaker()
originator.change_state("bar")
caretaker.add_memento(originator.create_snapshot())
originator.restore_snapshot(caretaker.get_memento(0))
actual_foo_bar = originator.state
```

### Observer Pattern in Python

:pencil2: The Observer Pattern is a design pattern where an object (the subject) maintains a list of its dependents (observers) and notifies them of any state changes. This allows for loose coupling between components, making it easier to maintain and extend the system.

**Use when:** several objects must react to state changes of another object (events, UI updates).
**Avoid when:** notification chains become hard to trace – consider explicit calls or an event bus.

:bulb: [Observer Python source code](src/designpatterns/behavioral/observer/simple/)

:pill: [Observer pytest test](tests/behavioral/observer/simple/test_observer_simple.py)

#### Observer client code example

```python
subject = ConcreteRoutingSubject()
CalculateDistanceObserver(subject)
CalculateDurationObserver(subject)

route = RouteEntity("way home", Point(0, 0), Point(20, 20))
# subject.detach_observer(...)  # some concrete observer
subject.set_state_entity(route)

print(f"You would have {route.duration:.2f} h to travel")
```

#### Variant: Observer with a property-change event

This example mirrors Java's `PropertyChangeListener`: the subject fires a `PropertyChangeEvent` when its entity is replaced, and each observer reacts only to events for its own subject. Registration and notification are delegated to the subject.

The client code is the same as above – the interface did not change.

:bulb: [Observer with PropertyChangeEvent Python source code](src/designpatterns/behavioral/observer/propertychange/)

:pill: [Observer with PropertyChangeEvent pytest test](tests/behavioral/observer/propertychange/test_observer_property_change.py)

### State Pattern in Python

:pencil2: The State pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. The object will appear to change its class. Instead of using conditional logic scattered across the code, states encapsulate behavior and transitions explicitly.

In practice, each State encapsulates rules of transitions, and the Context delegates behavior to its current state.

**Use when:** behavior depends on a state with clear transitions (workflows, documents, orders).
**Avoid when:** there are only two or three states with trivial logic – a `match` over an enum is enough.

:bulb: [State Python source code](src/designpatterns/behavioral/state)

:pill: [State pytest test](tests/behavioral/state/test_state.py)

#### State client code example

```python
document = Document()
first_state = document.state_name
# "Draft"

document.publish()
second_state = document.state_name
# "Published"

document.archive()
third_state = document.state_name
# "Archived"
```

### Strategy Pattern in Python

:pencil2: The Strategy pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one of them, and make them interchangeable. It enables a client to choose a particular algorithm from the family of algorithms at runtime without altering the client's code.

The key idea behind the Strategy pattern is to encapsulate algorithms into separate classes and make them interchangeable. This allows the client to select the appropriate algorithm at runtime.

**Use when:** an algorithm must be exchangeable at runtime (pricing, sorting, calculation rules).
**Avoid when:** the algorithm never changes – a plain function is enough.

:bulb: [Strategy Python source code](src/designpatterns/behavioral/strategy/)

:pill: [Strategy pytest test](tests/behavioral/strategy/test_strategy.py)

#### Strategy client code example

```python
calculator = CalculatorContext()
calculator.set_behavior(AdditionStrategy())
calculator.calculate(2, 6)  # 8
calculator.set_behavior(MultiplicationStrategy())
calculator.calculate(2, 6)  # 12
```

### Template Method Pattern in Python

:pencil2: Gang of Four describes the purpose of the "Template Method" pattern as [follows:](https://archive.org/details/designpatternsel00gamm/page/324/mode/2up)
"Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure."

It's a way to outline the steps of a process while letting subclasses fill in the details. Think of it as a recipe: the main steps are fixed, but you can choose the ingredients for some parts.

**Use when:** several classes share the same process and differ only in individual steps.
**Avoid when:** deep inheritance hierarchies arise – prefer composition with a Strategy.

:bulb: [Template Method Python source code](src/designpatterns/behavioral/template)

:pill: [Template Method pytest test](tests/behavioral/template/test_template_method.py)

#### Template Method client code example

```python
user_processor = UserProcessor()
user_processor.process_data()
user_processor.saved_data       # [UserData("Alice"), UserData("John")] - overrides the process hook

product_processor = ProductProcessor()
product_processor.process_data()
product_processor.saved_data    # [ProductData("Laptop", 999.0), ProductData("Phone", 599.0)] - keeps the default hook
```

### Visitor Pattern in Python

:pencil2: The Visitor pattern allows operations to be performed on elements of a structure without changing the classes of those elements. This is achieved by defining a separate "Visitor" class that provides specific operations for each element type. The elements implement an "accept" method, which allows the Visitor to perform its operations on the element.

The Visitor pattern is often used when you want to perform operations on various elements of a structure without changing their class hierarchy. It provides a way to add new behavior to elements of a structure without modifying the elements themselves.

**Use when:** you add many operations to a stable class hierarchy.
**Avoid when:** new element types are added often – every visitor has to change. In modern Python, `functools.singledispatch` or a `match` statement are often simpler.

:bulb: [Visitor Python source code](src/designpatterns/behavioral/visitor)

:pill: [Visitor pytest test](tests/behavioral/visitor/test_visitor.py)

#### Visitor client code example

Python has no method overloading, so each visit method is named after its element type.

```python
zoo = ObjectStructure()
zoo.add_animal(LionElement())
zoo.add_animal(ElephantElement())

feeding_visitor = FeedingVisitor()
veterinarian_visitor = VeterinarianVisitor()
zoo.visit_animals(feeding_visitor)
zoo.visit_animals(veterinarian_visitor)
```

You could use the callable interface instead of defining `accept` on your own:

```diff
- class Element(Protocol):
-     def accept(self, visitor: Visitor) -> None: ...
+ class Element(Protocol):
+     def __call__(self, visitor: Visitor) -> None: ...
```

The loop in `ObjectStructure` would do the same job:

```diff
  def visit_animals(self, visitor: Visitor) -> None:
-     for animal in self.animals:
-         animal.accept(visitor)
+     for animal in self.animals:
+         animal(visitor)
```

## Run the examples

Requirements: Python 3.12+ and pytest.

```shell
git clone https://github.com/abach42/design-patterns-python.git
cd design-patterns-python
pip install pytest
pytest
```

Each pattern lives in its own package under `src/designpatterns/{creational|structural|behavioral}`, and the matching pytest tests are in `tests/`.

## References

* Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides: *Design Patterns: Elements of Reusable Object-Oriented Software* (Addison-Wesley, 1994) – the original "Gang of Four" book.

## License

This Python design patterns cheat sheet is licensed under the [GNU General Public License v3.0](LICENSE).
