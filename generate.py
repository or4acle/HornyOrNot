import json

def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    horny = config.get("horny", False)

    if horny:
        text = "HORNY"
        color = "#FF0000"
    else:
        text = "NO"
        color = "#FFFFFF"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="30">
  <rect width="200" height="30" fill="#24292E"/>
  <text x="100" y="20" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="{color}">AM I HORNY? {text}</text>
</svg>'''

    with open("badge.svg", "w") as f:
        f.write(svg)

    print(f"Generated badge: horny={horny}")

if __name__ == "__main__":
    main()