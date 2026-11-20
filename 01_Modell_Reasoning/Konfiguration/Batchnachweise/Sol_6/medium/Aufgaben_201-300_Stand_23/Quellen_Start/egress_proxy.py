"""Host-owned logging wrapper around the unchanged AgentCompass egress proxy."""
import asyncio
import importlib.util
import json
import sys
from datetime import datetime, timezone

spec = importlib.util.spec_from_file_location("upstream_proxy", "/opt/upstream_proxy.py")
proxy = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = proxy
spec.loader.exec_module(proxy)
original_open = proxy._open_permitted_target


async def logged_open(policy, host, port):
    result = await original_open(policy, host, port)
    print(json.dumps({"at": datetime.now(timezone.utc).isoformat(), "host": host,
                      "port": port, "connected": result is not None}), flush=True)
    return result


proxy._open_permitted_target = logged_open
asyncio.run(proxy.serve())
