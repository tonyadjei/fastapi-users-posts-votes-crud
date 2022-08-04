"""add user table

Revision ID: 28e0cf8edf4a
Revises: a869730917ce
Create Date: 2022-08-03 19:30:25.106306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28e0cf8edf4a'
down_revision = 'a869730917ce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
