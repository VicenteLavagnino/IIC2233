from typing import Tuple, List
import requests
import json

from parametros import GITHUB_BASE_URL, GITHUB_REPO_OWNER, GITHUB_REPO_NAME
from parametros import GITHUB_USERNAME
from parametros import ANIME_BASE_URL, ANIME_NUMERO
from utils.anime import Anime
from collections import namedtuple


def get_animes() -> Tuple[int, List[Anime]]:
    # ToDo: Completar
    status_code = 404
    animes = []

    # url = https://backend.chan.ing.puc.cl/animeranking/v1/AB?id=2
    # formato inspirado en semana 14: Webservices
    url = ANIME_BASE_URL.format("AB?id=" + ANIME_NUMERO)
    response = requests.get(url)
    animes_received = response.json()["animes"]

    status_code = response.status_code

    for anime in animes_received:

        nombre = anime["nombre"]
        ano = anime["season"]["year"]
        etiquetas = anime["tags"]

        nuevo = Anime(nombre, ano, etiquetas)
        animes.append(nuevo)

    """for anime in animes:
        print(anime.nombre)"""

    # print(status_code)

    return status_code, animes


def post_issue(token, animes: List[Anime]) -> Tuple[int, int]:
    # ToDo: Completar
    status_code = 404
    issue_number = -1

    # codigo inspirado en https://docs.github.com/en/rest/issues/issues#create-an-issue
    # url = https://api.github.com/repos/IIC2233/VicenteLavagnino-iic2233-2022-2/issues
    url = GITHUB_BASE_URL.format(GITHUB_REPO_OWNER + "/" + GITHUB_REPO_NAME + "/issues")

    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
    }

    data = {
        "owner": GITHUB_USERNAME,
        "repo": GITHUB_REPO_NAME,
        "title": GITHUB_USERNAME,
        "body": str(animes),
    }

    response = requests.post(url, headers=headers, json=data)

    status_code = response.status_code
    issue_number = response.json()["number"]

    # print("issue_number ", issue_number, " debería ya estar creada")

    return status_code, issue_number


def put_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404

    # codigo inspirado en https://docs.github.com/en/rest/issues/issues#lock-an-issue
    # url = https://api.github.com/repos/IIC2233/VicenteLavagnino-iic2233-2022-2/issues/numero_issue
    url = GITHUB_BASE_URL.format(
        GITHUB_REPO_OWNER + "/" + GITHUB_REPO_NAME + "/issues" + f"/{numero_issue}/lock"
    )

    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "lock_reason": "off-topic",
    }

    response = requests.put(url, headers=headers)
    status_code = response.status_code

    # print("issue_number ", numero_issue, " debería ya estar bloqueada")

    return status_code


def delete_lock_issue(token: str, numero_issue: int) -> int:
    # ToDo: Completar
    status_code = 404

    # codigo inspirado en https://docs.github.com/en/rest/issues/issues#unlock-an-issue
    # url = https://api.github.com/repos/IIC2233/VicenteLavagnino-iic2233-2022-2/issues/numero_issue
    url = GITHUB_BASE_URL.format(
        GITHUB_REPO_OWNER + "/" + GITHUB_REPO_NAME + "/issues" + f"/{numero_issue}/lock"
    )

    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "lock_reason": "off-topic",
    }

    response = requests.delete(url, headers=headers)

    # print("issue_number ", numero_issue, " debería ya estar desbloqueada")

    return status_code


if __name__ == "__main__":
    get_animes()
