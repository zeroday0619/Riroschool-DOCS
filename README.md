# swagger-client
리로스쿨 2.9 버전의 API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.9.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
id = 'id_example' # str | 사용자 아이디
password = 'password_example' # str | 사용자 비밀번호
site_id = 'site_id_example' # str | 학교 아이디
parent = 'parent_example' # str | 학부모구분 엄마:M, 아빠:F (optional)

try:
    # 인증코드 요청
    api_instance.auth_authorize_get(client_id, id, password, site_id, parent=parent)
except ApiException as e:
    print("Exception when calling AuthApi->auth_authorize_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # 본인 인증 Callback 페이지
    api_instance.auth_callback_post()
except ApiException as e:
    print("Exception when calling AuthApi->auth_callback_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # 본인 인증 cancel 페이지
    api_instance.auth_cancel_post()
except ApiException as e:
    print("Exception when calling AuthApi->auth_cancel_post: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
tid = 'tid_example' # str | 본인인증에서 callback 받은 tid
auth_info = 'auth_info_example' # str | 본인인증에서 callback 받은 auth_info

try:
    # 본인 인증
    api_instance.auth_info_get(client_id, tid, auth_info)
except ApiException as e:
    print("Exception when calling AuthApi->auth_info_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
cookie_token = 'cookie_token_example' # str | API Key

try:
    # 업데이트 이전 사용자들 새 버전로그인으로 갈아타기
    api_instance.auth_login_get(client_id, cookie_token)
except ApiException as e:
    print("Exception when calling AuthApi->auth_login_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
site_id = 'site_id_example' # str | 학교 아이디

try:
    api_instance.auth_me_get(client_id, site_id)
except ApiException as e:
    print("Exception when calling AuthApi->auth_me_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
authorization = 'authorization_example' # str | 토큰 : tokenType + ' ' + refreshToken

try:
    # 토큰 재발급
    api_instance.auth_refesh_token_get(client_id, authorization)
except ApiException as e:
    print("Exception when calling AuthApi->auth_refesh_token_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
authorization_code = 'authorization_code_example' # str | 인증 코드

try:
    # 로그아웃
    api_instance.auth_sign_out_get(client_id, authorization_code)
except ApiException as e:
    print("Exception when calling AuthApi->auth_sign_out_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
client_id = 'client_id_example' # str | API Key
authorization_code = 'authorization_code_example' # str | 인증 코드

try:
    # 토큰 발급
    api_instance.auth_token_get(client_id, authorization_code)
except ApiException as e:
    print("Exception when calling AuthApi->auth_token_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://apidev.riroschool.kr*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthApi* | [**auth_authorize_get**](docs/AuthApi.md#auth_authorize_get) | **GET** /api/v2/auth/authorize | 인증코드 요청
*AuthApi* | [**auth_callback_post**](docs/AuthApi.md#auth_callback_post) | **POST** /api/v2/callback | 본인 인증 Callback 페이지
*AuthApi* | [**auth_cancel_post**](docs/AuthApi.md#auth_cancel_post) | **POST** /api/v2/cancel | 본인 인증 cancel 페이지
*AuthApi* | [**auth_info_get**](docs/AuthApi.md#auth_info_get) | **GET** /api/v2/auth/info | 본인 인증
*AuthApi* | [**auth_login_get**](docs/AuthApi.md#auth_login_get) | **GET** /api/v2/old/login | 업데이트 이전 사용자들 새 버전로그인으로 갈아타기
*AuthApi* | [**auth_me_get**](docs/AuthApi.md#auth_me_get) | **GET** /api/v2/auth/me | 
*AuthApi* | [**auth_refesh_token_get**](docs/AuthApi.md#auth_refesh_token_get) | **GET** /api/v2/auth/refresh-token | 토큰 재발급
*AuthApi* | [**auth_sign_out_get**](docs/AuthApi.md#auth_sign_out_get) | **GET** /api/v2/auth/sign-out | 로그아웃
*AuthApi* | [**auth_token_get**](docs/AuthApi.md#auth_token_get) | **GET** /api/v2/auth/token | 토큰 발급
*ChildApi* | [**child_delete**](docs/ChildApi.md#child_delete) | **DELETE** /api/v2/child | 자녀 등록 해제
*ChildApi* | [**child_get**](docs/ChildApi.md#child_get) | **GET** /api/v2/child | 자녀 목록
*ChildApi* | [**child_post**](docs/ChildApi.md#child_post) | **POST** /api/v2/child | 자녀 인증
*ChildApi* | [**child_put**](docs/ChildApi.md#child_put) | **PUT** /api/v2/child | 자녀 등록
*MemberApi* | [**auth_sign_up_post**](docs/MemberApi.md#auth_sign_up_post) | **POST** /api/v2/sign-up | 회원가입
*MemberApi* | [**member_change_password_get**](docs/MemberApi.md#member_change_password_get) | **GET** /api/v2/change-password | 비밀번호 변경
*MemberApi* | [**member_check_id_get**](docs/MemberApi.md#member_check_id_get) | **GET** /api/v2/check/{siteId}/{id} | 아이디 중복체크
*MemberApi* | [**member_confirm_password_get**](docs/MemberApi.md#member_confirm_password_get) | **GET** /api/v2/confirm-password | 비밀번호 확인
*MemberApi* | [**member_find_id_get**](docs/MemberApi.md#member_find_id_get) | **GET** /api/v2/find-id | 아이디 찾기
*MemberApi* | [**member_find_password_get**](docs/MemberApi.md#member_find_password_get) | **GET** /api/v2/find-password | 비밀번호 찾기 / 처음에 인증번호 없이 보내면 알림톡으로 인증번호 발송됨 두번째는 인증번호와 함께 다시 전송.
*MemberApi* | [**member_info_get**](docs/MemberApi.md#member_info_get) | **GET** /api/v2/info | 내정보 가져가기
*MemberApi* | [**member_info_put**](docs/MemberApi.md#member_info_put) | **PUT** /api/v2/info | 내정보 수정하기
*MemberApi* | [**member_me_get**](docs/MemberApi.md#member_me_get) | **PUT** /api/v2/me | 내 정보
*MemberApi* | [**member_phone_get**](docs/MemberApi.md#member_phone_get) | **GET** /api/v2/phone | 전화번호 인증
*MessageApi* | [**message_badge_get**](docs/MessageApi.md#message_badge_get) | **GET** /api/v2/badge | 뱃지 가져오기
*MessageApi* | [**message_message_delete**](docs/MessageApi.md#message_message_delete) | **DELETE** /api/v2/message | 메시지 삭제하기
*MessageApi* | [**message_message_get**](docs/MessageApi.md#message_message_get) | **GET** /api/v2/message | 메시지 가져오기
*MessageApi* | [**message_read_get**](docs/MessageApi.md#message_read_get) | **GET** /api/v2/message/read | 메시지 읽음 표시
*SchoolApi* | [**check_get**](docs/SchoolApi.md#check_get) | **GET** /api/v2/check | 상태 체크
*SchoolApi* | [**health_check_get**](docs/SchoolApi.md#health_check_get) | **GET** /api/v2/health-check | 상태 체크
*SchoolApi* | [**school_get**](docs/SchoolApi.md#school_get) | **GET** /api/v2/school | 리로스쿨 학교 리스트
*SchoolApi* | [**school_menu_get**](docs/SchoolApi.md#school_menu_get) | **GET** /api/v2/menu | 학교 사이드 메뉴
*SchoolApi* | [**school_search_get**](docs/SchoolApi.md#school_search_get) | **GET** /api/v2/school/{search} | 리로스쿨 학교 검색

## Documentation For Models

 - [Child](docs/Child.md)
 - [Device](docs/Device.md)
 - [Member](docs/Member.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

develop@rirosoft.com