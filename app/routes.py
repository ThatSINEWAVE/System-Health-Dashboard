from flask import render_template, redirect, url_for
from . import app
from .checkers import check_system_health
import json


@app.route('/')
def index():
    with open('app/data/systems.json', 'r') as f:
        systems = json.load(f)
    return render_template('dashboard.html', systems=systems)


@app.route('/all_checks/<system_name>')
def all_checks(system_name):
    # Load systems from JSON file
    with open('app/data/systems.json', 'r') as f:
        systems = json.load(f)

    # Find the system by name
    system = next((s for s in systems if s['name'] == system_name), None)

    # If system is not found, redirect to main page or show an error
    if not system:
        return redirect(url_for('index'))  # or render an error template

    # Extract all checks for the system
    checks = system['checks']

    # Render a template to display the checks
    return render_template('all_checks.html', system_name=system_name, checks=checks)


@app.route('/check_all_systems')
def check_all_systems():
    with open('app/data/systems.json', 'r') as f:
        systems = json.load(f)

    for system in systems:
        current_status = check_system_health(system['url'])
        system['status'] = current_status

        # Store the result of the check with a timestamp
        from datetime import datetime
        check = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "status": current_status
        }
        system['checks'].insert(0, check)

        # Limit to only the last 5 checks for the main view
        system['checks'] = system['checks'][:5]

    with open('app/data/systems.json', 'w') as f:
        json.dump(systems, f, indent=4)

    return redirect(url_for('index'))
