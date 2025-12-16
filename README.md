# Asteroids

A modern implementation of the classic arcade game "Asteroids," built with Python and Pygame. This project demonstrates object-oriented programming, vector mathematics for game physics, and collision detection.

## Features

* **Player Physics:** Smooth acceleration, deceleration, and rotation controls using vector math.
* **Shooting Mechanics:** Weapon system with rate-of-fire limitations (cooldowns) and projectile physics.
* **Asteroid Splitting:** Asteroids break into smaller chunks with randomized trajectories when hit.
* **Collision System:** Circle-based hitbox detection for interactions between game objects.

## Tech Stack

* **Language:** Python 3
* **Library:** Pygame (Community Edition)
* **Package Manager:** uv

## Installation & Setup

This project uses `uv` for dependency management and execution to ensure a consistent environment.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tluong1116/asteroid-game
   cd asteroid-game
   ```

2. **Run the game:** Since the project uses uv, you do not need to manually install dependencies. The following command will sync dependencies from uv.lock and start the game in an isolated environment.
    ```bash
    uv run main.py
    ```

## Controls

* **W**: Move Forward
* **S**: Move Backward
* **A**: Rotate Left
* **D**: Rotate Right
* **SPACE**: Shoot

## Project Structure

* `main.py`: The entry point of the game containing the game loop.
* `constants.py`: Global configuration variables (screen size, physics constants, colors).
* `player.py`: Player class logic, including movement and shooting.
* `asteroid.py`: Asteroid behavior, including splitting mechanics.
* `shot.py`: Projectile logic.
* `circleshape.py`: Base class for all circular game objects (handles collision math).

## License

This project is for educational purposes.