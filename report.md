# API Reliability Monitor — SLA Report

> Last updated: **2026-06-13 20:58 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.44% | 2648.3 | 10206.7 | 1000ms | 266/1083 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.8 | 4595.4 | 1500ms | 4/1083 |
| ❌ | `nasa_apod` | 75.72% | 54.02% | 3146.4 | 10565.8 | 2000ms | 498/1083 |
| ❌ | `ipapi_check` | 76.18% | 99.91% | 156.6 | 4507.0 | 2500ms | 1/1083 |
| ⚠️ | `rest_countries` | 98.61% | 98.34% | 344.1 | 10221.5 | 2500ms | 18/1083 |
| ⚠️ | `open_meteo_weather` | 98.89% | 96.68% | 721.3 | 14877.1 | 2000ms | 36/1083 |
| ✅ | `dog_ceo_random` | 99.54% | 96.12% | 566.1 | 10244.1 | 2500ms | 42/1083 |
| ✅ | `catfact_random` | 99.72% | 99.17% | 265.4 | 10080.2 | 3000ms | 9/1083 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.6 | 253.3 | 1500ms | 0/1083 |
| ✅ | `useless_fact` | 99.82% | 99.63% | 626.5 | 10229.6 | 2500ms | 4/1083 |
| ✅ | `agify_name` | 99.91% | 99.72% | 378.8 | 16112.2 | 2000ms | 3/1083 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 220.1 | 3882.8 | 2000ms | 2/1083 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 05:00 | 4214.9 | 65.52% |
| `nasa_apod` | 09:00 | 4014.2 | 52.08% |
| `nasa_apod` | 17:00 | 4014.1 | 53.33% |
| `nasa_apod` | 11:00 | 3861.7 | 50.0% |
| `nasa_apod` | 01:00 | 3846.6 | 50.0% |
| `nasa_apod` | 18:00 | 3491.9 | 51.85% |
| `nasa_apod` | 12:00 | 3419.7 | 48.98% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
