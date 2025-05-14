#!/usr/bin/env python3
"""
Script to automatically update pyproject.toml when new components are added to src/.
This script will:
1. Scan the src/ directory for components (subdirectories)
2. Update the packages list in the hatch.build.targets.wheel section
3. All packages are installed by default (no optional dependencies)
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
    Only updates the tool.hatch.build.targets.wheel.packages section.
    All packages are installed by default (no optional dependencies).
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

        # 1. Update project dependencies to include reflex if needed
        project_pattern = r"(\[project\]\s*)(.*?)(\n\[|\Z)"
        project_match = re.search(project_pattern, content, re.DOTALL)

        if project_match:
            project_section = project_match.group(2)

            # Check if we need to update dependencies to include reflex
            deps_pattern = r"dependencies\s*=\s*(\[.*?\])"
            deps_match = re.search(deps_pattern, project_section, re.DOTALL)

            if deps_match:
                # Extract current dependencies
                deps_str = deps_match.group(1)
                # Check if reflex is already included
                if '"reflex' not in deps_str and "'reflex" not in deps_str:
                    # Add reflex to the dependencies list
                    # Remove the closing bracket
                    deps_list = deps_str[:-1].strip()
                    # Add reflex if the list is not empty
                    if deps_list.endswith("]"):
                        deps_list = deps_list[:-1].strip()

                    if deps_list.endswith('"') or deps_list.endswith("'"):
                        deps_list += ', "reflex>=0.7.9"]'
                    else:
                        deps_list += '"reflex>=0.7.9"]'

                    # Update the content
                    new_project_section = project_section.replace(deps_str, deps_list)
                    content = (
                        content[: project_match.start(2)]
                        + new_project_section
                        + content[project_match.end(2) :]
                    )
            else:
                # Dependencies not found, add them after the project section
                new_deps = '\ndependencies = ["reflex>=0.7.9"]\n'
                new_project_section = project_section + new_deps
                content = (
                    content[: project_match.start(2)]
                    + new_project_section
                    + content[project_match.end(2) :]
                )

        # 2. Remove the optional dependencies section if it exists
        dependencies_pattern = r"(\[project\.optional-dependencies\]\s*)(.*?)(\n\[|\Z)"
        dependencies_match = re.search(dependencies_pattern, content, re.DOTALL)

        if dependencies_match:
            # Remove the entire section
            start_pos = dependencies_match.start()
            end_pos = dependencies_match.end() - len(dependencies_match.group(3))
            content = content[:start_pos] + content[end_pos:]

        # 3. Update packages list in the wheel build section
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
            # Section doesn't exist, add it
            hatch_build_pattern = r"(\[tool\.hatch\.build\]\s*)(.*?)(\n\[|\Z)"
            hatch_build_match = re.search(hatch_build_pattern, content, re.DOTALL)

            if hatch_build_match:
                # Add to existing hatch.build section
                packages = [f"src/{base_package}"]
                packages.extend([f"src/{component}" for component in components])
                packages_str = str(packages).replace("'", '"')

                new_section = "\n[tool.hatch.build.targets.wheel]\n"
                new_section += f"packages = {packages_str}\n"

                if hatch_build_match.group(3).startswith("\n["):
                    new_section += "\n"

                content = (
                    content[: hatch_build_match.end() - len(hatch_build_match.group(3))]
                    + new_section
                    + content[
                        hatch_build_match.end() - len(hatch_build_match.group(3)) :
                    ]
                )
            else:
                # Add both sections if they don't exist
                packages = [f"src/{base_package}"]
                packages.extend([f"src/{component}" for component in components])
                packages_str = str(packages).replace("'", '"')

                new_section = "\n[tool.hatch.build]\n\n"
                new_section += "[tool.hatch.build.targets.wheel]\n"
                new_section += f"packages = {packages_str}\n\n"

                # Add at the end of file
                content += new_section

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
        print("No components found in the src/ directory.")
        print(f"Only the base package '{base_package}' is present.")
        return

    print(f"Found {len(components)} components: {', '.join(components)}")

    count = update_pyproject_toml(components, base_package)
    print(f"Updated pyproject.toml with {count} components.")
    print("All components will be installed by default.")
    print("pyproject.toml has been updated successfully!")


if __name__ == "__main__":
    main()
