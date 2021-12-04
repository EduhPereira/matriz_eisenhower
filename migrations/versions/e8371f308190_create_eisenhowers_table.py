"""create 'eisenhowers' table

Revision ID: e8371f308190
Revises: 8b74d9b16058
Create Date: 2021-11-30 21:38:22.213603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8371f308190'
down_revision = '8b74d9b16058'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eisenhowers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('eisenhowers')
    # ### end Alembic commands ###
