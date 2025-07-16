# Movie Warp

This tool warps any video into your Minecraft world!

## Installation

```console
pipx install git+https://github.com/bedrock-ws/movie-warp.git
```

## Usage

```console
moviewarp --name movie --fps 0.5 video.mp4
```

> [!TIP]
> More options can be shown with `moviewarp --help`.

```mcfunction
/connect localhost:6464
```

To generate the frames, go to any free space and type this into the chat.

```text
moviewarp
```

The frames will be saves as structures named `moviewarp.{name}.frame{i}` where
`name` is the name given in the CLI and `i` the frame index starting from 0.
