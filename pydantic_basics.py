"""""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "estimatedTime": "string",
    }
}
"""""

from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from pydantic.alias_generators import to_camel


class FileSchema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    description: str
    estimated_time: str = Field(alias='estimatedTime')


course_default_model = CourseSchema(
    id='course-id',
    title='Playwright',
    maxScore=100,
    minScore=10,
    description='Playwright',
    estimatedTime="1 week"
)

print("Course default model:", course_default_model)

course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}

course_dict_model = CourseSchema(**course_dict)
print("Course dict:", course_dict_model)



course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print("Course JSON model:", course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))