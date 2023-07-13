import pynecone as pc

class FrontendConfig(pc.Config):
    pass

config = FrontendConfig(
    app_name="front_end",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)