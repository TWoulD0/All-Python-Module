from typing import Dict
import sys
import importlib
import numpy
import pandas
import matplotlib.pyplot as plt


def check_dependency(module_name: str) -> Dict[str, str]:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {module_name} ({version})")
        return {"name": module_name, "version": version}
    except ImportError:
        print(f"[MISSING] {module_name} is not installed")
        return {"name": module_name, "version": "missing"}


def analyze_data() -> None:
    print("\nAnalyzing Matrix data...")
    data = numpy.random.normal(loc=50, scale=15, size=1000)
    df = pandas.DataFrame({"signal_strength": data})

    print("Processing 1000 data points...")
    plt.figure()
    df["signal_strength"].hist(bins=40)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")

    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Generating visualization...")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    deps = ["pandas", "requests", "matplotlib", "numpy"]
    results = [check_dependency(dep) for dep in deps]

    if any(dep["version"] == "missing" for dep in results):
        print("\nSome dependencies are missing.")
        sys.exit(1)

    analyze_data()


if __name__ == "__main__":
    main()
