"""add tables

Revision ID: f1c3fb7956c0
Revises: 
Create Date: 2023-04-21 22:01:48.614313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1c3fb7956c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.String(length=50), nullable=True),
    sa.Column('current_price', sa.Float(), nullable=True),
    sa.Column('last_low', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    # ### end Alembic commands ###
