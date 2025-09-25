from datetime import timezone, datetime
from dateutil.parser import parse
from health.domain.entities import HealthRecord


class HealthRecordService:
    def __init__(self):
        """Initialize the health record service"""
        pass

    @staticmethod
    def create_record(device_id: str, bpm: float, created_at: str|None) -> HealthRecord:
        """Create a new health record.

        Args:
            device_id (str): Identifier for the device that recorded the data.
            bpm (float): Beats per minute recorded.
            created_at (str|None): Timestamp when the record was created in ISO 8601
        Returns:
            HealthRecord: The created health record instance.
        Raises:
            ValueError: If the input data is invalid.
        """
        try:
            bpm = float(bpm)
            if not (0 <= bpm <= 200):
                raise ValueError("Invalid BPM value, BPM must be between 0 and 200.")
            if created_at:
                parsed_created_at = parse(created_at).astimezone(timezone.utc)
            else:
                parsed_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid input data for creating a health record.")

        return HealthRecord(device_id, bpm, parsed_created_at)