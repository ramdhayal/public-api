"""Auto-First

Revision ID: 7f33844b5f3e
Revises: 
Create Date: 2021-12-31 20:44:57.948978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f33844b5f3e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('links',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link_name', sa.String(), nullable=True),
    sa.Column('link', sa.String(), nullable=True),
    sa.Column('link_identity', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('links')
    # ### end Alembic commands ###