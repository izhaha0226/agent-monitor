# TASK_AGENT_MONITOR

## 목표
대표님이 Hermes 헤리, 데브, 치프, 클로드 4개 에이전트의 전체 동작 구조를 한눈에 볼 수 있는 agent-monitor 프로젝트를 신설한다.

## 1차 산출물
- GitHub repo: `izhaha0226/agent-monitor`
- 로컬 프로젝트 폴더: `/Users/yosiki/projects/agent-monitor`
- 초기 문서:
  - `README.md`
  - `CLAUDE.md`
  - `docs/DESIGN_V1.md`
  - `docs/ARCHITECTURE.md`
- 기본 디렉터리:
  - `app/backend`
  - `app/frontend`
  - `collectors`
  - `storage`
  - `scripts`
  - `tests`

## 대시보드 핵심 질문
1. 현재 어떤 에이전트/게이트웨이가 살아있는가?
2. 각각 어디(HERMES_HOME/OpenClaw/workspace) 데이터를 쓰는가?
3. 메모리(RSS), CPU, 디스크, 로그, 세션이 얼마나 쌓였는가?
4. context compression / summary model / memory limits는 어떻게 설정되어 있는가?
5. delegate_task, background process, cronjob 등 보조 실행이 얼마나 돌고 있는가?

## 구현 원칙
- 실측 데이터 우선
- OpenClaw/Hermes 설정 차이를 통합 뷰로 보여주기
- 허위 성공 보고 금지
- 초기엔 로컬 mac mini 관측 중심
