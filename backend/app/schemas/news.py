from datetime import datetime

from pydantic import BaseModel, ConfigDict

class NewsListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    short_description: str | None

    image_url: str | None
    video_url: str | None

    category_id: int | None
    country_id: int | None
    state_id: int | None
    city_id: int | None
    tehsil_id: int | None
    block_id: int | None

    district: str | None
    area: str | None
    village: str | None
    police_chowki: str | None

    reporter: str | None
    posted_from: str | None

    is_home: bool | None
    is_slider: bool | None
    is_breaking: bool | None
    is_latest: bool | None
    is_viral: bool | None

    viewers: int | None
    created_at: datetime | None
    published_at: datetime | None

class NewsDetailResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    short_description: str | None
    content: str | None

    image_url: str | None
    video_url: str | None

    category_id: int | None
    country_id: int | None
    state_id: int | None
    city_id: int | None
    tehsil_id: int | None
    block_id: int | None

    district: str | None
    area: str | None
    village: str | None
    police_chowki: str | None

    reporter: str | None
    posted_from: str | None

    is_home: bool | None
    is_slider: bool | None
    is_breaking: bool | None
    is_latest: bool | None
    is_viral: bool | None

    viewers: int | None
    created_at: datetime | None
    published_at: datetime | None    