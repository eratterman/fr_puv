"""adding work centers table

Revision ID: 09398d848075
Revises: 15ebf837513f
Create Date: 2021-10-31 12:10:15.403763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09398d848075'
down_revision = '15ebf837513f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('work_centers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('work_center', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_work_centers_work_center'), 'work_centers', ['work_center'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_work_centers_work_center'), table_name='work_centers')
    op.drop_table('work_centers')
    # ### end Alembic commands ###
