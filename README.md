# Handzzle

**Handzzle** is an innovative hand-gesture recognition puzzle game designed for art museums. It leverages gamification principles to enhance visitor engagement and offers an interactive and educational experience for people of all ages.

## Features

- **Hand Gesture Recognition**: Solve puzzles using hand movements, powered by Mediapipe's real-time hand tracking.
- **Museum Integration**: Engage with artworks through gesture-based puzzles.
- **Gamification Benefits**:
  - Increases engagement.
  - Facilitates mistake-driven learning.
  - Makes education fun and interactive.

## How It Works

1. **Choose a Category**: Select from art styles like Impressionism, Expressionism, Renaissance, or Romanticism.
2. **Interactive Puzzle Solving**: Use hand gestures to drag and drop puzzle pieces, recreating famous paintings.
3. **Touch Simulation**: Gestures are translated into simulated touch inputs for Unity, enabling natural interactions.

## System Requirements

- **Hardware**:
  - Full HD screen (1920x1080).
  - Full HD camera with a matching resolution.
  - Computer capable of running the system.
- **Software**:
  - Mediapipe for hand gesture detection.
  - Unity for game development and interface design.
  - Python for gesture data processing.

## Technology Stack

- **Mediapipe**: For hand landmark detection and gesture recognition.
- **Unity**: Used for game development due to its robust tools and ease of use.
- **Python**: Handles data processing and sends hand gesture coordinates to Unity.
- **Socket Library**: Facilitates real-time data transfer between Python and Unity.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/handzzle.git
   ```
2. Install Python dependencies:
   ```bash
   pip install mediapipe
   ```
3. Open the Unity project located in the `HandzzleUnity` folder.
4. Connect your Full HD camera and ensure the resolution matches the screen.
5. Run the Python script to initiate hand tracking.
6. Launch the Unity application to start the game.

## Future Developments

- Adding hints to assist users in solving puzzles.
- Including painting references during gameplay.
- Enhancing the hand representation and user interface for better immersion.

## Mockups

Initial and updated designs were created to refine the user interface and improve usability. 

![Mockup Image Placeholder](https://via.placeholder.com/600x300)  
*Example of a puzzle-solving interface.*

## Testing Insights

- Younger users quickly adapted to the game.
- Older users required additional practice but still enjoyed the experience.
- Hand gesture mechanics were well-received across all age groups.

## Contributors

- **Adrian Cristurean Laurentiu**
- **Daniel Pamfil**
- **Carolina Proietti**
- **Tommaso Maldera**
- **Jorge Bernal**

## License

This project is licensed under the [MIT License](LICENSE).
