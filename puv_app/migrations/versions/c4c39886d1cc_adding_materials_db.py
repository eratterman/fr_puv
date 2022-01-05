"""adding materials db

Revision ID: c4c39886d1cc
Revises: 09398d848075
Create Date: 2021-10-31 12:50:13.486026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4c39886d1cc'
down_revision = '09398d848075'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=600), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('turn_around_days', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_materials_item'), 'materials', ['item'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_materials_item'), table_name='materials')
    op.drop_table('materials')
    # ### end Alembic commands ###
