# KAIST MLP Lab 웹사이트 — 프로젝트 컨텍스트

## 목표

KAIST MLP Lab의 연구 프로젝트를 모아 보여주는 웹사이트를 GitHub Pages로 만든다.

우선순위는 다음 순서다.

1. **검색 노출 (최우선)**: Google, Bing 같은 검색엔진과 Claude, ChatGPT, Codex 같은 AI 도구가 우리 연구를 잘 찾고, 읽고, 인용할 수 있어야 한다. 디자인보다 이 원칙이 우선한다.
2. **프로젝트 페이지**: 논문마다 [https://llava-vl.github.io/](https://llava-vl.github.io/) 같은 프로젝트 페이지를 둔다. 이 스타일은 Nerfies 템플릿 기반이다.
3. **허브 사이트**: 모든 프로젝트 페이지를 한곳에 모아 보여주는 연구실 사이트를 둔다.

## 현재 상태

- GitHub organization `kaist-mlplab`을 만들었다.
- 레포 `kaist-mlplab/[kaist-mlplab.github.io](http://kaist-mlplab.github.io)`를 만들었고, 비어 있다(파일 없음).
- 나중에 [`mlplab.kaist.ac.kr`](http://mlplab.kaist.ac.kr) 도메인을 연결할 수 있다(KAIST 정보통신팀 승인 필요). 따라서 URL을 하드코딩하지 말고 설정 한 곳에서 바꿀 수 있게 만든다.

## 전체 구조

GitHub Pages에서는 org 아래 다른 레포가 [`kaist-mlplab.github.io/<레포이름>/`](http://kaist-mlplab.github.io/<레포이름>/) 주소로 열린다. 이 점을 이용해 모든 페이지를 한 도메인 아래에 모은다.


| 레포                                                        | 주소            | 역할                                             |
| --------------------------------------------------------- | ------------- | ---------------------------------------------- |
| [`kaist-mlplab.github.io`](http://kaist-mlplab.github.io) | `/`           | 허브: 연구실 소개, 프로젝트 목록, 구성원, 전체 sitemap           |
| `project-page-template`                                   | (배포 안 함)      | 프로젝트 페이지 템플릿. GitHub "Template repository"로 설정 |
| `<프로젝트명>` (예: `fooformer`)                                | `/fooformer/` | 개별 논문 프로젝트 페이지                                 |


프로젝트 레포 이름이 곧 URL이 된다. 소문자와 하이픈만 쓰고 짧게 짓는다(예: `fooformer`, `fast-vit`).

## 기술 원칙 (반드시 지킬 것)

- **결과물은 정적 HTML이어야 한다.** React, Vue 같은 SPA나 JavaScript로 본문을 렌더링하는 방식은 쓰지 않는다. 많은 AI 도구와 크롤러가 JS를 실행하지 않기 때문이다. 페이지 소스(view-source)만 봐도 모든 본문이 보여야 한다.
- 런타임에 JSON을 fetch해서 목록을 그리지 않는다. 목록도 빌드 시점에 HTML로 만든다.
- 허브는 **Jekyll**을 쓴다. GitHub Pages가 별도 Actions 없이 빌드해 준다. GitHub Pages 기본 허용 플러그인만 쓴다(`jekyll-seo-tag`, `jekyll-sitemap` 등).
- 프로젝트 페이지는 **순수 HTML + Bulma CSS**를 쓴다(Nerfies 방식). 빌드 과정이 없어야 한다.
- 무거운 프레임워크나 외부 의존성을 최소화한다. 이미지는 적절히 압축하고 모든 이미지에 의미 있는 `alt`를 단다.
- 모바일에서도 깨지지 않아야 한다.

## 허브 사이트 ([`kaist-mlplab.github.io`](http://kaist-mlplab.github.io))

### 페이지 구성

- `/`: 연구실 한 줄 소개, 연구 분야, 최신 프로젝트 카드 목록
- `/projects/`: 전체 프로젝트 목록(연도별 정렬, 학회/연도 표시)
- `/people/`: 교수, 구성원, 졸업생
- `/publications/`: 논문 목록(선택)

### 데이터 관리

- 프로젝트 정보는 `_data/projects.yml` 한 파일에서 관리한다. 새 프로젝트를 추가할 때 이 파일에 항목 하나만 넣으면 카드 목록과 sitemap에 모두 반영되게 만든다.
- 항목 예시:

```yaml
- slug: fooformer            # 프로젝트 레포 이름 = URL 경로
  title: "FooFormer: ..."
  venue: "NeurIPS 2026"
  year: 2026
  authors: ["Gildong Hong", "..."]
  summary: "한두 문장 영어 요약"
  thumbnail: /assets/img/projects/fooformer.jpg
  arxiv: https://arxiv.org/abs/xxxx.xxxxx
  code: https://github.com/kaist-mlplab/fooformer-code

```

- 구성원은 `_data/people.yml`로 관리한다.

### 검색 설정

- `_config.yml`에 `url`, `baseurl`, `title`, `description`을 둔다. 도메인을 바꿀 때 `url` 한 줄만 바꾸면 되게 한다.
- `jekyll-seo-tag`로 각 페이지에 title, description, canonical, Open Graph 태그를 넣는다.
- **sitemap.xml은 직접 만든다.** `jekyll-sitemap`은 이 레포 안의 페이지만 포함하므로, `_data/projects.yml`을 순회해 다른 레포의 프로젝트 페이지 주소(`/<slug>/`)까지 포함하는 Liquid 템플릿으로 `sitemap.xml`을 생성한다.
- `robots.txt`: 모든 크롤러를 허용하고(ClaudeBot, GPTBot 등 AI 크롤러도 막지 않음) sitemap 위치를 적는다.
- 홈페이지에 연구실 정보를 [schema.org](http://schema.org) `ResearchOrganization` JSON-LD로 넣는다.

## 프로젝트 페이지 템플릿 (`project-page-template`)

### 기반

- Nerfies 템플릿([https://github.com/nerfies/nerfies.github.io](https://github.com/nerfies/nerfies.github.io)) 또는 이를 정리한 Academic Project Page Template([https://github.com/eliahuhorwitz/Academic-project-page-template)을](https://github.com/eliahuhorwitz/Academic-project-page-template)을) 기반으로 한다.
- 라이선스는 CC BY-SA 4.0이다. 페이지 하단에 원본 템플릿 출처 표기를 반드시 남긴다.
- 레퍼런스 디자인: [https://llava-vl.github.io/](https://llava-vl.github.io/)

### 섹션 순서

1. 논문 제목, 부제
2. 학회/연도 배지
3. 저자(개인 페이지 링크), 소속(KAIST 명시), 공동 1저자 표시
4. 버튼: Paper(arXiv), PDF, Code, Demo, Dataset, Model(없는 버튼은 숨김)
5. 대표 그림(teaser)과 캡션
6. Abstract(텍스트)
7. 방법 설명(그림 + 텍스트)
8. 주요 결과(표는 이미지가 아니라 HTML `<table>`로)
9. BibTeX(복사 버튼 포함)
10. 허브로 돌아가는 링크("More projects from KAIST MLP Lab")
11. 하단: 템플릿 출처 표기

### 검색 설정 (템플릿에 기본 포함)

- `<title>`: 논문 제목 전체
- `<meta name="description">`: 논문 핵심을 한두 문장으로
- `<link rel="canonical">`
- Open Graph, Twitter card 태그(teaser 이미지 사용)
- Google Scholar용 Highwire 메타태그: `citation_title`, `citation_author`(저자마다 하나씩), `citation_publication_date`, `citation_conference_title` 또는 `citation_journal_title`, `citation_pdf_url`, `citation_arxiv_id`
- [schema.org](http://schema.org) `ScholarlyArticle` JSON-LD: 제목, 저자, 소속(KAIST), 날짜, 초록, arXiv/코드 링크
- 그림 속 핵심 결과는 캡션이나 본문 텍스트에도 수치로 적는다. 그림으로만 표현된 정보는 AI가 읽지 못한다.

### 사용 편의

- 바꿔야 할 부분을 `<!-- TODO: ... -->` 주석으로 명확히 표시한다.
- 레포 README에 "Use this template → 내용 수정 → Settings &gt; Pages 켜기 → 허브의 `_data/projects.yml`에 추가" 절차를 적는다.

## 작업 순서 제안

1. 허브 레포에 Jekyll 기본 구조, `_config.yml`, 레이아웃, 홈/프로젝트/구성원 페이지를 만든다.
2. 예시 데이터(가짜 프로젝트 1~2개)로 카드 목록, sitemap, robots.txt가 잘 생성되는지 확인한다.
3. 프로젝트 페이지 템플릿을 만든다. 처음에는 허브 레포의 `_template/` 폴더(Jekyll이 무시하도록 `_`로 시작)에 만들고, 확정되면 `project-page-template` 레포로 옮긴다.
4. 로컬 확인 후 push하고 Settings &gt; Pages에서 배포를 켠다.
5. Google Search Console, Bing Webmaster Tools에 sitemap을 등록한다(사람이 직접 할 일).

## 검증 체크리스트

- `curl`로 받은 HTML(JS 실행 없이)에 제목, 초록, 결과가 모두 보이는가
- 모든 페이지에 고유한 title, description, canonical이 있는가
- sitemap.xml에 허브 페이지와 모든 프로젝트 페이지 주소가 들어 있는가
- robots.txt가 크롤러를 막지 않는가
- JSON-LD가 문법적으로 올바른가(Google Rich Results Test로 확인 가능)
- 깨진 링크와 `alt` 없는 이미지가 없는가
- `_config.yml`의 `url`만 바꾸면 도메인 전체가 바뀌는가

## 아직 정해지지 않은 정보 (작업 중 사용자에게 물어볼 것)

- 연구실 정식 명칭(MLP의 풀네임), 소속 학과, 지도교수 이름과 연락처
- 연구실 한 줄 소개와 연구 분야
- 구성원 명단
- 첫 번째로 올릴 실제 프로젝트(논문) 정보
- 색상, 로고 등 디자인 선호



현재 우리 연구실 사이트 (프로젝트페이지 아님): [https://sites.google.com/view/aailab](https://sites.google.com/view/aailab)