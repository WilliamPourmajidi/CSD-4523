from data_processor import fetch_data, process_data


def main():
    api_key = "your_api_key_here"
    cities = ["London", "New York", "Tokyo", "Delhi"]

    # Fetch data
    fetch_data.fetch_weather_data(api_key, cities)

    # Process data
    processed_data = process_data.process_weather_data()

    # Print data
    for city, info in processed_data.items():
        if isinstance(info, dict):
            print(
                f"{city}:\n  Temperature: {info['temperature']}°C\n"
                f"  Humidity: {info['humidity']}%\n  Description: {info['description']}\n")
        else:
            print(f"{city}:\n  Error: {info}\n")


if __name__ == "__main__":
    main()

