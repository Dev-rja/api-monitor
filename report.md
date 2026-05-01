# API Reliability Monitor — SLA Report

> Last updated: **2026-05-01 23:59 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 55.54% | 4636.3 | 10206.7 | 1000ms | 261/587 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 123.0 | 4088.9 | 1500ms | 2/587 |
| ❌ | `nasa_apod` | 68.65% | 46.0% | 3756.5 | 10549.1 | 2000ms | 317/587 |
| ❌ | `ipapi_check` | 87.56% | 100.0% | 156.2 | 353.0 | 2500ms | 0/587 |
| ⚠️ | `rest_countries` | 98.47% | 98.3% | 346.0 | 10221.5 | 2500ms | 10/587 |
| ⚠️ | `open_meteo_weather` | 98.64% | 97.27% | 716.8 | 14877.1 | 2000ms | 16/587 |
| ⚠️ | `dog_ceo_random` | 99.49% | 92.84% | 733.3 | 10244.1 | 2500ms | 42/587 |
| ✅ | `catfact_random` | 99.49% | 99.49% | 249.6 | 10080.2 | 3000ms | 3/587 |
| ✅ | `useless_fact` | 99.66% | 99.32% | 585.0 | 10229.6 | 2500ms | 4/587 |
| ✅ | `coingecko_bitcoin` | 99.66% | 100.0% | 99.0 | 252.0 | 1500ms | 0/587 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.8 | 3237.1 | 2000ms | 1/587 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 237.6 | 3882.8 | 2000ms | 2/587 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 03:00 | 5523.2 | 53.33% |
| `nasa_apod` | 03:00 | 5403.4 | 86.67% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 07:00 | 5197.7 | 50.0% |
| `numbers_trivia` | 18:00 | 5196.2 | 50.0% |
| `numbers_trivia` | 10:00 | 5173.5 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `numbers_trivia` | 05:00 | 4949.4 | 47.37% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
