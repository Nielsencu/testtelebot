# Python Telegram Bot

## Setting up Python Telegram Bot

### System Requirements

1. Python (>= 3.6.5)
1. Pip (>= 18.0)
1. MariaDB (>= 10.3.9)
1. virtualenv (== 16.0.0) (if setting up project in virtual environment)

### Getting Started

 1. Install Python Dependencies

    ```
    $ pip install -r requirements.txt
    ```

 1. Setup database
    ```
    $ python setup.py
    ```

 1. Run the bot
    ```
    $ python main.py
    ```

### Setting up in Virtual Environment

 1. Setup Virtual Environment
    ```
    $ python -m venv virtualenv
    ```

 1. Activate Virtual Environment
    ```
    $ source virtualenv/bin/activate
    ```

 1. Update pip to latest version
    ```
    $ python -m pip install --upgrade pip
    ```

 4. Repeat the above steps to set up the project in the virtual environment
    Run the following code to deactivate the virtual environment
    ```
    $ deactivate
    ```