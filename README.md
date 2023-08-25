# Home Lights Control Backend

Welcome to the Home Lights Control Backend project! This simple Python application utilizes the Flask framework and the phue library to provide a straightforward way to control the lights in your house remotely. With just a few API endpoints, you can command your lights to create the perfect ambiance from the comfort of your smartphone or computer.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [Acknowledgments](#acknowledgments)

## Introduction

Have you ever wanted to adjust the lighting in your house without leaving your seat? Look no further! This project allows you to interact with your Philips Hue lights through a simple Python backend. With Flask serving as the framework and the phue library handling the Hue API communication, you're in full control of setting the mood.

## Features

- **Light Control:** Easily turn lights on/off, adjust brightness, and change colors using intuitive API endpoints.
- **Remote Access:** Control your lights from anywhere by sending HTTP requests to the backend.
- **Simple Setup:** With Flask and phue, the project is lightweight and quick to set up.

## Installation

1. Clone the repository: `git clone https://github.com/your-username/home-lights-control-backend.git`
2. Navigate to the project directory: `cd home-lights-control-backend`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Configure the `config.json` file with your Philips Hue bridge IP address and API key.
2. Run the Flask app: `python app.py`
3. Access the API endpoints to control your lights remotely.


## Technologies

- Flask: A micro web framework for building web applications in Python.
- phue: A Python library to interact with Philips Hue lights through their API.

## Acknowledgments

Huge shoutout to the Flask and phue communities for their fantastic work in creating these tools. Special thanks to Philips Hue for making smart lighting accessible and fun.

Feel free to contribute, open issues, or provide feedback. Let's light up our homes with technology!
