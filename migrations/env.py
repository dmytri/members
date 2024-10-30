from alembic import context
from flask import current_app

config = context.config

target_metadata = current_app.extensions['migrate'].db.metadata

def run_migrations_online():
    with current_app.app_context():
        with current_app.extensions['migrate'].db.engine.connect() as connection:
            context.configure(
                connection=connection,
                target_metadata=target_metadata
            )
            with context.begin_transaction():
                context.run_migrations() 