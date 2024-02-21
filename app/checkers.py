from bs4 import BeautifulSoup
import requests


def check_system_health(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        element = soup.find('img', {'alt': 'xConnector', 'src': '/images/logo.png'})

        if element:
            return "green"
        else:
            return "red"
    except requests.RequestException:
        return "yellow"


def periodic_check():
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
        system['checks'] = system['checks'][:5]  # Limit to the last 5 checks

    with open('app/data/systems.json', 'w') as f:
        json.dump(systems, f, indent=4)
