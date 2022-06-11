from sqlalchemy import create_engine, MetaData
from db import wallets, courses, tasks, students, students_courses, students_tasks
from settings import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

ADMIN_DB_URL = DSN.format(
    user=DB_USER, password=DB_PASSWORD, database=DB_NAME,
    host=DB_HOST, port=DB_PORT
)

admin_engine = create_engine(ADMIN_DB_URL)


def create_tables(engine=admin_engine):
    meta = MetaData(bind=engine)
    meta.create_all(bind=engine, tables=[wallets, courses, tasks, students, students_courses, students_tasks], checkfirst=True)


if __name__ == '__main__':
    create_tables(admin_engine)
