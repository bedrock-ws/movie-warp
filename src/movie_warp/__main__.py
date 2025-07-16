from .cli import cmd, Direction
from .config import Config
from typing import cast
from moviepy import VideoFileClip
from adorable.color import Color3bit as color
from math import floor
from .server import server

def run() -> None:
    args = cmd.parse_args()

    config = Config(
        fps=cast(list[float], args.value_of("fps"))[0],
        video=VideoFileClip(args.value_of("video")),
        height=cast(list[int], args.value_of("height"))[0],
        width=cast(list[int], args.value_of("width"))[0],
        direction=cast(list[Direction], args.value_of("direction"))[0],
        name=cast(list[str], args.value_of("name"))[0],
    )

    host = cast(list[str], args.value_of("host"))[0]
    port = cast(list[int], args.value_of("port"))[0]

    frames_count = floor(config.video.duration * config.fps)
    input(f"Press enter to confirm generating {color.from_name("yellow").fg:~{frames_count}} frames")
    server(config).start(host, port)

if __name__ == "__main__":
    run()
