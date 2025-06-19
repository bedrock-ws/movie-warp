from attrs import define
from moviepy import VideoClip
from .cli import Direction

@define(kw_only=True)
class Config:
    fps: float
    name: str
    direction: Direction
    width: int
    height: int
    video: VideoClip
