from sqlalchemy import Boolean, DateTime, Integer, NVARCHAR, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class News(Base):
    __tablename__ = "tblNews"
    __table_args__ = {"schema": "dbo"}

    news_id: Mapped[int] = mapped_column("NewsId", Integer, primary_key=True)

    image_url: Mapped[str | None] = mapped_column("ImageUrl", NVARCHAR(50))
    rank: Mapped[int | None] = mapped_column("Rank", Integer)
    created_by: Mapped[int | None] = mapped_column("CreatedBy", Integer)
    created_at: Mapped[DateTime | None] = mapped_column("CreatedAt", DateTime)
    activated_from: Mapped[DateTime | None] = mapped_column("ActivatedFrom", DateTime)

    redirect_url: Mapped[str | None] = mapped_column(
        "RedirectUrl", NVARCHAR(150)
    )

    is_active: Mapped[bool | None] = mapped_column("IsActive", Boolean)

    caption_name: Mapped[str | None] = mapped_column(
        "CaptionName", NVARCHAR(145)
    )

    cat_id: Mapped[int | None] = mapped_column("CatId", Integer)

    rank_home: Mapped[int | None] = mapped_column("Rank_Home", Integer)
    is_home: Mapped[bool | None] = mapped_column("IsHome", Boolean)

    details: Mapped[str | None] = mapped_column("Details", Text)

    video_url: Mapped[str | None] = mapped_column(
        "Vidio_URL", NVARCHAR(200)
    )

    short_desc: Mapped[str | None] = mapped_column(
        "Short_desc", NVARCHAR(250)
    )

    country_id: Mapped[int | None] = mapped_column("Country_Id", Integer)
    state_id: Mapped[int | None] = mapped_column("State_Id", Integer)
    city_id: Mapped[int | None] = mapped_column("City_Id", Integer)

    police_chowki: Mapped[str | None] = mapped_column(
        "PoliceChowki", NVARCHAR(100)
    )

    area: Mapped[str | None] = mapped_column("Area", NVARCHAR(100))
    village: Mapped[str | None] = mapped_column("Village", NVARCHAR(100))

    approved_by: Mapped[int | None] = mapped_column("ApprovedBy", Integer)
    approved_at: Mapped[DateTime | None] = mapped_column("ApprovedAt", DateTime)

    is_approved: Mapped[bool | None] = mapped_column(
        "isapproved", Boolean
    )

    member_id: Mapped[int | None] = mapped_column("Member_Id", Integer)

    posted_from: Mapped[str | None] = mapped_column(
        "PostedFrom", NVARCHAR(10)
    )

    reporter: Mapped[str | None] = mapped_column(
        "Reporter", NVARCHAR(100)
    )

    district: Mapped[str | None] = mapped_column(
        "Distict", NVARCHAR(100)
    )

    is_slider: Mapped[bool | None] = mapped_column(
        "isSlider", Boolean
    )

    is_breaking: Mapped[bool | None] = mapped_column(
        "isBreaking", Boolean
    )

    is_latest: Mapped[bool | None] = mapped_column(
        "isLatest", Boolean
    )

    is_viral: Mapped[bool | None] = mapped_column(
        "isViral", Boolean
    )

    tehsil_id: Mapped[int | None] = mapped_column(
        "Tehsil_Id", Integer
    )

    block_id: Mapped[int | None] = mapped_column(
        "Block_Id", Integer
    )

    viewers: Mapped[int | None] = mapped_column(
        "Viewers", Integer
    )

    view_on: Mapped[DateTime | None] = mapped_column(
        "View_On", DateTime
    )

    publish_by_member_id: Mapped[int | None] = mapped_column(
        "PublishBy_MemberId", Integer
    )

    published_at: Mapped[DateTime | None] = mapped_column(
        "PublishedAt", DateTime
    )