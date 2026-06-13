# API Reliability Monitor — SLA Report

> Last updated: **2026-06-13 23:35 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.0%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 75.48% | 2643.9 | 10206.7 | 1000ms | 266/1085 |
| ❌ | `public_apis_list` | 0.0% | 99.63% | 125.9 | 4595.4 | 1500ms | 4/1085 |
| ❌ | `nasa_apod` | 75.76% | 54.01% | 3143.2 | 10565.8 | 2000ms | 499/1085 |
| ❌ | `ipapi_check` | 76.22% | 99.91% | 156.5 | 4507.0 | 2500ms | 1/1085 |
| ⚠️ | `rest_countries` | 98.62% | 98.34% | 343.7 | 10221.5 | 2500ms | 18/1085 |
| ⚠️ | `open_meteo_weather` | 98.89% | 96.68% | 721.0 | 14877.1 | 2000ms | 36/1085 |
| ✅ | `dog_ceo_random` | 99.54% | 96.13% | 565.6 | 10244.1 | 2500ms | 42/1085 |
| ✅ | `catfact_random` | 99.72% | 99.17% | 265.1 | 10080.2 | 3000ms | 9/1085 |
| ✅ | `coingecko_bitcoin` | 99.72% | 100.0% | 96.5 | 253.3 | 1500ms | 0/1085 |
| ✅ | `useless_fact` | 99.82% | 99.63% | 626.6 | 10229.6 | 2500ms | 4/1085 |
| ✅ | `agify_name` | 99.91% | 99.72% | 378.8 | 16112.2 | 2000ms | 3/1085 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.82% | 219.9 | 3882.8 | 2000ms | 2/1085 |

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
