"""update category (add is_deleted fields)

Revision ID: 8c7a7a1e6a5c
Revises: 12fc31a87805
Create Date: 2023-11-25 12:07:47.620126

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c7a7a1e6a5c'
down_revision: Union[str, None] = '12fc31a87805'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('is_deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'is_deleted')
    # ### end Alembic commands ###