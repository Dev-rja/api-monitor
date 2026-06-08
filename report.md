# API Reliability Monitor — SLA Report

> Last updated: **2026-06-08 23:39 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 74.42% | 2749.9 | 10206.7 | 1000ms | 266/1040 |
| ❌ | `public_apis_list` | 0.0% | 99.62% | 125.5 | 4595.4 | 1500ms | 4/1040 |
| ❌ | `ipapi_check` | 76.15% | 99.9% | 156.7 | 4507.0 | 2500ms | 1/1040 |
| ❌ | `nasa_apod` | 76.54% | 55.48% | 3047.8 | 10565.8 | 2000ms | 463/1040 |
| ⚠️ | `rest_countries` | 98.56% | 98.27% | 350.8 | 10221.5 | 2500ms | 18/1040 |
| ⚠️ | `open_meteo_weather` | 98.94% | 97.02% | 700.4 | 14877.1 | 2000ms | 31/1040 |
| ✅ | `dog_ceo_random` | 99.52% | 95.96% | 573.2 | 10244.1 | 2500ms | 42/1040 |
| ✅ | `catfact_random` | 99.71% | 99.13% | 267.8 | 10080.2 | 3000ms | 9/1040 |
| ✅ | `coingecko_bitcoin` | 99.71% | 100.0% | 96.8 | 253.3 | 1500ms | 0/1040 |
| ✅ | `useless_fact` | 99.81% | 99.62% | 622.9 | 10229.6 | 2500ms | 4/1040 |
| ✅ | `agify_name` | 99.9% | 99.71% | 380.1 | 16112.2 | 2000ms | 3/1040 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.81% | 222.0 | 3882.8 | 2000ms | 2/1040 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 4070.4 | 51.72% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 11:00 | 3771.4 | 48.28% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `nasa_apod` | 12:00 | 3363.9 | 47.83% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
