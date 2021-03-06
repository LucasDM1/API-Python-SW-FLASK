"""empty message

Revision ID: 2e924226c2ec
Revises: 7ad41ae311a5
Create Date: 2021-04-08 03:26:21.835819

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2e924226c2ec'
down_revision = '7ad41ae311a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('eyeColor', sa.String(length=250), nullable=False))
    op.add_column('character', sa.Column('hairColor', sa.String(length=250), nullable=False))
    op.drop_column('character', 'eye_color')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('character', sa.Column('eye_color', mysql.VARCHAR(length=250), nullable=False))
    op.drop_column('character', 'hairColor')
    op.drop_column('character', 'eyeColor')
    # ### end Alembic commands ###
