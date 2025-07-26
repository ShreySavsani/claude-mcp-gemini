from fastapi import FastAPI
from config import config, ConfigurationError
import sys
import logging

logging.basicConfig(level=getattr(logging, config.log_level))
logger = logging.getLogger(__name__)

try:
    logger.info("Initializing MCP Server with Google Generative AI")
    logger.info(f"Google API Key configured: {bool(config.google_api_key)}")
except ConfigurationError as e:
    logger.error(f"Configuration error: {e}")
    sys.exit(1)

app = FastAPI(title="MCP Server", description="FastAPI MCP Server with Google Generative AI", version="1.0.0")

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Server is running successfully"}

@app.get("/config")
async def config_status():
    return {
        "google_api_configured": bool(config.google_api_key),
        "host": config.app_host,
        "port": config.app_port,
        "debug": config.app_debug,
        "log_level": config.log_level
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.app_host, port=config.app_port, debug=config.app_debug)