# Agent Monitor Workspace Rules

- 목적: Hermes/Dev/Chief/Claude 에이전트 운영 상태를 관측하는 대시보드 개발
- 절대 원칙: 실제 상태를 확인하지 않고 성공 보고 금지
- 데이터 우선순위: 프로세스/로그/세션/DB/설정 파일 실측 > 추정
- 초기 타깃 에이전트: heri(.hermes), dev(.hermes-dev), chief(.openclaw), claude(local cli/process)
- 주요 질문:
  1. 어떤 에이전트가 켜져 있는가?
  2. 어떤 게이트웨이가 연결되어 있는가?
  3. 메모리/RSS/로그/세션/DB 용량은 얼마나 쓰는가?
  4. 최근 delegate_task/서브에이전트 사용 흔적은 얼마나 되는가?
  5. context compression이 언제/어떻게 일어났는가?
