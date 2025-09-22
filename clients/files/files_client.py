from httpx import Response
from clients.api_clients import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_httpx_builder import AuthenticationUserSchema, get_private_http_client


class FilesClient(APIClient):

    def get_file_api(self, file_id: str) -> Response:
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        return self.post(
            "/api/v1/files",
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": open(request.upload_file, 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    return FilesClient(client=get_private_http_client(user))