# Agent Monitor Design V1

## Product Goal
Hermes(헤리/데브), OpenClaw(치프), Claude CLI 계열 에이전트의 실행 구조와 리소스 사용량을 단일 대시보드에서 관측한다.

## Primary Views
### 1. Fleet Overview
- agent name
- runtime status
- pid
- cpu %
- rss / vms
- uptime
- home path
- gateway status
- last error

### 1.5 Representative Dashboard Output (2026-04-09)
- 상단 KPI 카드: 활성 에이전트 수, 라이브 게이트웨이 수, 총 RSS, 총 스토리지
- Agent Overview 카드 4개: 헤리 / 데브 / 치프 / 클로드의 PID, 게이트웨이 상태, RSS/CPU, uptime, sessions, storage
- Resource Charts: 에이전트별 RSS 막대차트, 디스크 사용량 막대차트, session volume 막대차트
- Automation Snapshot: cron count, delegate traces, recent errors
- Storage Breakdown 표: sessions/logs/db/total
- Warnings 패널: 꺼진 에이전트, 중복 cloudflared, 최근 오류 흔적

### 2. Resource Heatmap
- agent별 RSS 비교
- logs/session/db 디스크 점유량 비교
- 최근 1h / 24h 변화량

### 3. Context & Memory View
- config 기준 memory enabled 여부
- memory char limits
- compression enabled/threshold/target ratio
- summary model/provider
- session count and latest updated time

### 4. Delegation View
- delegate_task 흔적
- background process 수
- cronjob 수
- child/subagent 실행 흔적

### 5. Gateway View
- telegram/discord 등 플랫폼 연결 여부
- polling/log error
- 중복 게이트웨이 탐지

## Collection Strategy
1. process collector
   - `ps`, `pgrep`, command line, rss/cpu/uptime
2. filesystem collector
   - HERMES_HOME, logs, sessions, DB size
3. config collector
   - yaml/json 파싱으로 model/memory/compression/gateway 추출
4. log collector
   - gateway log 최근 error/warn 수집
5. activity collector
   - sessions, cron definitions, delegate_task 흔적 집계

## Initial Target Paths
- `/Users/yosiki/.hermes`
- `/Users/yosiki/.hermes-dev`
- `/Users/yosiki/.openclaw`
- Claude 관련 실행 프로세스와 인증/로그 경로

## Non-Goals V1
- 원격 서버 모니터링
- 실시간 trace sampling
- 에이전트 내부 토큰 단위 billing 정산
