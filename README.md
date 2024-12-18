# Asteroids Arcade Game

A Python implementation of the classic **Asteroids** arcade game using the `pygame` library. Players control a spaceship, avoiding and destroying asteroids to earn points.

## Table of Contents
- [Game Features](#game-features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Screenshots](#screenshots)
- [License](#license)

---

## Game Features
- **Classic gameplay**: Control a spaceship, destroy asteroids, and avoid collisions.
- **Power-ups**: Gain shields or double-fire capabilities.
- **Realistic mechanics**: Physics-based movement for asteroids and the spaceship.
- **Dynamic difficulty**: More asteroids and faster speeds as you progress.

---

## Installation

### Prerequisites
Make sure you have Python 3.7+ installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Shramkoweb/asteroids.git
   cd asteroids
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the game:
   ```bash
   python main.py
   ```

---

## How to Play
- **Move the spaceship**:
  - `Arrow keys`: Rotate and thrust.
  - `Space`: Shoot lasers.
- **Objective**:
  - Destroy all asteroids without being hit.
  - Large asteroids break into smaller pieces when hit.
- **Scoring**:
  - Points are awarded based on asteroid size: smaller asteroids yield more points.
- **Game Over**:
  - Collision with an asteroid ends the game.

---

## Controls
| Action         | Key         |
|----------------|-------------|
| Rotate Left    | Left Arrow  |
| Rotate Right   | Right Arrow |
| Thrust         | Up Arrow    |
| Fire           | Spacebar    |
| Quit           | Escape      |

---

## Screenshots
WIP

---

## Contributing
1. Fork the project.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License.