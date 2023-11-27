"""add cascade delete on balance

Revision ID: 2ed936a9dba7
Revises: da6465054fb0
Create Date: 2023-11-25 11:51:38.034941

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ed936a9dba7'
down_revision: Union[str, None] = 'da6465054fb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('transactions_balance_id_fkey', 'transactions', type_='foreignkey')
    op.create_foreign_key(None, 'transactions', 'balances', ['balance_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transactions', type_='foreignkey')
    op.create_foreign_key('transactions_balance_id_fkey', 'transactions', 'balances', ['balance_id'], ['id'])
    # ### end Alembic commands ###
