import json
from jsonpath_ng import parse

import pytest
import requests


@pytest.fixture(scope="function")
def auth():
    url = 'https://auth.tusvc.bcs.ru/auth/realms/perseus/protocol/openid-connect/token'
    data = {
        'grant_type': 'password',
        'username': 'usr-ef-001',
        'password': 'DBSHeF1A9m',
        'client_id': 'ef-front',
        'client_secret': 'client_secret'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    # Выполняем POST-запрос для получения токена
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()  # Проверка успешности запроса
    access_token = response.json().get('access_token')
    headers_auth = {
        'Authorization': f'Bearer {access_token}'
    }
    return headers_auth

@pytest.mark.parametrize("idProposal", ["4c7f371a-ea20-4dc6-ab82-35254611570b",
                                        "4922a1de-9e9f-4255-acae-74b746467132"])
def test_bff_proposal_cache(auth, idProposal):
    response = requests.get(
        f"https://ef-pfp-test4.tusvc.bcs.ru/ef-pfp-bff-proposal/api/v1/cache/proposals/{idProposal}",
        headers=auth)
    assert response.status_code == 200
    print(response.json())

    jsonProposal = response.json()
    assert jsonProposal["isNoteEditable"] == True
    assert "Персональное финансовое" in jsonProposal["name"]
    # assert jsonProposal["portfolioTools"]["investmentTools"][0]["id"] == "NTQzO0lOVkVTVE1FTlQ="


@pytest.mark.parametrize("proposalsId, code", [("4c7f371a-ea20-4dc6-ab82-35254611570b","227"),("4922a1de-9e9f-4255-acae-74b746467132", "6")])
def test_ppoposalsCache(auth, proposalsId, code):
    response = requests.get(f"https://ef-pfp-test4.tusvc.bcs.ru/ef-pfp-bff-proposal/api/v1/cache/proposals/{proposalsId}", headers=auth)
    assert response.status_code == 200
    response.raise_for_status()
    print(response.json())

    jsonProposal = response.json()
    assert jsonProposal["isDescriptionEditable"] == True, f'Параметр isDescriptionEditable не равен True'
    assert "Персональное финансовое" in jsonProposal["name"]

    second_product = jsonProposal["portfolioTools"]["liquidTools"][1]
    print(second_product)
    assert second_product["code"] == code

    # assert jsonProposal["description"] == "", "Поле description не пустое"
    # assert jsonProposal.get("description") == "", "Поле description не пустое"

    assert jsonProposal["portfolioTools"]["investmentTools"] == []
    assert len(jsonProposal["portfolioTools"]["investmentTools"]) == 0

def test_post_clients_proposals(auth):
    with open("body.json") as file:
        body = json.load(file)
    response = requests.patch("https://ef-pfp-test4.tusvc.bcs.ru/ef-pfp-bff-proposal/api/v1/cache/proposals/4c7f371a-ea20-4dc6-ab82-35254611570b", json = body ,headers = auth)
    response.raise_for_status()
    assert response.status_code == 200
    print(body)

    patchProposal = response.json()

    second_product = patchProposal["portfolioTools"]["liquidTools"][1]

    assert body["portfolio"]["liquidTools"][0]["temporalProposalToolId"] == second_product["temporalProposalToolId"]

@pytest.mark.test
@pytest.mark.parametrize("proposalId", ["0739b029-86b8-4a75-a241-066789969495"])
def test_proposals_id(auth, proposalId):
    url = f"https://ef-pfp-test1.tusvc.bcs.ru/ef-pfp-ms-proposal/api/v1/proposals/{proposalId}"
    response = requests.get(url, headers=auth)
    response.raise_for_status()

    jsonProposal = response.json()
    print(jsonProposal)

    assert jsonProposal['id'] == proposalId
    assert "Персональное финансовое предложение" in jsonProposal['name']

    path = parse("$.portfolio.liquidTools.[*].code")

    matches = [x.value for x in path.find(jsonProposal)]

    print(path.find(jsonProposal))
    print(matches)
