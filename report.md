# API Reliability Monitor — SLA Report

> Last updated: **2026-06-16 20:30 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.97% | 2595.7 | 10206.7 | 1000ms | 266/1107 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 125.6 | 4595.4 | 1500ms | 4/1107 |
| ❌ | `nasa_apod` | 75.34% | 53.21% | 3186.3 | 11152.5 | 2000ms | 518/1107 |
| ❌ | `ipapi_check` | 76.15% | 99.91% | 156.2 | 4507.0 | 2500ms | 1/1107 |
| ⚠️ | `rest_countries` | 98.64% | 98.37% | 340.6 | 10221.5 | 2500ms | 18/1107 |
| ⚠️ | `open_meteo_weather` | 98.92% | 96.75% | 718.5 | 14877.1 | 2000ms | 36/1107 |
| ✅ | `dog_ceo_random` | 99.55% | 96.21% | 560.3 | 10244.1 | 2500ms | 42/1107 |
| ✅ | `catfact_random` | 99.73% | 99.19% | 263.7 | 10080.2 | 3000ms | 9/1107 |
| ✅ | `coingecko_bitcoin` | 99.73% | 100.0% | 96.4 | 253.3 | 1500ms | 0/1107 |
| ✅ | `useless_fact` | 99.82% | 99.64% | 627.0 | 10229.6 | 2500ms | 4/1107 |
| ✅ | `agify_name` | 99.91% | 99.73% | 377.8 | 16112.2 | 2000ms | 3/1107 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.1 | 3882.8 | 2000ms | 2/1107 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 05:00 | 4214.9 | 65.52% |
| `nasa_apod` | 17:00 | 4096.3 | 54.84% |
| `nasa_apod` | 09:00 | 4014.2 | 52.08% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 01:00 | 3752.8 | 53.85% |
| `nasa_apod` | 18:00 | 3616.1 | 52.73% |
| `nasa_apod` | 14:00 | 3469.5 | 47.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
