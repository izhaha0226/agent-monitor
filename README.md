# agent-monitor

Unified monitoring dashboard for Hermes / Dev / Chief / Claude agents.

Public site: https://izhaha0226.github.io/agent-monitor/
GitHub repo: https://github.com/izhaha0226/agent-monitor

## Goal
- 한눈에 에이전트 상태 확인
- 게이트웨이/프로세스/메모리/세션/컨텍스트 압축/서브에이전트 사용량 추적
- 어떤 에이전트가 리소스를 많이 먹는지 비교

## Initial Scope
- Agent registry: heri, dev, chief, claude
- Process metrics: pid, cpu, rss, start time, command
- Gateway metrics: enabled platform, status, log error count
- Session metrics: session count, latest session, transcript size
- Context metrics: compression 설정, 최근 압축 흔적, summary model
- Delegation metrics: delegate_task/subagent 호출 흔적, background process 수
- Storage metrics: HERMES_HOME/OpenClaw 디렉터리 용량, 로그 용량, DB 용량

## Planned Stack
- Backend: FastAPI
- Frontend: Next.js
- Storage: SQLite
- Collector: Python schedulers / scripts

## Project Layout
- `app/backend` — API
- `app/frontend` — dashboard UI
- `collectors` — local agent/gateway collectors
- `storage` — SQLite schema and snapshots
- `scripts` — bootstrap/run helpers
- `docs` — design and task documents
