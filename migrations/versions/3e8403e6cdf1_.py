"""empty message

Revision ID: 3e8403e6cdf1
Revises: f3488b67bc7
Create Date: 2015-05-01 02:02:57.788552

"""

# revision identifiers, used by Alembic.
revision = '3e8403e6cdf1'
down_revision = 'f3488b67bc7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stream', sa.Column('need_to_notify_subscribers', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stream', 'need_to_notify_subscribers')
    ### end Alembic commands ###
