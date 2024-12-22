"""Create tables for User, MutualFund, Portfolio, and Investment models

Revision ID: your_revision_id
Revises: your_previous_revision_id
Create Date: YYYY-MM-DD HH:MM:SS

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# Revision identifiers, used by Alembic.
revision = 'your_revision_id'
down_revision = 'your_previous_revision_id'
branch_labels = None
depends_on = None


def upgrade():
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String, unique=True, index=True, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )

    # Create mutual_fund table
    op.create_table(
        'mutual_fund',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('scheme_code', sa.String, unique=True, index=True, nullable=False),
        sa.Column('scheme_name', sa.String, nullable=False),
        sa.Column('fund_family', sa.String, index=True),
        sa.Column('nav', sa.Float),
        sa.Column('scheme_type', sa.String),
        sa.Column('scheme_category', sa.String),
        sa.Column('date', sa.DateTime)
    )

    # Create portfolio table
    op.create_table(
        'portfolio',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('total_value', sa.Float),
        sa.Column('investments_summary', postgresql.JSON, server_default=sa.text("'{}'::json"))
    )

    # Create investment table
    op.create_table(
        'investment',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('portfolio_id', sa.Integer, sa.ForeignKey('portfolio.id'), nullable=False),
        sa.Column('mutual_fund_id', sa.Integer, sa.ForeignKey('mutual_fund.id'), nullable=False),
        sa.Column('mutual_fund_name', sa.String, nullable=False),
        sa.Column('units', sa.Float),
        sa.Column('purchase_price', sa.Float)
    )


def downgrade():
    # Drop tables in reverse order of creation
    op.drop_table('investment')
    op.drop_table('portfolio')
    op.drop_table('mutual_fund')
    op.drop_table('users')