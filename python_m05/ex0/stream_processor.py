from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        try:
            count = len(data)
            total = sum(data)
            average = total / count
            return (f"Processed {count} numeric values, "
                    f"sum={total}, avg={average}")
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        try:
            if isinstance(data, list) and len(data) > 0:
                return all(isinstance(x, int) for x in data)
            return False
        except Exception:
            return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid Text data")

        try:
            chars = len(data)
            words = len(data.split())
            return f"Processed text: {chars} characters, {words} words"
        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        try:
            log_levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
            level = "INFO"

            for lvl in log_levels:
                if lvl in data.upper():
                    level = lvl
                    break

            message = data
            for lvl in log_levels:
                if f"{lvl}" in data:
                    message = data.split(f"{lvl}:", 1)[1].strip()
                    break

            alert_prefix = "[ALERT]" if level == "ERROR" else "[INFO]"
            return f"{alert_prefix} {level} level detected: {message}"

        except Exception as e:
            return f"Error: {e}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0


def polymorphic(processors: list[DataProcessor], all_data: list[Any]) -> None:
    print("Processing multiple data types through same interface...")

    for i in range(len(processors)):
        processor = processors[i]
        data = all_data[i]
        result = i + 1

        try:
            if processor.validate(data):
                print(f"Result {result}: {processor.process(data)}")
            else:
                print(f"Result {result}: failed")
        except Exception as e:
            print(f"Result {result}: Error - {e}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    numeric_proc = NumericProcessor()
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    if numeric_proc.validate(numeric_data):
        print("Validation: Numeric data verified")
        result = numeric_proc.process(numeric_data)
        print(numeric_proc.format_output(result))

    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    text_data = "Hello Nexus World"
    print(f"Processing data: {text_data}")
    if text_proc.validate(text_data):
        print("Validation: Numeric data verified")
        result = text_proc.process(text_data)
        print(text_proc.format_output(result))

    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    log_data = "ERROR: Connection timeout"
    print(f"Processing data: {log_data}")
    if log_proc.validate(log_data):
        print("Validation: Log entry verified")
        result = log_proc.process(log_data)
        print(log_proc.format_output(result))

    print("\n=== Polymorphic Processing Demo ===")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    all_data = [[1, 2, 3], "Hello World.", "INFO: System ready"]
    polymorphic(processors, all_data)
    print("\nFoundation systems online. Nexus ready for advanced streams.")


main()
