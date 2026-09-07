from enum import StrEnum
from pathlib import Path
from typing import Self

from pydantic import BaseModel, DirectoryPath, EmailStr, FilePath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Browser(StrEnum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_nested_delimiter="__")
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: Path
    tracing_dir: Path
    browser_state_file: Path

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("./browser_state.json")

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return cls(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file,
        )


settings = Settings.initialize()
