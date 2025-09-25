import allure
from httpx import Response
from clients.api_clients import APIClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from clients.private_httpx_builder import AuthenticationUserSchema, get_private_http_client
from tools.routes import APIRoutes
from clients.api_coverage import tracker


class FilesClient(APIClient):
    @allure.step("Get file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def get_file_api(self, file_id: str) -> Response:
        return self.get(f"{APIRoutes.FILES}/{file_id}")

    @allure.step("Create file")
    @tracker.track_coverage_httpx(APIRoutes.FILES)
    def create_file_api(self, request: CreateFileRequestSchema) -> Response:
        return self.post(
            APIRoutes.FILES,
            data=request.model_dump(by_alias=True, exclude={'upload_file'}),
            files={"upload_file": request.upload_file.read_bytes()}
        )

    @allure.step("Delete file by id {file_id}")
    @tracker.track_coverage_httpx(f"{APIRoutes.FILES}/{{file_id}}")
    def delete_file_api(self, file_id: str) -> Response:
        return self.delete(f"{APIRoutes.FILES}/{file_id}")

    def create_file(self, request: CreateFileRequestSchema) -> CreateFileResponseSchema:
        response = self.create_file_api(request)
        return CreateFileResponseSchema.model_validate_json(response.text)


def get_files_client(user: AuthenticationUserSchema) -> FilesClient:
    return FilesClient(client=get_private_http_client(user))