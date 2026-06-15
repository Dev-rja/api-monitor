# API Reliability Monitor — SLA Report

> Last updated: **2026-06-15 23:14 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.86% | 2606.4 | 10206.7 | 1000ms | 266/1102 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 125.7 | 4595.4 | 1500ms | 4/1102 |
| ❌ | `nasa_apod` | 75.5% | 53.27% | 3177.3 | 10565.8 | 2000ms | 515/1102 |
| ❌ | `ipapi_check` | 76.32% | 99.91% | 156.2 | 4507.0 | 2500ms | 1/1102 |
| ⚠️ | `rest_countries` | 98.64% | 98.37% | 341.3 | 10221.5 | 2500ms | 18/1102 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.73% | 718.8 | 14877.1 | 2000ms | 36/1102 |
| ✅ | `dog_ceo_random` | 99.55% | 96.19% | 561.2 | 10244.1 | 2500ms | 42/1102 |
| ✅ | `catfact_random` | 99.73% | 99.18% | 263.6 | 10080.2 | 3000ms | 9/1102 |
| ✅ | `coingecko_bitcoin` | 99.73% | 100.0% | 96.4 | 253.3 | 1500ms | 0/1102 |
| ✅ | `useless_fact` | 99.82% | 99.64% | 626.8 | 10229.6 | 2500ms | 4/1102 |
| ✅ | `agify_name` | 99.91% | 99.73% | 377.9 | 16112.2 | 2000ms | 3/1102 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.5 | 3882.8 | 2000ms | 2/1102 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 05:00 | 4214.9 | 65.52% |
| `nasa_apod` | 09:00 | 4014.2 | 52.08% |
| `nasa_apod` | 17:00 | 3993.9 | 54.1% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 01:00 | 3752.8 | 53.85% |
| `nasa_apod` | 18:00 | 3616.1 | 52.73% |
| `nasa_apod` | 14:00 | 3469.5 | 47.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
