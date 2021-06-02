class VideoEmbeddingApiOptions(object):
    def __init__(self,
                 url: str):
        self.url = url


class SecurityOptions(object):
    def __init__(self, secret_key, algorithm, access_token_expire_minutes):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.access_token_expire_minutes = access_token_expire_minutes


class AppOptions(object):
    def __init__(self):

        self.project_name = "exerciser-backend"
        self.video_embedding_api_options = VideoEmbeddingApiOptions(url="http://165.22.67.71:5005")
        self.security_options = SecurityOptions(secret_key="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
                                                algorithm="HS256",
                                                access_token_expire_minutes=30)


APP_OPTIONS = AppOptions()