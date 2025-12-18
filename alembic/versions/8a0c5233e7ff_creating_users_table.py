"""Creating users table

Revision ID: 8a0c5233e7ff
Revises: 4058ad7af340
Create Date: 2025-12-18 20:23:45.923118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a0c5233e7ff'
down_revision: Union[str, Sequence[str], None] = '4058ad7af340'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('email',sa.String(),nullable=False,unique=True),
                    sa.Column('password',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
