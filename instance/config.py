import os


class Config:
    """ Parent configuration class"""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    """Configurations for development"""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for testing, with a separate test database"""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost:5433/test_db"
    DEBUG = True


class StagingConfig(Config):
    """Configurations for staging"""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for production"""

    DEBUG = False
    TESTING = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
