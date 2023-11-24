"""Add balance

Revision ID: 35863dadd9df
Revises: a74fa97042f4
Create Date: 2023-11-23 18:39:15.984397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35863dadd9df'
down_revision: Union[str, None] = 'a74fa97042f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=16), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('currency', sa.String(), nullable=False),
    sa.Column('created_date_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_date_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('balances')
    # ### end Alembic commands ###
