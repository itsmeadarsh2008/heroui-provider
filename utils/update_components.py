#!/usr/bin/env python3
"""
Script to automatically update pyproject.toml when new components are added to src/.
This script will:
1. Scan the src/ directory for components (subdirectories)
2. Update the optional dependencies in pyproject.toml (project.optional-dependencies)
3. Update the packages list in the hatch.build.targets.wheel section
"""

import os
import sys
import re
from pathlib import Path

try:
    import rtoml
except ImportError:
    print("Error: This script requires rtoml to be installed.")
    print("Please install the development dependencies: pip install -e '.[dev]'")
    sys.exit(1)


def scan_components():
    """Scan the src/ directory for components."""
    # Updated to go up one directory level to find src/
    src_dir = Path(__file__).parent.parent / "src"
    components = []

    # The provider is the base package and should not be included in optional dependencies
    base_package = "provider"

    for item in src_dir.iterdir():
        if (
            item.is_dir()
            and (item / "__init__.py").exists()
            and item.name != base_package
        ):
            components.append(item.name)

    return components, base_package


def update_pyproject_toml(components, base_package):
    """
    Update the pyproject.toml file with the discovered components.
    Only updates specific sections: project.optional-dependencies and tool.hatch.build.targets.wheel.packages
    """
    # Updated to go up one directory level to find pyproject.toml
    toml_path = Path(__file__).parent.parent / "pyproject.toml"

    try:
        # Read the entire file content
        with open(toml_path, "r") as f:
            content = f.read()

        # Create a backup of the original file
        backup_path = toml_path.with_suffix(".toml.bak")
        with open(backup_path, "w") as f:
            f.write(content)

        # Use regex to directly update specific sections in the file
        # This avoids TOML serialization issues

        # 1. Update optional dependencies section
        # Find the project.optional-dependencies section
        dependencies_pattern = r"(\[project\.optional-dependencies\]\s*)(.*?)(\n\[|\Z)"
        dependencies_match = re.search(dependencies_pattern, content, re.DOTALL)

        if dependencies_match:
            # Keep dev dependencies if they exist
            new_deps_section = "[project.optional-dependencies]\n"

            # Check for dev dependency in the current content
            dev_pattern = r"dev\s*=\s*(\[.*?\])"
            dev_match = re.search(dev_pattern, dependencies_match.group(2), re.DOTALL)

            if dev_match:
                new_deps_section += f"dev = {dev_match.group(1)}\n"

            # Add component dependencies
            for component in components:
                new_deps_section += f'{component} = ["reflex>=0.7.9"]\n'

            # Add a newline at the end if there's a section following
            if dependencies_match.group(3).startswith("\n["):
                new_deps_section += "\n"

            # Replace the section in the content
            content = (
                content[: dependencies_match.start()]
                + new_deps_section
                + content[dependencies_match.end() - len(dependencies_match.group(3)) :]
            )
        else:
            # Section doesn't exist, add it after project section
            project_pattern = r"(\[project\]\s*)(.*?)(\n\[|\Z)"
            project_match = re.search(project_pattern, content, re.DOTALL)

            if project_match:
                # Create the new section
                new_deps_section = "\n[project.optional-dependencies]\n"
                for component in components:
                    new_deps_section += f'{component} = ["reflex>=0.7.9"]\n'
                new_deps_section += 'dev = ["rtoml>=0.9.0"]\n'

                # Add it after the project section
                if project_match.group(3).startswith("\n["):
                    new_deps_section += "\n"

                content = (
                    content[: project_match.end() - len(project_match.group(3))]
                    + new_deps_section
                    + content[project_match.end() - len(project_match.group(3)) :]
                )

        # 2. Update packages list in the wheel build section
        wheel_pattern = r"(\[tool\.hatch\.build\.targets\.wheel\]\s*)(.*?)(\n\[|\Z)"
        wheel_match = re.search(wheel_pattern, content, re.DOTALL)

        if wheel_match:
            # Create the new packages list
            packages = [f"src/{base_package}"]
            packages.extend([f"src/{component}" for component in components])
            packages_str = str(packages).replace("'", '"')

            # Extract existing wheel section properties except packages
            existing_props = ""
            for line in wheel_match.group(2).split("\n"):
                if line.strip() and not line.strip().startswith("packages"):
                    existing_props += line + "\n"

            # Create the new section
            new_wheel_section = "[tool.hatch.build.targets.wheel]\n"
            new_wheel_section += existing_props
            new_wheel_section += f"packages = {packages_str}\n"

            # Add a newline at the end if there's a section following
            if wheel_match.group(3).startswith("\n["):
                new_wheel_section += "\n"

            # Replace the section in the content
            content = (
                content[: wheel_match.start()]
                + new_wheel_section
                + content[wheel_match.end() - len(wheel_match.group(3)) :]
            )
        else:
            # Section doesn't exist, add it at the end
            # This is a more complex case as it may require creating parent sections
            # For simplicity, let's assume the appropriate parent sections exist
            pass

        # Write the updated content back to pyproject.toml
        with open(toml_path, "w") as f:
            f.write(content)

        return len(components)
    except Exception as e:
        print(f"Error processing pyproject.toml: {str(e)}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


def main():
    print("Scanning src/ directory for components...")
    components, base_package = scan_components()

    if not components:
        print("No optional components found in the src/ directory.")
        print(f"Only the base package '{base_package}' is present.")
        return

    print(f"Found {len(components)} optional components: {', '.join(components)}")

    count = update_pyproject_toml(components, base_package)
    print(f"Updated pyproject.toml with {count} optional components.")
    print("pyproject.toml has been updated successfully!")


if __name__ == "__main__":
    main()
