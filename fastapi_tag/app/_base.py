from fastapi import Request

from base.model import Metadata
from router.routers import Namespace, Resource

app = Namespace(["Generic"])


@app.route("/metadata")
class Information(Resource):
    """
    Information class is a Resource class that is used to show API metadata.
    
    Args:
        request: Request object
    """
    async def get(self, request: Request) -> Metadata:
        """Show API metadata"""
        return request.app.metadata


@app.route("/health")
class Health(Resource):
    """
    health class is a Resource class that is used to show health status.
    
    Args:
        Resource class
    """
    async def get(self):
        """Show health status"""
        return {"status": "ok"}
