# API Reliability Monitor — SLA Report

> Last updated: **2026-04-21 14:50 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 66.27% | 3603.0 | 10206.7 | 1000ms | 140/415 |
| ❌ | `public_apis_list` | 0.0% | 99.52% | 130.1 | 4088.9 | 1500ms | 2/415 |
| ❌ | `nasa_apod` | 61.93% | 37.83% | 4322.7 | 10549.1 | 2000ms | 258/415 |
| ❌ | `ipapi_check` | 93.73% | 100.0% | 159.0 | 353.0 | 2500ms | 0/415 |
| ⚠️ | `open_meteo_weather` | 98.07% | 96.87% | 747.6 | 14877.1 | 2000ms | 13/415 |
| ⚠️ | `dog_ceo_random` | 99.28% | 89.88% | 877.6 | 10244.1 | 2500ms | 42/415 |
| ✅ | `catfact_random` | 99.28% | 99.28% | 277.1 | 10080.2 | 3000ms | 3/415 |
| ✅ | `useless_fact` | 99.52% | 99.04% | 586.7 | 10229.6 | 2500ms | 4/415 |
| ✅ | `agify_name` | 100.0% | 99.76% | 373.4 | 3237.1 | 2000ms | 1/415 |
| ✅ | `rest_countries` | 100.0% | 99.04% | 259.8 | 7269.1 | 2500ms | 4/415 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.76% | 232.8 | 2314.9 | 2000ms | 1/415 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.7 | 252.0 | 1500ms | 0/415 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 03:00 | 6314.9 | 91.67% |
| `nasa_apod` | 17:00 | 5778.8 | 70.83% |
| `nasa_apod` | 18:00 | 5606.7 | 82.35% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5164.2 | 64.0% |
| `numbers_trivia` | 10:00 | 4692.0 | 45.0% |
| `numbers_trivia` | 12:00 | 4658.8 | 44.44% |
| `nasa_apod` | 12:00 | 4598.1 | 66.67% |
| `nasa_apod` | 23:00 | 4535.5 | 55.17% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
