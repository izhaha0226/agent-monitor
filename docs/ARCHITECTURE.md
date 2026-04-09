# Architecture

## Layers
1. Collectors
- local process scanner
- config snapshot loader
- log summarizer
- storage size analyzer

2. Storage
- SQLite snapshot tables
- periodic snapshots for trend lines

3. API
- `/api/agents`
- `/api/overview`
- `/api/resources`
- `/api/context`
- `/api/delegation`
- `/api/gateways`

4. UI
- overview cards
- agent detail drawer
- charts/tables
- warnings panel

## First Implementation Order
1. collectors/process_inventory.py
2. collectors/config_inventory.py
3. collectors/storage_inventory.py
4. app/backend/main.py
5. app/frontend dashboard shell

## Risks
- Claude CLI 관측 포인트가 Hermes/OpenClaw보다 약할 수 있음
- subagent 사용 흔적은 로그/세션 포맷 의존성이 큼
- launchd/pty/tmux 기반 프로세스는 이름이 제각각일 수 있음
