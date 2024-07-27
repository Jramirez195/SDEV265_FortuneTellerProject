# Fortune Teller Project

## Overview
The Fortune Teller Project is a simple tarot card reading application built using Python and the Tkinter library. The application randomly draws three tarot cards representing the past, present, and future, providing interpretations for each card based on its orientation (upright or reversed).

## Features
- **Draw Cards**: Randomly selects three tarot cards from the major arcana and displays their interpretations.
- **User Interface**: Intuitive and visually appealing interface using Tkinter with a color scheme inspired by mystical themes.
- **Card Meanings**: Provides detailed interpretations for both upright and reversed orientations of each card.

## Major Arcana Cards
The project includes the following major arcana cards with their respective meanings:

- The Fool
- The Magician
- The High Priestess
- The Empress
- The Emperor
- The Hierophant
- The Lovers
- The Chariot
- Strength
- The Hermit
- Wheel of Fortune
- Justice
- Judgement
- The Hanged Man
- Death
- Temperance
- The Devil
- The Tower
- The Star
- The Moon
- The Sun
- The World

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jramirez195/fortune-teller-project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd fortune-teller-project
    ```
3. Install the required dependencies (Tkinter should be included with Python, but ensure it is available):
    ```bash
    pip install tk
    ```

## Usage

1. Run the application:
    ```bash
    python fortune_teller.py
    ```
2. Click on the "Draw Cards" button to draw three random tarot cards and view their interpretations.

## Project Structure

- `fortune_teller.py`: The main Python script containing the implementation of the tarot card reading application.
- `README.md`: Project documentation.

## How it Works

The application initializes a Tkinter window with a button to draw cards. When the button is clicked, three cards are randomly selected from the major arcana deck. Each card is displayed with its name, orientation (upright or reversed), and its interpretation. The interpretations are predefined in a dictionary and include meanings for both upright and reversed orientations.

## Acknowledgements

This project uses the Tkinter library for the graphical user interface and random module for drawing cards. 

## License

This project is licensed under the MIT License - see the [LICENSE](License.md) file for details.

---

Feel free to explore the project and customize the card meanings or add more features to enhance the fortune teller experience!
