from powercli import Command
from powercli.utils import static
from pathlib import Path
from typing import Any
from enum import auto, IntEnum

class Direction(IntEnum):
    LATITUDINAL = auto()
    LONGITUDINAL = auto()

    @classmethod
    def from_str(cls, raw: str):
        match raw.lower():
            case "x" | "east" | "west" | "latitudinal":
                return cls.LATITUDINAL
            case "z" | "north" | "south" | "longitudinal":
                return cls.LONGITUDINAL
        raise ValueError(f"invalid value {raw!r}")

cmd: Command[Any, Any] = Command(name="movie-warp")
cmd.flag(identifier="fps", long="fps", description="Frames per second to use for the output", values=[("FLOAT", float)], default=static([1.0]))
cmd.flag(identifier="name", long="name", description="The prefix name of the structure", values=[("STRING", str)], required=static(True))
cmd.flag(identifier="port", long="port", description="The port to use for the server", values=[("PORT", int)], default=static([6464]))
cmd.flag(identifier="host", long="host", description="The host to use for the server", values=[("HOST", str)], default=static(["localhost"]))
cmd.flag(identifier="direction", long="direction", description="The direction to use", values=[("X|Z|EAST|WEST|NORTH|SOUTH|LATITUDINAL|LONGITUDINAL", Direction.from_str)], default=static([Direction.LATITUDINAL]))
cmd.flag(identifier="width", short="w", long="width", description="The width of the video output", values=[("INT", int)], default=static([64]))
cmd.flag(identifier="height", short="h", long="height", description="The height of the video output", values=[("INT", int)], default=static([16]))
cmd.pos(identifier="video", description="Path to the video file", name="PATH", into=Path)
