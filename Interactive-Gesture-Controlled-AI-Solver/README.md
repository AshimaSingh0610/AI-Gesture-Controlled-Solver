# Interactive-Gesture-Controlled-AI-Solver

## Overview

The **Interactive-Gesture-Controlled-AI-Solver** is a project designed to build an AI system capable of recognizing and responding to gestures. This project integrates machine learning, computer vision, and gesture recognition technologies to create an interactive application.

## Project Structure

Here's a detailed overview of the project directory structure:

```
Interactive-Gesture-Controlled-AI-Solver/
│
├── src/
│   ├── model.py               # Defines the architecture of the AI model.
│   ├── training.py            # Handles the training process of the model.
│   ├── inference.py           # Manages inference and predictions.
│   └── gesture_control/       # Contains modules for gesture control.
│       ├── detector.py        # Gesture detection logic.
│       ├── processor.py       # Processes gestures into actionable data.
│       └── actions.py         # Defines actions based on gestures.
│
├── data/
│   ├── raw/                   # Directory for raw data files.
│   └── processed/             # Directory for processed data files.
│
├── models/
│   └── model.h5               # Trained model file.
│
├── notebooks/
│   └── experiments.ipynb      # Jupyter notebook for experiments and analysis.
│
├── utils/
│   └── helper.py             # Helper functions used across the project.
│
├── config/
│   └── config.yaml           # Configuration file in YAML format.
│
├── tests/
│   └── test_model.py         # Unit tests for the model components.
│
├── .gitignore                 # Git ignore file to exclude specific files and directories.
├── README.md                  # This README file.
└── requirements.txt           # List of Python packages required for the project.
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Amartya-007/Interactive-Gesture-Controlled-AI-Solver.git
   cd Interactive-Gesture-Controlled-AI-Solver
   ```

2. **Create and Activate Conda Environment**

   ```bash
   conda create --name gesture-ai python=3.8
   conda activate gesture-ai
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run Training**

   To start training the model, execute:

   ```bash
   python src/training.py
   ```

2. **Run Inference**

   To perform inference with the trained model:

   ```bash
   python src/inference.py
   ```

3. **Run Gesture Control**

   To run the gesture control system:

   ```bash
   python src/gesture_control/detector.py
   ```

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
