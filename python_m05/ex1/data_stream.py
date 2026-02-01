from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.total_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [d for d in data_batch if criteria in str(d)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": self.stream_type,
            "total_processed": self.total_processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total_processed = len(data_batch)
            temps = []
            for data in data_batch:
                if not isinstance(data, str):
                    return "Error: Invalid data type"

                if "temp:" in data:
                    temp_value = float(data.split("temp:")[1])
                    temps.append(temp_value)

            if temps:
                avg = sum(temps) / len(temps)
            else:
                avg = 0

            return (f"Sensor analysis: {self.total_processed} "
                    f"readings processed, avg temp: {avg}°C")

        except Exception:
            return "Error: processing sensor"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            return [data for data in data_batch if "temp" in data]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total_processed = len(data_batch)
            buys = []
            sells = []

            for data in data_batch:
                if not isinstance(data, str):
                    return "Error: Invalid data type"

                if "buy:" in data:
                    buy_value = float(data.split("buy:")[1])
                    buys.append(buy_value)
                elif "sell:" in data:
                    sell_value = float(data.split("sell:")[1])
                    sells.append(sell_value)

            net_flow = sum(buys) - sum(sells)
            sign = ("+" if net_flow > 0 else "")
            return (f"Transaction analysis: {self.total_processed} "
                    f"operations, net flow: {sign}{net_flow} units")

        except Exception:
            return "Error: processing transaction"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        for data in data_batch:
            if ":" not in data:
                return super().filter_data(data_batch, criteria)
        if criteria == "large":
            return [data for data in data_batch
                    if float(data.split(":")[1]) > 100]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.total_processed = len(data_batch)

            num_error = 0
            for data in data_batch:
                if not isinstance(data, str):
                    return "Error: Invalid data type"

                if "error" in data:
                    num_error += 1

            return (f"Event analysis: {self.total_processed} "
                    f"events, {num_error} error detected")

        except Exception:
            return "Error: processing event"


class StreamProcessor():
    def __init__(self):
        self.streams: List[DataStream] = []
        self.batch_number = 0

    def add_stream(self, stream: DataStream):
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def processing_all_batch(self, batches: List[List[str]]) -> None:
        self.batch_number += 1
        print(f"\nBatch {self.batch_number} Results:")

        try:
            i = 0
            for stream in self.streams:
                if i < len(batches):
                    if isinstance(stream, SensorStream):
                        print("- Sensor data: "
                              f"{len(batches[i])} readings processed")
                    elif isinstance(stream, TransactionStream):
                        print("- Transaction data: "
                              f"{len(batches[i])} operations processed")
                    elif isinstance(stream, EventStream):
                        print("- Event data: "
                              f"{len(batches[i])} events processed")
                i += 1

        except Exception as e:
            print(f"Error: {e}")

    def filtering(self, batches: List[List[Any]],
                  criteria: List[Optional[str]]) -> None:
        print("\nStream filtering active: High-priority data only")
        try:
            critical_sensor = 0
            large_transaction = 0
            i = 0

            for stream in self.streams:
                if i < len(batches) and i < len(criteria):
                    filtered = stream.filter_data(batches[i], criteria[i])

                    if isinstance(stream, SensorStream) and filtered:
                        critical_sensor = len(filtered)
                    elif isinstance(stream, TransactionStream) and filtered:
                        large_transaction = len(filtered)
                i += 1

            print(f"Filtered results: {critical_sensor} critical sensor alerts"
                  f", {large_transaction} large transaction")

        except Exception as e:
            print(f"Error: {e}")


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream("SENSOR_001")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("\nInitializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: [{", ".join(sensor_data)}]")
    print(sensor.process_batch(sensor_data))

    transaction = TransactionStream("TRANS_001")
    transaction_data = ["buy:100", "sell:150", "buy:75"]
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, "
          f"Type: {transaction.stream_type}")
    print(f"Processing transaction batch: [{", ".join(transaction_data)}]")
    print(transaction.process_batch(transaction_data))

    event = EventStream("EVENT_001")
    event_data = ["login", "error", "logout"]
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, "
          f"Type: {event.stream_type}")
    print(f"Processing event batch: [{", ".join(event_data)}]")
    print(event.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    batches = [
        ["temp:22.5", "humidity:65"],
        ["buy:100", "sell:150", "buy:75", "sell:100"],
        ["login", "error", "logout"]
    ]

    processor.processing_all_batch(batches)

    processor.filtering(
        [["temp:22", "temp:25"], ["buy:150"]],
        ["critical", "large"])

    print("\nAll streams processed successfully. Nexus throughput optimal.")


main()
