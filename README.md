# System Health Dashboard

This repository houses a Flask-based web application designed to monitor and display the health status of various systems. It includes a set of Python scripts for checking system health, HTML templates for displaying the status, JavaScript for interactive elements, and a CSS file for styling.

## Features

- **System Health Checks**: Automated checks to determine the operational status of predefined systems.
- **Interactive Dashboard**: A web-based dashboard to view the current health status of all monitored systems.
- **Historical Data View**: Access to historical check data for each system, allowing for trend analysis and troubleshooting.
- **Customizable Check Intervals**: Ability to set the frequency of health checks as per requirement.

## Setup

1. **Dependencies**: Ensure you have Flask and other required packages installed.

    ```bash
    pip install Flask
    ```

2. **Configuration**: Modify the `systems.json` file to include the systems you wish to monitor. Set the `url` for each system, and the script will automatically handle the health checks.

    ```json
    [
        {
            "name": "System Name",
            "url": "http://example.com"
        }
    ]
    ```

3. **Running the Application**: Execute the `run.py` script to start the Flask server:

    ```bash
    python run.py
    ```

    The dashboard will be accessible at `http://localhost:5000` or the configured port.

## Usage

- Visit the main dashboard page to see the overall health status of all systems.
- Click on a system name to view detailed historical data regarding its health checks.
- The dashboard updates automatically with each new check, providing real-time insights.

## Customization

- **Checkers**: Modify `checkers.py` to change the logic used for determining system health.
- **Frontend**: Adjust `dashboard.html` and `all_checks.html` to alter the dashboard's layout or to add new features.
- **Styling**: Update `styles.css` to customize the appearance of the dashboard according to your preferences.

## Disclaimer

This tool is intended for internal use and should be configured responsibly. The author is not responsible for any misuse or for any damages resulting from improper configuration or deployment.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
