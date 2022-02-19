from fastapi import Request

from fastapi_tag.base.model import Metadata
from fastapi_tag.router.routers import Namespace, Resource

app = Namespace(["Generic"])


@app.route("/metadata")
class Information(Resource):
    """
    Information class is a Resource class that is used to show API metadata.
    """

    async def get(self, request: Request) -> Metadata:
        return request.app.metadata


@app.route("/health")
class Health(Resource):
    """
    health class is a Resource class that is used to show health status.
    """

    async def get(self):
        return {"status": "healthy"}
