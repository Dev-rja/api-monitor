# API Reliability Monitor — SLA Report

> Last updated: **2026-05-02 07:53 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.76% | 4613.7 | 10206.7 | 1000ms | 261/590 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 123.2 | 4088.9 | 1500ms | 2/590 |
| ❌ | `nasa_apod` | 68.81% | 46.27% | 3739.5 | 10549.1 | 2000ms | 317/590 |
| ❌ | `ipapi_check` | 87.63% | 100.0% | 156.1 | 353.0 | 2500ms | 0/590 |
| ⚠️ | `rest_countries` | 98.47% | 98.31% | 345.4 | 10221.5 | 2500ms | 10/590 |
| ⚠️ | `open_meteo_weather` | 98.64% | 97.29% | 715.9 | 14877.1 | 2000ms | 16/590 |
| ⚠️ | `dog_ceo_random` | 99.49% | 92.88% | 731.5 | 10244.1 | 2500ms | 42/590 |
| ✅ | `catfact_random` | 99.49% | 99.49% | 249.9 | 10080.2 | 3000ms | 3/590 |
| ✅ | `coingecko_bitcoin` | 99.49% | 100.0% | 99.0 | 252.0 | 1500ms | 0/590 |
| ✅ | `useless_fact` | 99.66% | 99.32% | 585.5 | 10229.6 | 2500ms | 4/590 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.7 | 3237.1 | 2000ms | 1/590 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 238.1 | 3882.8 | 2000ms | 2/590 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 18:00 | 5196.2 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 14:00 | 4872.4 | 46.88% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
