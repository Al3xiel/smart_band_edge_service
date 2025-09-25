# Smart Band Edge Service (smart_band_edge_service)

## Overwiew

Smnart Band Edge Service is an application designed to run on edge devices, providing real-time data processing and analysis for smart band devices. It leverages edge computing to minimize latency and enhance performance, making it ideal for applications that require immediate feedback and low power consumption.

## Dependencies
- Python 3.13+
- Flask (web framework)
- Peeweee (ORM for database interactions)
- SQLite (lightweight database)
- python-dateutil (date and time utilities)

## Domain-Driven Design (DDD) Structure

The project is structured following Domain-Driven Design principles, which helps in organizing the codebase into distinct layers and modules. The main components include:

- **Health Monitoring**: Manages health-related data and metrics, including heart rate.
- **Identity and Access Management**: Handles device authentication and authorization.

## User Stories
The user stories for the Smart Band Edge Service can be found in the [docs/user_stories.md](docs/user_stories.md) file.

## Class Diagram
Class diagram illustrating the architecture and relationships between different components of the system are available in the [docs/class_diagram.md](docs/class_diagram.md) file.
