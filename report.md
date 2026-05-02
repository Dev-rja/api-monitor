# API Reliability Monitor — SLA Report

> Last updated: **2026-05-02 05:56 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.69% | 4621.3 | 10206.7 | 1000ms | 261/589 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 123.0 | 4088.9 | 1500ms | 2/589 |
| ❌ | `nasa_apod` | 68.76% | 46.18% | 3744.9 | 10549.1 | 2000ms | 317/589 |
| ❌ | `ipapi_check` | 87.61% | 100.0% | 156.1 | 353.0 | 2500ms | 0/589 |
| ⚠️ | `rest_countries` | 98.47% | 98.3% | 345.8 | 10221.5 | 2500ms | 10/589 |
| ⚠️ | `open_meteo_weather` | 98.64% | 97.28% | 716.4 | 14877.1 | 2000ms | 16/589 |
| ⚠️ | `dog_ceo_random` | 99.49% | 92.87% | 732.1 | 10244.1 | 2500ms | 42/589 |
| ✅ | `catfact_random` | 99.49% | 99.49% | 250.2 | 10080.2 | 3000ms | 3/589 |
| ✅ | `useless_fact` | 99.66% | 99.32% | 585.4 | 10229.6 | 2500ms | 4/589 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 99.0 | 252.0 | 1500ms | 0/589 |
| ✅ | `agify_name` | 100.0% | 99.83% | 370.1 | 3237.1 | 2000ms | 1/589 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 238.1 | 3882.8 | 2000ms | 2/589 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 07:00 | 5197.7 | 50.0% |
| `numbers_trivia` | 18:00 | 5196.2 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 14:00 | 4872.4 | 46.88% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
