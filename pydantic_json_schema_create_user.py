import jsonschema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.fakers import fake


public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=fake.email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()


jsonschema.validate(instance=create_user_response.json(), schema=create_user_response_schema)