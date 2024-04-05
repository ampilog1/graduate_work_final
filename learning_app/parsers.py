#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

__all__ = ('hh', 'superjob', 'zarplata')


def hh():
    params = {
        'text': 'python',
        'area': '1',
        'page': 0,
        'per_page': 20
    }
    headers = {
        "X-Api-App-Id": "v3.r.137504985.cc7e8d483cc20413f71b6861b28a159c6ae08e93.d80f6ee44097a2e0e1c5b34a4d8021cbbe4dd446"}
    url_vacancies = 'https://api.hh.ru/vacancies'
    req_python = requests.get(url_vacancies, headers=headers, params=params).json()
    data = []

    for item in req_python['items']:
        address = item['address']['raw'] if item['address'] is not None else 'нет адреса'
        salary = item['salary']['from'] if item['salary'] is not None else 'нет зарплаты'
        data.append({'name': item['name'], 'link': item['alternate_url'], 'address': address, 'salary': salary})

    return data


def superjob():
    url = 'https://api.superjob.ru/2.0/vacancies'
    headers = {
        "X-Api-App-Id": "v3.r.137504985.cc7e8d483cc20413f71b6861b28a159c6ae08e93.d80f6ee44097a2e0e1c5b34a4d8021cbbe4dd446"}
    params = {
        "catalogues": 48,
        "keyword": 'python',
        "town": '4',
        "count": '20'
    }
    # Получение страницы с вакансиями и ее декодирование
    req_python = requests.get(url, headers=headers, params=params).json()
    data = []

    for item in req_python['objects']:
        address = item['address'] if item['address'] is not None else 'нет адреса'
        salary = item['payment_from'] if item['payment_from'] is not None else 'нет зарплаты'
        data.append({'name': item['profession'], 'link': item['link'], 'address': address, 'salary': salary})

    return data


def zarplata():
    params = {
        'text': 'python',
        'area': '1',
        'page': 0,
        'per_page': 20
    }
    headers = {
        "X-Api-App-Id": "v3.r.137504985.cc7e8d483cc20413f71b6861b28a159c6ae08e93.d80f6ee44097a2e0e1c5b34a4d8021cbbe4dd446"}
    url_vacancies = 'https://api.zarplata.ru/vacancies/'
    req_python = requests.get(url_vacancies, headers=headers, params=params).json()
    data = []

    for item in req_python['items']:
        address = item['address']['raw'] if item['address'] is not None else 'нет адреса'
        salary = item['salary']['from'] if item['salary'] is not None else 'нет зарплаты'
        data.append({'name': item['name'], 'link': item['alternate_url'], 'address': address, 'salary': salary})

    return data


if __name__ == '__main__':
    data = zarplata()
    with open('zarplata.json', 'w', encoding='utf-8') as f:
        json.dump(data, f,
                  indent=4,
                  ensure_ascii=False)
