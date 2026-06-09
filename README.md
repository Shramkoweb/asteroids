# Asteroids

A minimalist clone of the classic Asteroids arcade game, built in Python with [pygame](https://www.pygame.org/).

[![Python](https://img.shields.io/badge/python-3.13%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![pygame](https://img.shields.io/badge/pygame-2.6.1-green)](https://www.pygame.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

## Features

- Frame-rate-independent movement at 60 FPS
- Asteroids spawn from screen edges and split into smaller fragments when shot
- Shot cooldown and per-frame circle collision detection
- JSONL state/event logger (`game_state.jsonl`, `game_events.jsonl`) for replay analysis

## Requirements

- Python **3.13+**
- [uv](https://docs.astral.sh/uv/) for dependency management (recommended)

## Install

```bash
git clone https://github.com/Shramkoweb/asteroids.git
cd asteroids
uv sync
```

## Run

```bash
uv run python main.py
```

## Controls

| Key          | Action               |
|--------------|----------------------|
| `W` / `S`    | Thrust forward / back |
| `A` / `D`    | Rotate left / right  |
| `Space`      | Shoot                |
| Window close | Quit                 |

Colliding with an asteroid ends the game.

## Project layout

```
.
├── main.py            # Game loop, sprite groups, collision dispatch
├── player.py          # Player ship: input, movement, shooting
├── asteroid.py        # Asteroid sprite and splitting logic
├── asteroidfield.py   # Timed asteroid spawner at screen edges
├── shot.py            # Player projectile
├── circleshape.py     # Base class for circular sprites with collision
├── constants.py       # Tunable gameplay constants
└── logger.py          # JSONL state/event logger
```

Gameplay tuning lives in [`constants.py`](constants.py) — screen size, player speed, spawn rate, asteroid radii, shot cooldown.

## License

[MIT](LICENSE) &copy; Serhii Shramko
