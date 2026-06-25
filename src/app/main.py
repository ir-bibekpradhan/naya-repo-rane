import importlib.metadata
import os
import sys

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "docker-python")
APP_ENV = os.getenv("APP_ENV", "development")


def list_installed_packages() -> list[dict]:
    """Return a sorted list of installed packages with their versions."""
    packages = [
        {"name": dist.name, "version": dist.version}
        for dist in importlib.metadata.distributions()
    ]
    return sorted(packages, key=lambda p: p["name"].lower())


def main() -> None:
    print(f"=== {APP_NAME} | env={APP_ENV} | python={sys.version} ===\n")
    print("Installed packages:")
    print("-" * 40)
    for pkg in list_installed_packages():
        print(f"  {pkg['name']}=={pkg['version']}")
    print("-" * 40)
    print(f"Total: {len(list_installed_packages())} packages")


if __name__ == "__main__":
    main()
