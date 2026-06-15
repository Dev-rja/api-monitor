# API Reliability Monitor — SLA Report

> Last updated: **2026-06-15 21:21 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.84% | 2608.7 | 10206.7 | 1000ms | 266/1101 |
| ❌ | `public_apis_list` | 0.0% | 99.64% | 125.6 | 4595.4 | 1500ms | 4/1101 |
| ❌ | `nasa_apod` | 75.48% | 53.32% | 3177.8 | 10565.8 | 2000ms | 514/1101 |
| ❌ | `ipapi_check` | 76.39% | 99.91% | 156.2 | 4507.0 | 2500ms | 1/1101 |
| ⚠️ | `rest_countries` | 98.64% | 98.37% | 341.5 | 10221.5 | 2500ms | 18/1101 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.73% | 719.1 | 14877.1 | 2000ms | 36/1101 |
| ✅ | `dog_ceo_random` | 99.55% | 96.19% | 561.4 | 10244.1 | 2500ms | 42/1101 |
| ✅ | `catfact_random` | 99.73% | 99.18% | 263.7 | 10080.2 | 3000ms | 9/1101 |
| ✅ | `coingecko_bitcoin` | 99.73% | 100.0% | 96.4 | 253.3 | 1500ms | 0/1101 |
| ✅ | `useless_fact` | 99.82% | 99.64% | 626.9 | 10229.6 | 2500ms | 4/1101 |
| ✅ | `agify_name` | 99.91% | 99.73% | 378.1 | 16112.2 | 2000ms | 3/1101 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.5 | 3882.8 | 2000ms | 2/1101 |

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
