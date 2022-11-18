import os.path

TOKENS_FILE_PATH = os.path.join("data", "tokens.csv")
ISSUES_FILE_PATH = os.path.join("data", "issues.csv")

ANIME_BASE_URL = "https://backend.chan.ing.puc.cl/animeranking/v1/{}"

# NUMERO_ALUMNO = "21638322"
# NUMERO_ALUMNO[5:6] = 32 --> % 6 = 2

ANIME_NUMERO = str(2)  # Completar

REGEX_FILTRO = r"((ha)(\w)+o)|((a.*){3,})"  # Completar

GITHUB_BASE_URL = "https://api.github.com/repos/{}"
GITHUB_REPO_OWNER = "IIC2233"
GITHUB_REPO_NAME = "VicenteLavagnino-iic2233-2022-2"  # Completar
GITHUB_USERNAME = "VicenteLavagnino"  # Completar
