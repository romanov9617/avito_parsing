from datetime import datetime
from typing import Annotated
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db_base import Base

pkint = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
created_at = Annotated[datetime, mapped_column(default=datetime.utcnow)]

class PairsORM(Base):
    __tablename__ = "pairs"

    id: Mapped[pkint]
    q: Mapped[str]
    region: Mapped[str]
    created_at: Mapped[created_at]

    counters: Mapped[list['CountsORM']] = relationship("CountsORM", back_populates="pair")


class CountsORM(Base):
    __tablename__ = "counters"

    id: Mapped[pkint]
    quantity: Mapped[int]
    pair_id: Mapped[int] = mapped_column(ForeignKey('pairs.id', ondelete="CASCADE"))
    created_at: Mapped[created_at]

    pair: Mapped['PairsORM'] = relationship("PairsORM", back_populates="counters")

