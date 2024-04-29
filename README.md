# AntiScrape-FastAPI-Defender

Welcome to AntiScrape-FastAPI-Defender, a secure FastAPI-based authentication service with robust defense mechanisms against web scraping and malicious activities. This project aims to provide developers with a framework to build authentication services that are resilient to common threats such as abusive requests, spam submissions, and malicious user agents.

## Features

- **Rate Limiting**: Protects against abuse by limiting the number of requests per IP address.
- **Behavioral Analysis**: Detects and blocks suspicious user agents, such as headless browsers and bots.
- **Honeypot Detection**: Identifies and blocks form submissions from honeypot fields to deter automated attacks.
- **IP Health Check**: Verifies the health of incoming IP addresses to block toxic, proxy, or spam traffic.
- **Logging**: Records suspicious activities for further analysis and monitoring.

## Getting Started

To get started with AntiScrape-FastAPI-Defender, follow these steps:

1. **Clone the Repository**: 
    ```sh
    git clone https://github.com/geoseiden/AntiScrape-FastAPI-Defender.git
    ```

2. **Install Dependencies**: 
    ```sh
    cd AntiScrape-FastAPI-Defender
    pip install -r requirements.txt
    ```

3. **Run the Server**: 
    ```sh
    python server.py
    ```

4. **Interact with the API**: 
    - Use `client.py` to trigger different scenarios for testing.
    - Explore the API endpoints (`/login`) and observe the implemented security measures in action.

## Configuration

- Adjust rate limits, honeypot field names, and other settings in `server.py` to suit your requirements.
- Obtain an API key from [Antideo](https://www.antideo.com/) for IP health checks and replace the placeholder in the `check_ip_health` function with your API key.
- Optionally, integrate with other third-party IP health check services by modifying the `check_ip_health` function.

## Contributing

Contributions to AntiScrape-FastAPI-Defender are welcome! Here are some ways you can contribute:
- Report bugs or suggest features by opening an issue.
- Submit pull requests for bug fixes, improvements, or new features.
- Share your feedback and ideas to help enhance the project.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/): The high-performance web framework used for building the API.
- [user-agents](https://pypi.org/project/user-agents/): Python library for parsing user agent strings.
- [aiohttp](https://docs.aiohttp.org/en/stable/): Asynchronous HTTP client/server framework for Python.
- [Antideo](https://www.antideo.com/): External service used for IP health checks.
