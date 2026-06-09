# API Reliability Monitor — SLA Report

> Last updated: **2026-06-09 08:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.5% | 2742.6 | 10206.7 | 1000ms | 266/1043 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.5 | 4595.4 | 1500ms | 4/1043 |
| ❌ | `ipapi_check` | 76.13% | 99.9% | 156.6 | 4507.0 | 2500ms | 1/1043 |
| ❌ | `nasa_apod` | 76.32% | 55.32% | 3068.6 | 10565.8 | 2000ms | 466/1043 |
| ⚠️ | `rest_countries` | 98.56% | 98.27% | 350.3 | 10221.5 | 2500ms | 18/1043 |
| ⚠️ | `open_meteo_weather` | 98.95% | 96.93% | 704.5 | 14877.1 | 2000ms | 32/1043 |
| ✅ | `dog_ceo_random` | 99.52% | 95.97% | 572.2 | 10244.1 | 2500ms | 42/1043 |
| ✅ | `catfact_random` | 99.71% | 99.14% | 267.3 | 10080.2 | 3000ms | 9/1043 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.7 | 253.3 | 1500ms | 0/1043 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 622.9 | 10229.6 | 2500ms | 4/1043 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.0 | 16112.2 | 2000ms | 3/1043 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 221.7 | 3882.8 | 2000ms | 2/1043 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4070.4 | 51.72% |
| `nasa_apod` | 05:00 | 3993.8 | 64.29% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 11:00 | 3771.4 | 48.28% |
| `nasa_apod` | 01:00 | 3603.5 | 45.45% |
| `numbers_trivia` | 05:00 | 3427.1 | 32.14% |
| `nasa_apod` | 12:00 | 3363.9 | 47.83% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
