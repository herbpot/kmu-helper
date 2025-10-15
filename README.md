# kmu-helper

2024년 2학기 국민대학교 헬퍼 교육 실습 코드 저장소입니다.

## 개요

이 레포지토리는 국민대학교 헬퍼 교육 프로그램에서 작성된 Python 실습 예제들을 포함합니다. 기초 알고리즘과 게임 로직 구현을 통해 Python 프로그래밍을 학습합니다.

## 포함된 프로그램

### 1. baseball.py (by hyeongu)
숫자 야구 게임 구현

**주요 기능:**
- 1-9 사이의 중복되지 않는 3자리 난수 생성
- 사용자 입력 검증 (3회 연속 실패시 종료)
- Strike/Ball 판정 로직
- 게임 재시작 기능

**게임 규칙:**
- 3자리 숫자를 맞추는 게임
- Strike: 숫자와 위치가 모두 일치
- Ball: 숫자는 일치하지만 위치가 다름
- Out: 일치하는 숫자가 없음

### 2. number.py (by inwoo)
숫자 관련 기본 연산 및 검증 프로그램

### 3. arraycheck.py (by inwoo)
배열 검증 및 처리 프로그램

## 기술 스택

- **Python 3.x**
- **표준 라이브러리**
  - `random` - 난수 생성
  - `sys` - 시스템 종료 처리

## 사용 방법

### 숫자 야구 게임 실행

```bash
python baseball.py
```

게임이 시작되면 3자리 숫자를 입력하세요:
```
숫자 야구 게임을 시작합니다.
123
2B 1S
```

### 기타 프로그램 실행

```bash
python number.py
python arraycheck.py
```

## 코드 예제

### baseball.py 핵심 로직

```python
# 숫자 검증 함수
def check(arr):
    if len(arr) != 3 or len(set(arr)) < 3:
        return True
    else:
        return False

# Strike/Ball 판정
s_cnt = 0
b_cnt = 0
for i in range(0, 3):
    for j in range(0, 3):
        if user[i] == answer[j]:
            if i == j:
                s_cnt += 1  # Strike
            elif i != j:
                b_cnt += 1  # Ball
            break
```

## 학습 목표

- Python 기본 문법 및 제어문 이해
- 리스트와 집합 자료구조 활용
- 사용자 입력 처리 및 검증
- 게임 로직 구현
- 함수 설계 및 모듈화

## 프로젝트 구조

```
kmu-helper/
├── baseball.py       # 숫자 야구 게임
├── number.py         # 숫자 연산 프로그램
├── arraycheck.py     # 배열 검증 프로그램
└── README.md
```

## 개발 환경

- Python 3.x 이상
- 텍스트 에디터 또는 IDE (VSCode, PyCharm 등)

## 실행 요구사항

- Python 3.x 설치
- 추가 패키지 설치 불필요 (표준 라이브러리만 사용)

## 참고 사항

- `there is no sudoku` - 스도쿠 프로그램은 포함되지 않음
- 교육용 프로젝트로, 기본적인 알고리즘 학습에 중점

## 기여자

- **inwoo** - number.py, arraycheck.py
- **hyeongu** - baseball.py

## 라이선스

교육 목적으로 작성된 프로젝트입니다.
