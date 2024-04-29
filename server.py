from fastapi import FastAPI, Request, HTTPException, status
from user_agents import parse
from pydantic import BaseModel
from ipaddress import ip_address
import aiohttp
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Honeypot field
honeypot_field = "email"  # Change this to your desired honeypot field name

# Define a dictionary to store request counts per IP
request_counts = {}

class LoginRequest(BaseModel):
    user_agent: str
    email: str  # Honeypot field

def behavioral_analysis(user_agent_string):
    # Parse the user agent string
    user_agent = parse(user_agent_string)

    # Implement risk assessment criteria based on user agent properties
    is_suspicious = (
            user_agent.browser.family in ['HeadlessChrome', 'PhantomJS'] or
            user_agent.device.family in ['Spider', 'Bot'] or
            (hasattr(user_agent, 'language') and user_agent.language == 'xx-XX')
    )
    return is_suspicious

async def check_ip_health(ip: str) -> dict:
    url = f"https://api.antideo.com/ip/health/{ip}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise HTTPException(status_code=response.status, detail="Failed to check IP health")

def block_ip(response: dict):
    if response["health"]["toxic"] or response["health"]["proxy"] or response["health"]["spam"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="IP is toxic, a proxy, or spam")

# Middleware for rate limiting
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    ip = ip_address(request.client.host)

    # Increase the request count for this IP
    request_counts[ip] = request_counts.get(ip, 0) + 1

    # If the request count exceeds the limit, return 429 Too Many Requests
    if request_counts.get(ip, 0) > 5:  # Adjust the limit as needed
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many requests from this IP")

    response = await call_next(request)
    return response

# Login route
@app.post('/login')
async def login(request: Request, login_request: LoginRequest):
    # Perform behavioral analysis
    if behavioral_analysis(login_request.user_agent):
        logger.warning('Suspicious user agent detected: {}'.format(login_request.user_agent))
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Suspicious user agent detected.")

    # Check honeypot field
    if login_request.email != "":
        logger.warning('Honeypot field triggered: {}'.format(honeypot_field))
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Honeypot field triggered.")

    # Check IP health
    ip = ip_address(request.client.host)
    ip_health = await check_ip_health(str(ip))
    block_ip(ip_health)

    # For demonstration purposes, always return 200 OK for non-suspicious user agents
    return {'message': 'Login successful.'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
