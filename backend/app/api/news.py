from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import select

from app.db.database import engine
from app.models.news import News
from app.schemas.news import NewsListResponse, NewsDetailResponse


router = APIRouter(prefix="/api/news", tags=["News"])





@router.get("", response_model=list[NewsListResponse])
def get_news(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
    category_id: int | None = Query(default=None, ge=1),
    state_id: int | None = Query(default=None, ge=1),
    city_id: int | None = Query(default=None, ge=1),
    is_breaking: bool | None = Query(default=None),
    is_latest: bool | None = Query(default=None),
    is_viral: bool | None = Query(default=None),
    is_slider: bool | None = Query(default=None),
):
    offset = (page - 1) * limit

    with engine.connect() as connection:
        statement = select(News).where(
            News.is_approved == True
        )

        if category_id is not None:
            statement = statement.where(
                News.cat_id == category_id
            )

        if state_id is not None:
            statement = statement.where(
                News.state_id == state_id
            )

        if city_id is not None:
            statement = statement.where(
                News.city_id == city_id
            )

        if is_breaking is not None:
            statement = statement.where(News.is_breaking == is_breaking)

        if is_latest is not None:
            statement = statement.where(News.is_latest == is_latest)

        if is_viral is not None:
            statement = statement.where(News.is_viral == is_viral)

        if is_slider is not None:
            statement = statement.where(News.is_slider == is_slider)    

        statement = (
            statement
            .order_by(
                News.created_at.desc(),
                News.news_id.desc(),
            )
            .offset(offset)
            .limit(limit)
        )

        result = connection.execute(statement)

        return [
            NewsListResponse(
                id=row.NewsId,
                title=row.CaptionName,
                short_description=row.Short_desc,
                image_url=row.ImageUrl,
                video_url=row.Vidio_URL,
                category_id=row.CatId,
                country_id=row.Country_Id,
                state_id=row.State_Id,
                city_id=row.City_Id,
                tehsil_id=row.Tehsil_Id,
                block_id=row.Block_Id,
                district=row.Distict,
                area=row.Area,
                village=row.Village,
                police_chowki=row.PoliceChowki,
                reporter=row.Reporter,
                posted_from=row.PostedFrom,
                is_home=row.IsHome,
                is_slider=row.isSlider,
                is_breaking=row.isBreaking,
                is_latest=row.isLatest,
                is_viral=row.isViral,
                viewers=row.Viewers,
                created_at=row.CreatedAt,
                published_at=row.PublishedAt,
            )
            for row in result
        ]





@router.get("/{news_id}", response_model=NewsDetailResponse)
def get_news_detail(news_id: int):
    with engine.connect() as connection:
        statement = (
            select(News)
            .where(
                News.news_id == news_id,
                News.is_approved == True,
            )
            
        )

        row = connection.execute(statement).first()

        if row is None:
            raise HTTPException(
                status_code=404,
                detail="News not found",
            )

        return NewsDetailResponse(
            id=row.NewsId,
            title=row.CaptionName,
            short_description=row.Short_desc,
            content=row.Details,
            image_url=row.ImageUrl,
            video_url=row.Vidio_URL,
            category_id=row.CatId,
            country_id=row.Country_Id,
            state_id=row.State_Id,
            city_id=row.City_Id,
            tehsil_id=row.Tehsil_Id,
            block_id=row.Block_Id,
            district=row.Distict,
            area=row.Area,
            village=row.Village,
            police_chowki=row.PoliceChowki,
            reporter=row.Reporter,
            posted_from=row.PostedFrom,
            is_home=row.IsHome,
            is_slider=row.isSlider,
            is_breaking=row.isBreaking,
            is_latest=row.isLatest,
            is_viral=row.isViral,
            viewers=row.Viewers,
            created_at=row.CreatedAt,
            published_at=row.PublishedAt,
        )



@router.get("/{news_id}/related", response_model=list[NewsListResponse])
def get_related_news(news_id: int, limit: int = 5):
    limit = min(max(limit, 1), 10)

    with engine.connect() as connection:
        category_id = connection.execute(
            select(News.cat_id).where(
                News.news_id == news_id,
                News.is_approved == True,
            )
        ).scalar_one_or_none()

        if category_id is None:
            raise HTTPException(
                status_code=404,
                detail="Approved news not found",
            )

        columns = [
            News.news_id.label("news_id"),
            News.caption_name.label("caption_name"),
            News.short_desc.label("short_desc"),
            News.image_url.label("image_url"),
            News.video_url.label("video_url"),
            News.cat_id.label("cat_id"),
            News.country_id.label("country_id"),
            News.state_id.label("state_id"),
            News.city_id.label("city_id"),
            News.tehsil_id.label("tehsil_id"),
            News.block_id.label("block_id"),
            News.district.label("district"),
            News.area.label("area"),
            News.village.label("village"),
            News.police_chowki.label("police_chowki"),
            News.reporter.label("reporter"),
            News.posted_from.label("posted_from"),
            News.is_home.label("is_home"),
            News.is_slider.label("is_slider"),
            News.is_breaking.label("is_breaking"),
            News.is_latest.label("is_latest"),
            News.is_viral.label("is_viral"),
            News.viewers.label("viewers"),
            News.created_at.label("created_at"),
            News.published_at.label("published_at"),
        ]

        statement = (
            select(*columns)
            .where(
                News.news_id != news_id,
                News.is_approved == True,
                News.cat_id == category_id,
            )
            .order_by(News.created_at.desc())
            .limit(limit)
        )

        rows = connection.execute(statement).mappings().all()

        return [
            NewsListResponse(
                id=row["news_id"],
                title=row["caption_name"],
                short_description=row["short_desc"],
                image_url=row["image_url"],
                video_url=row["video_url"],
                category_id=row["cat_id"],
                country_id=row["country_id"],
                state_id=row["state_id"],
                city_id=row["city_id"],
                tehsil_id=row["tehsil_id"],
                block_id=row["block_id"],
                district=row["district"],
                area=row["area"],
                village=row["village"],
                police_chowki=row["police_chowki"],
                reporter=row["reporter"],
                posted_from=row["posted_from"],
                is_home=row["is_home"],
                is_slider=row["is_slider"],
                is_breaking=row["is_breaking"],
                is_latest=row["is_latest"],
                is_viral=row["is_viral"],
                viewers=row["viewers"],
                created_at=row["created_at"],
                published_at=row["published_at"],
            )
            for row in rows
        ]
