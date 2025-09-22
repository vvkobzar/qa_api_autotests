from pydantic import BaseModel, ConfigDict, Field
from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema
from tools.fakers import fake


class CourseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class GetCoursesResponseSchema(BaseModel):
    courses: list[CourseSchema]


class CreateCourseRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.mix_score)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)
    preview_file_id: str = Field(alias="previewFileId", default_factory=fake.uuid4)
    created_by_user_id: str = Field(alias="createdByUserId", default_factory=fake.uuid4)


class CreateCourseResponseSchema(BaseModel):
    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.mix_score)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateCourseResponseSchema(BaseModel):
    course: CourseSchema
