# clothing-api

Hexagonal Architecture: Also known as Ports and Adapters architecture, it separates the core business logic from external interfaces. Python can be used to implement this architecture, keeping the core application independent of external dependencies and frameworks.

When structuring a project following a Hexagonal Architecture you can organize your project into folders to separate the core business logic from external dependencies. Below is an example folder structure for a simple Hexagonal Architecture project:

my_project/
│
├── adapters/
│ ├── database_adapter.py # Adapters for database interaction
│ ├── web_adapter.py # Adapters for web/API interaction
│ └── ...
│
├── core/
│ ├── application.py # Core application logic and use cases
│ ├── domain/
│ │ ├── entities.py # Domain entities and value objects
│ │ ├── repositories.py # Port definitions for data access
│ │ └── ...
│ └── services/
│ ├── user_service.py # Use case implementations
│ └── ...
│
├── main.py # Main application entry point
├── config.py # Configuration settings
└── tests/
├── test_core/ # Unit tests for core business logic
├── test_adapters/ # Unit tests for adapters
└── ...

adapters/: This folder contains adapter implementations for interacting with external dependencies. You might have subfolders for different types of adapters (e.g., database, web, messaging) or organize them by functionality.

core/: The core of your application is here, containing the application logic and use cases. It might have subfolders for domain entities and value objects, as well as services that implement your use cases. This is where you define your ports (interfaces) and use them in the core logic.

domain/entities.py: This is where you define your domain entities and value objects. These are the building blocks of your application's business logic.

domain/repositories.py: Port definitions (interfaces) for data access, such as database repositories.

services/: Subfolder for your use case implementations. Each use case is a service that orchestrates operations on domain entities and uses the ports to interact with external dependencies.

main.py: The main entry point of your application. Here, you assemble the application by creating instances of adapters and injecting them into the core use cases.

config.py: Configuration settings for your application.

tests/: Folder for your unit tests.

test_core/: Unit tests for the core business logic. You can use mocking or stubbing to isolate the core logic from external dependencies.

test_adapters/: Unit tests for your adapter implementations.

This structure allows you to clearly separate the core business logic from external dependencies, making it easier to maintain, test, and swap out different adapters when needed.

The use of class UserRepository(ABC): with ABC is a way to define an abstract base class (ABC) in Python. This approach is used to define an interface or a contract that concrete implementations must adhere to. Here's a brief explanation of the usage:

ABC (Abstract Base Class): In Python, an abstract base class is a class that cannot be instantiated directly. It serves as a blueprint for other classes, defining a set of methods that must be implemented by any concrete subclass. The ABC module in Python provides the tools to define and work with abstract base classes.

class UserRepository(ABC):: In the provided code, UserRepository is declared as an abstract base class by inheriting from ABC. This indicates that any class that inherits from UserRepository must provide concrete implementations for all the abstract methods declared in it. In this case, UserRepository serves as a contract or interface that specifies the methods that any database adapter must implement to interact with user data.

@abstractmethod: Inside UserRepository, you can use the @abstractmethod decorator to declare methods as abstract. Abstract methods are methods that are defined in the base class but do not have an implementation there. Subclasses inheriting from UserRepository are required to provide concrete implementations for these abstract methods.
