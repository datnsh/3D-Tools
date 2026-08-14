# 3D-Tools

A collection of Python-based tools developed to automate and streamline common 3D asset production workflows in **Autodesk 3ds Max**.

The project focuses on reducing repetitive manual tasks, improving asset consistency, and providing small utilities that can be integrated into an artist's production workflow.
# Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Tools](#tools)
* [Extrude Tools](#extrude-tools)
* [Architecture](#architecture)
* [Requirements](#requirements)
* [Installation](#installation)
* [Running a Tool](#running-a-tool)
* [3ds Max Integration](#3ds-max-integration)
* [Development](#development)
* [Design Goals](#design-goals)
* [Tech Stack](#tech-stack-1)
* [Project Purpose](#project-purpose)
* [License](#license)

# Features

The project currently contains the following tools:

| Tool                  | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| **Pivot Placer**      | Automates pivot placement and transfer operations between objects.     |
| **Validation Tool**   | Validates 3D assets against predefined production requirements.        |
| **Polycount Checker** | Checks polygon counts of selected or scene objects.                    |
| **Scale Plane**       | Provides utilities for working with and scaling planes in the scene.   |
| **Update Famas**      | Automates updates to Famas-related assets or scene data.               |
| **Extrude Tools**     | Provides utilities for automating common extrusion-related operations. |

---

# Project Structure

```text
3D-Tools/
│
├── Extrude_Tools/
│   └── ...
│
├── Scale_Plane/
│   ├── Controller/
│   ├── Model/
│   ├── View/
│   └── ...
│
├── Validation_Tool/
│   └── ...
│
├── pivot_placer/
│   └── ...
│
├── polycount_checker/
│   └── ...
│
├── update_famas/
│   └── ...
│
├── assets/
│   └── ...
│
└── README.md
```

Each tool is organized as an independent module so that it can be developed, tested, and maintained separately.

---

# Tools

## Pivot Placer

A 3ds Max utility for managing object pivots.

The tool provides functionality for transferring or applying pivot information between objects, reducing the amount of manual pivot adjustment required during asset preparation.

### Tech stack

* Python
* PySide2
* Autodesk 3ds Max
* Qt

---

## Validation Tool

A validation utility designed to check whether assets satisfy predefined production requirements.

The tool can perform automated checks on scene and asset data, allowing issues to be identified before assets are passed further down the production pipeline.

Typical validation requirements can include:

* Asset naming conventions
* File formats
* Asset properties
* Metadata
* Scene configuration
* Production-specific requirements

The tool provides a graphical interface integrated with 3ds Max.

### Technologies

* Python
* PySide2
* Autodesk 3ds Max
* Qt

---

## Polycount Checker

A utility for checking polygon counts within a 3ds Max scene.

It is intended to provide artists with a quick way to inspect polygon usage and identify objects that may exceed project requirements.

### Technologies

* Python
* Autodesk 3ds Max

---

## Scale Plane

A utility for working with plane objects and their scale within 3ds Max.

The tool follows a separation between its UI, application logic, and data/model components.

```text
Scale_Plane/
├── Controller/
├── Model/
└── View/
```

This structure makes the tool easier to maintain and extend as additional functionality is introduced.

### Technologies

* Python
* PySide2
* Autodesk 3ds Max
* Qt

---

## Update Famas

A production utility for automating updates to Famas-related scene or asset data.

The purpose of the tool is to replace repetitive manual operations with a consistent automated workflow.

### Technologies

* Python
* Autodesk 3ds Max

---

## Extrude Tools

A collection of utilities for automating common extrusion operations in 3ds Max.

These tools are intended to simplify repetitive modeling operations and improve artist workflow efficiency.

### Technologies

* Python
* Autodesk 3ds Max

---

# Architecture

The project is primarily written in **Python** and uses **PySide2/Qt** for tools that require a graphical interface.

Where appropriate, individual tools separate their responsibilities into different components.

For example:

```text
┌───────────────┐
│     View      │
│   PySide2 UI  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  Controller   │
│ Application   │
│    Logic      │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     Model     │
│ Data / Scene  │
│   Operations  │
└───────────────┘
```

This approach keeps UI code separate from the underlying tool logic and makes individual components easier to modify and test.

---

# Requirements

The tools are designed to run inside **Autodesk 3ds Max** and depend on the Python environment provided by the corresponding 3ds Max version.

Depending on the tool, additional dependencies may include:

* Python
* PySide2
* Qt
* 3ds Max Python API

Some tools may also depend on project-specific assets, configuration files, or 3ds Max scene data.

> **Note:** The exact 3ds Max version and Python/PySide2 versions should match the environment for which each tool was developed.

---

# Installation

Clone or download the repository:

```bash
git clone https://github.com/datnsh/3D-Tools.git
```

Then copy the required tool folders into a location accessible from your 3ds Max Python environment.

For development, the repository can be kept in a dedicated tools directory:

```text
D:/3D-Tools/
```

The individual tools can then be executed through 3ds Max's Python environment.

---

# Running a Tool
## Method 1:
Most tools provide a Python entry point through `main.py`.

For example:

```python
import runpy

runpy.run_path(
    r"D:\3D-Tools\pivot_placer\main.py",
    run_name="__main__"
)
```
## Method 2:
### (Note that this is the quickest and easiest method to run the tools)
Alternatively, the tools' entry points can be opened in the Max Editor inside 3ds Max and run using either Ctrl+E or Tools->Evaluate All.

For tools with a graphical interface, the UI is created as a child of the 3ds Max main window.

For example:

```python
from qtmax import GetQMaxMainWindow

parent = GetQMaxMainWindow()
```

This allows PySide2 interfaces to behave like native 3ds Max windows.

---

# 3ds Max Integration

The project is intended to eventually provide a centralized interface for launching the individual tools directly from 3ds Max.

A potential tool launcher can expose the utilities through a toolbar:

```text
┌─────────────────────────────────────────────────────────────┐
│  Pivot  │  Validation  │  Polycount  │  Scale  │  Update  │
│  Placer │     Tool     │   Checker  │  Plane  │  Famas   │
└─────────────────────────────────────────────────────────────┘
```

Each button can launch its corresponding tool while keeping the implementation of each tool independent.

This allows new tools to be added without modifying the existing tool implementations.

---

# Development

The project is organized as a collection of independent tools rather than one monolithic application.

When adding a new tool, the recommended structure is:

```text
New_Tool/
│
├── main.py
├── Controller/
├── Model/
├── View/
└── assets/
```

Not every tool requires all of these components. Simple utilities can use a smaller structure when appropriate.

For example:

```text
Simple_Tool/
├── main.py
└── tool.py
```

The important principle is to keep the tool's entry point separate from its implementation.

---

# Design Goals

The main goals of the project are:

* **Automation** — Replace repetitive manual operations with scripts.
* **Consistency** — Apply production rules consistently across assets.
* **Efficiency** — Reduce the time required to perform common tasks.
* **Maintainability** — Keep individual tools independent and easy to modify.
* **Usability** — Provide simple interfaces for artists working inside 3ds Max.
* **Extensibility** — Make it easy to add new production tools.

---

# Tech stack

* **Python**
* **PySide2**
* **Qt**
* **Autodesk 3ds Max**
* **3ds Max Python API**
* **Git**
---

# Project Purpose

3D-Tools was created to explore and develop practical automation solutions for 3D production workflows.

The project demonstrates the use of Python scripting, desktop UI development, application architecture, and 3ds Max integration to build tools that solve practical problems encountered during asset production.

The tools are designed around a simple principle:

> **Automate repetitive work so artists can focus on creating assets.**

---

# License

This project is currently intended for personal and portfolio use.

Add an appropriate license here if the project is intended to be distributed publicly.

```
```
