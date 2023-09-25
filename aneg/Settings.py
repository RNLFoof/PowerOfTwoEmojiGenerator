import json
import json5

from pydantic import BaseModel


class Settings(BaseModel):
    size_multiplier_range: tuple[float, float]

    def __init__(self, settings_location="settings.json5"):
        with open(settings_location, "rb") as f:
            super().__init__(**json5.load(f))

    @classmethod
    def dump_schema(cls, dump_location="settings_schema.json") -> None:
        with open(dump_location, "w") as f:
            f.write(
                json.dumps(
                    cls.model_json_schema(), indent=4
                )
            )
