"""add transaction

Revision ID: 07543256a957
Revises: 773087ca12e0
Create Date: 2023-11-25 09:11:12.777923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07543256a957'
down_revision: Union[str, None] = '773087ca12e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=60), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('created_date_time', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('balance_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['balance_id'], ['balances.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###